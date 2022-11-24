# Python Imports
import sys
import datetime
import json
import keyboard
import psutil
import requests
import os
import time
from enum import Enum, auto

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QMessageBox
from PySide6.QtCore import Slot, Signal, QObject, QThread, QSettings, QFile, QTextStream, QStandardPaths, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QPixmap, QIcon

# PhasmoCompanion Imports
import Resources
from PhasmoClasses import Map, Evidence, Phasmo, Windows, ghosts_data, table_html, map_data
from UI_Components import Ui_PhasmoCompanion
from qt_material import apply_stylesheet

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
    @staticmethod
    def get(value):
        for level in LogLevel:
            if(value == level.value):
                return level
        return LogLevel.INFO

class KeyEvent(Enum):
    CYCLE_EVIDENCE_1 = auto()
    CYCLE_EVIDENCE_2 = auto()
    CYCLE_EVIDENCE_3 = auto()
    CYCLE_TABS = auto()
    MAP_LEFT = auto()
    MAP_RIGHT = auto()
    RESET = auto()


class PhasmoCompanion(QMainWindow, Ui_PhasmoCompanion):
    ui = None
    phasmo = None
    selectedEvidence = []
    possibleGhostsModel = None
    selectedMap = None
    
    def __init__(self):
        super(PhasmoCompanion, self).__init__()

        #Load UI Components
        self.setupUi(self)
        
        #Ghost Data URL
        self.ghostdata_url = "https://lightplanstudio.com/api/phasmo/ghostdata.json"

        #Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        theme_file = QFile(":resources/ui/themes/dark_cyan.xml")
        theme_file.open(QFile.ReadOnly)
        theme_text_stream = QTextStream(theme_file)
        theme_file_text = theme_text_stream.readAll()
        self.setWindowTitle(f"PhasmoCompanion {self.version}")
        
        #Load Settings
        self.log_level = LogLevel.DEBUG
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if(not os.path.isdir(self.config_dir)):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, "PhasmoCompanion.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        #Write Theme File
        theme_path = os.path.join(self.config_dir, "dark_cyan.xml").replace("\\", "/")
        with open(theme_path, "w") as fd:
            fd.write(theme_file_text)

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        #Initialize the starting evidence / map
        self.selectedEvidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.selectedMap = Map.TANGLEWOOD
        
        #Add Model to ListView
        self.possibleGhostsModel = QStandardItemModel()
        self.ghost_listwidget.setModel(self.possibleGhostsModel)
        
        #Setup Button Signals
        self.cycleEvidenceButtonL1.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonL2.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonL3.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR1.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR2.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR3.clicked.connect(self.cycleEvidence)
        self.resetEvidenceButton.clicked.connect(self.resetEvidence)
        self.verbose_checkbox.stateChanged.connect(self.verbose_checkbox_clicked)

        #Local KeyEvent Listener to Communicate with Stream Deck
        self.key_listener = KeyListener()
        self.key_listener.signals.key_event.connect(self.process_key_event)
        self.key_listener.signals.log.connect(self.log)
        self.key_listener.start()

        # Set Theme
        apply_stylesheet(self, theme=theme_path)
        
        # Set Label font sizes
        self.evidenceLabel1.setStyleSheet("font-size: 20px;")
        self.evidenceLabel2.setStyleSheet("font-size: 20px;")
        self.evidenceLabel3.setStyleSheet("font-size: 20px;")
        self.ghost_listwidget.setStyleSheet("font-size: 20px;")

        #Set the verbose log checkbox
        self.verbose_logs = int(self.settings.value("PhasmoCompanion/verbose_logs", "0"))
        if self.verbose_logs == 1:
            self.verbose_checkbox.setChecked(True)
            self.verbose_logs = True
        else:
            self.verbose_checkbox.setChecked(False)
            self.verbose_logs = False

        self.log(f"Config File Loaded: {self.config_dir}", LogLevel.DEBUG)

        #Update Ghost Data
        self.log("Updating Ghost Data")
        self.ghost_data = self.fetch_ghostdata()
        self.log("Ghost Data Updated!")
        
        #Build Phasmo Object with Ghost Data
        self.phasmo = Phasmo(self.ghost_data)

        #Initialize Possible Ghosts and Info Panel
        self.updateSelectedEvidence()
        self.infoTabWidget.setCurrentIndex(0)

        #Finally, Show the UI
        geometry = self.settings.value("PhasmoCompanion/geometry")
        window_state = self.settings.value("PhasmoCompanion/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()
        QTimer.singleShot(2000, self.checkStart)
    
    def checkStart(self):
        start = time.time()
        while time.time() - start < 3:
            if self.key_listener and self.key_listener.started:
                self.log("Ready to hunt some ghosts!")
                return
        self.log("KeyEventListener did not start! (5 sec timeout)", LogLevel.ERROR)

    def process_key_event(self, event=KeyEvent.RESET):
        self.log(f"Key Event: {event}", LogLevel.DEBUG)
        if(event == KeyEvent.CYCLE_EVIDENCE_1):
            self.cycleSingle(0)
        elif(event == KeyEvent.CYCLE_EVIDENCE_2):
            self.cycleSingle(1)
        elif(event == KeyEvent.CYCLE_EVIDENCE_3):
            self.cycleSingle(2)
        elif(event == KeyEvent.RESET):
            self.resetEvidence()
        elif(event == KeyEvent.MAP_LEFT):
            #self.cycleMapSingle(-1)
            pass
        elif(event == KeyEvent.MAP_RIGHT):
            #self.cycleMapSingle(1)
            pass

    def verbose_checkbox_clicked(self):
        verbose = self.verbose_checkbox.isChecked()
        if verbose:
            self.settings.setValue("PhasmoCompanion/verbose_logs", "1")
        else:
            self.settings.setValue("PhasmoCompanion/verbose_logs", "0")
        self.log(f"Verbose Logs Set: {verbose}")
        

    def fetch_ghostdata(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        self.log(f"Ghost Data URL: {self.ghostdata_url}", LogLevel.DEBUG)
        try:
            r = requests.get(self.ghostdata_url, headers=headers)
            if r.status_code >= 200 and r.status_code < 300:
                self.log(f"HTTP Status Code: {r.status_code}", LogLevel.DEBUG)
                data = r.json()
                n = len(data)
                self.log(f"Processing {n} Ghosts' Data", LogLevel.DEBUG)
                #Convert Evidence strings to enums
                for x in range(len(data)):
                    evidenceList = []
                    for i in range(len(data[x]["evidence"])):
                        evidenceList.append(Evidence[data[x]["evidence"][i]])
                    data[x]["evidence"] = evidenceList
                return data
            else:
                self.log(f"Error HTTP Status Code: {r.status_code}", LogLevel.ERROR)
        except Exception as e:
            self.log(repr(e), LogLevel.ERROR)
        self.log("Ghost Data could not be updated. Using fallback data.", LogLevel.ERROR)
        return ghosts_data

    def refresh_ghosts_table(self):
        self.possibleGhostsModel.clear()
        for ghost in self.phasmo.possible_ghosts:
            ghost_str = ghost.get_name_with_evidence(self.selectedEvidence)
            item = QStandardItem(ghost_str)
            self.possibleGhostsModel.appendRow(item)

    def refresh_notes(self):
        table = ""
        for ghost in self.phasmo.possible_ghosts:
            table += "<tr>"
            table += f"<td>{ghost.name}</td>"
            table += f"<td><b>Strength:</b><br>{ghost.strength}<p>"
            table += f"<b>Weakness:</b><br>{ghost.weakness}</td>"
            table += f"<b>Notes:</b><br>{ghost.notes}</td>"
            table += "</tr>"
        html = table_html.replace("TABLECONTENTS", table)
        notes = self.phasmo.get_evidence_notes()
        html = html.replace("NOTES", notes)
        self.info_browser.setHtml(html)

    def updateSelectedEvidence(self):
        self.evidenceLabel1.setText(str(self.selectedEvidence[0]))
        self.evidenceLabel2.setText(str(self.selectedEvidence[1]))
        self.evidenceLabel3.setText(str(self.selectedEvidence[2]))
        self.phasmo.update_current_evidence(self.selectedEvidence)
        self.refresh_ghosts_table()
        self.refresh_notes()
        
    @Slot()
    def resetEvidence(self):
        self.selectedEvidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.updateSelectedEvidence()
    
    def cycleSingle(self, evidenceNumber, step=1):
        if(evidenceNumber < 0 or evidenceNumber > 2):
            return  
        sel = self.selectedEvidence[evidenceNumber].value
        sel += step
        if(sel < 0):
            sel = len(Evidence)-1
        elif(sel >= len(Evidence)):
            sel = 0
        self.selectedEvidence[evidenceNumber] = Evidence(sel)
        self.updateSelectedEvidence()

    @Slot()
    def cycleEvidence(self):
        sender = self.sender()
        if(sender == self.cycleEvidenceButtonL1):
            self.cycleSingle(0, -1)
        elif(sender == self.cycleEvidenceButtonR1):
            self.cycleSingle(0, 1)
        elif(sender == self.cycleEvidenceButtonL2):
            self.cycleSingle(1, -1)
        elif(sender == self.cycleEvidenceButtonR2):
            self.cycleSingle(1, 1)
        elif(sender == self.cycleEvidenceButtonL3):
            self.cycleSingle(2, -1)
        elif(sender == self.cycleEvidenceButtonR3):
           self.cycleSingle(2, 1)
    
    def cycleMapSingle(self, step=1):
        sel = self.selectedMap.value
        sel += step
        if(sel < 0):
            sel = len(Map)-1
        elif(sel >= len(Map)):
            sel = 0
        self.selectedMap = Map(sel)
        self.updateSelectedMap()
        
    @Slot()
    def cycleMap(self):
        sender = self.sender()
        if(sender == self.cycleMapButtonL):
            self.cycleMapSingle(-1)
        elif(sender == self.cycleMapButtonR):
            self.cycleMapSingle(1)

    def closeEvent(self, evt):
        self.key_listener.die()
        self.settings.setValue("PhasmoCompanion/geometry", self.saveGeometry())
        self.settings.setValue("PhasmoCompanion/windowState", self.saveState())
        self.settings.sync()
        self.log("Closing PhasmoCompanion")

    def log(self, msg, level=LogLevel.INFO):
        if(not msg or level.value > self.log_level.value):
            return
        if(level == LogLevel.ERROR):
            style = "color: #cc0000;"
        elif(level == LogLevel.DEBUG):
            if self.verbose_logs == False:
                return
            style = "color: #006600;"
        elif(level == LogLevel.INFO):
            style = "color: #FFFFFF;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        self.log_edit.append(msg)


class KeyListener(QThread):
    # Pass along the Signals
    class Signals(QObject):
        key_event = Signal(KeyEvent)
        log = Signal(str, LogLevel)

    def __init__(self, host="127.0.0.1", port=35387):
        super().__init__()
        self.signals = self.Signals()
        self.started = False

    def run(self):
        keyboard.add_hotkey('ctrl+shift+1', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_1))
        keyboard.add_hotkey('ctrl+shift+2', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_2))
        keyboard.add_hotkey('ctrl+shift+3', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_3))
        keyboard.add_hotkey('ctrl+shift+4', lambda: self.signals.key_event.emit(KeyEvent.RESET))
        keyboard.add_hotkey('ctrl+shift+5', lambda: self.signals.key_event.emit(KeyEvent.MAP_LEFT))
        keyboard.add_hotkey('ctrl+shift+6', lambda: self.signals.key_event.emit(KeyEvent.MAP_RIGHT))
        keyboard.add_hotkey('ctrl+shift+7', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_TABS))
        self.started = True
        self.log("KeyEvent Listener Started")

    def die(self):
        # In case KeyListener needs a Deconstructor
        self.log("KeyEvent Listener Stopped")

    def log(self, msg, level=LogLevel.INFO):
        self.signals.log.emit(msg, level)

def checkIfProcessRunning(processName):
        '''
        Check if there is any running process that contains the given name processName.
        '''
        #Iterate over the all the running process
        for proc in psutil.process_iter():
            try:
                # Check if process name contains the given name string.
                if processName.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False;

if __name__ == "__main__":
    if checkIfProcessRunning("PhasmoCompanion.exe"):
        print("PhasmoCompanion is already running.")
        #sys.exit(0)
    app = QApplication(sys.argv)
    version = "1"
    org_name = "ChillAspect"
    app_name = "PhasmoCompanion"
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = PhasmoCompanion()
    sys.exit(app.exec())