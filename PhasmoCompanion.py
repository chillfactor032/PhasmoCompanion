# Python Imports
import sys
import socketserver
import socket
import datetime
import json
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QMessageBox
from PySide6.QtCore import Slot, Signal, QObject, QThread, QSettings, QFile, QTextStream, QStandardPaths
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIntValidator, QPixmap, QIcon

# PhasmoCompanion Imports
import Resources
from PhasmoClasses import Map, Evidence, Phasmo, ghosts_data, table_html, map_data
from UI_Components import Ui_PhasmoCompanion

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

class PhasmoCompanion(QMainWindow, Ui_PhasmoCompanion):
    ui = None
    phasmo = None
    selectedEvidence = []
    possibleGhostsModel = None
    selectedMap = None
    
    def __init__(self, settings):
        super(PhasmoCompanion, self).__init__()
        #Load UI Components
        self.setupUi(self)
        

        #Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.setWindowTitle(f"PhasmoCompanion {self.version}")
        
        #Load Settings
        self.log_level = LogLevel.DEBUG
        self.settings = settings

        #Set window Icon
        pixmapi = QStyle.StandardPixmap.SP_FileDialogListView
        icon = self.style().standardIcon(pixmapi)
        self.setWindowIcon(icon)

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        #Local Host and Port for StreamDeck Communication
        self.host = settings.value("PhasmoCompanion/host", "127.0.0.1")
        self.port = int(settings.value("PhasmoCompanion/port", 39211))
        self.host_edit.setText(self.host)
        self.port_edit.setText(str(self.port))
        self.log(f"Setting UDP Server {self.host}:{self.port}")

        #Initialize the starting evidence / map
        self.selectedEvidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.selectedMap = Map.TANGLEWOOD
        
        #Add Model to ListView
        self.possibleGhostsModel = QStandardItemModel()
        self.ghostsListView.setModel(self.possibleGhostsModel)
        
        #Setup Button Signals
        self.save_settings_button.clicked.connect(self.save_settings)
        self.cycleEvidenceButtonL1.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonL2.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonL3.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR1.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR2.clicked.connect(self.cycleEvidence)
        self.cycleEvidenceButtonR3.clicked.connect(self.cycleEvidence)
        self.cycleMapButtonL.clicked.connect(self.cycleMap)
        self.cycleMapButtonR.clicked.connect(self.cycleMap)
        self.resetEvidenceButton.clicked.connect(self.resetEvidence)
        
        #Local UDP Server to Communicate with Stream Deck
        self.server = UDPServer(self.host, self.port)
        self.server.signals.get.connect(self.udpRecv)
        self.server.signals.log.connect(self.log)
        self.server.start()
        
        #Build Phasmo Object with Ghost Data
        self.phasmo = Phasmo(ghosts_data)
        
        #Initialize Possible Ghosts and Info Panel
        self.updateSelectedEvidence()
        self.updateSelectedMap()
        self.infoTabWidget.setCurrentIndex(0)

        # Setup Settings Panel
        self.port_validator = QIntValidator(10000, 65535, self)
        self.port_edit.setValidator(self.port_validator)

        #Finally, Show the UI
        geometry = self.settings.value("PhasmoCompanion/geometry")
        window_state = self.settings.value("PhasmoCompanion/windowState")
        print(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation))
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()
    
    def cycleTabs(self):
        curWidget = self.infoTabWidget.currentWidget()
        if(curWidget == self.ghostInfoTab):
            self.infoTabWidget.setCurrentWidget(self.mapInfoTab)
        if(curWidget == self.mapInfoTab):
            self.infoTabWidget.setCurrentWidget(self.ghostInfoTab)

    def save_settings(self):
        host = self.host_edit.text()
        port = int(self.port_edit.text())
        self.settings.setValue("PhasmoCompanion/host", host)
        self.settings.setValue("PhasmoCompanion/port", port)
        self.settings.sync()
        if(host != self.host or port != self.port):
            self.log("Server Restart Required.")
            self.restart_server()
            QMessageBox.information(self, "PhasmoCompanion", "Settings Saved\n\nUDP Server Restarted.")
        else:
            QMessageBox.information(self, "PhasmoCompanion", "Settings Saved.")
        
    @Slot()
    def udpRecv(self, msg):
        self.log(f"UDP Recv: {msg}")
        if(msg == "e1"):
            self.cycleSingle(0)
        elif(msg == "e2"):
            self.cycleSingle(1)
        elif(msg == "e3"):
            self.cycleSingle(2)
        elif(msg == "mapL"):
            self.cycleMapSingle(-1)
        elif(msg == "mapR"):
            self.cycleMapSingle(1)
        elif(msg == "tabs"):
            self.cycleTabs()
        elif(msg == "reset"):
            self.resetEvidence()
            
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
            table += "</tr>"
        html = table_html.replace("TABLECONTENTS", table)
        notes = self.phasmo.get_evidence_notes()
        html = html.replace("NOTES", notes)
        self.notesBrowser.setHtml(html)

    def updateSelectedEvidence(self):
        self.evidenceLabel1.setText(str(self.selectedEvidence[0]))
        self.evidenceLabel2.setText(str(self.selectedEvidence[1]))
        self.evidenceLabel3.setText(str(self.selectedEvidence[2]))
        self.phasmo.update_current_evidence(self.selectedEvidence)
        self.refresh_ghosts_table()
        self.refresh_notes()
    
    def updateSelectedMap(self):
        self.mapLabel.setText(str(self.selectedMap))
        self.mapBrowser.setHtml(map_data[self.selectedMap])
        
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

    def restart_server(self):
        self.host = settings.value("PhasmoCompanion/host", "127.0.0.1")
        self.port = int(settings.value("PhasmoCompanion/port", 39211))
        if(self.server.die()):
            self.server = UDPServer(self.host, self.port)
            self.server.signals.get.connect(self.udpRecv)
            self.server.signals.log.connect(self.log)
            self.server.start()

    def closeEvent(self, evt):
        self.server.die()
        self.settings.setValue("PhasmoCompanion/geometry", self.saveGeometry())
        self.settings.setValue("PhasmoCompanion/windowState", self.saveState())
        host = self.host_edit.text()
        port = int(self.port_edit.text())
        self.settings.setValue("PhasmoCompanion/host", host)
        self.settings.setValue("PhasmoCompanion/port", port)
        self.settings.sync()
        self.log("Closing PhasmoCompanion")

    def log(self, msg, level=LogLevel.INFO):
        if(not msg or level.value > self.log_level.value):
            return
        if(level == LogLevel.ERROR):
            style = "color: #cc0000;"
        elif(level == LogLevel.DEBUG):
            style = "color: #006600;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} {msg}</span>'
        self.log_edit.append(msg)


class UDPServer(QThread):

    #Class to handle HTTP Requests
    class Handler(socketserver.DatagramRequestHandler):
    
        #Handle GET requests
        def handle(self):
            msgRecvd = str(self.rfile.readline().strip().decode("utf-8"))
            self.server.signals.get.emit(msgRecvd)


    # Pass along the Signals
    class Signals(QObject):
        get = Signal(str)
        log = Signal(str, LogLevel)


    def __init__(self, host="127.0.0.1", port=35387):
        super().__init__()
        self.port = port
        self.host = host
        self.signals = self.Signals()
        self.server = socketserver.UDPServer((self.host, self.port), self.Handler)
        self.server.signals = self.signals

    def run(self):
        self.log(f"UDP Server Running  {self.host}:{self.port}")
        self.server.serve_forever()

    def die(self):
        self.log("UDP Server Shutdown")
        self.server.shutdown()
        return True

    def log(self, msg, level=LogLevel.INFO):
        self.signals.log.emit(msg, level)


if __name__ == "__main__":
    num_args = len(sys.argv)
    app = QApplication(sys.argv)
    version = "1"
    app_name = "PhasmoCompanion"
    app.setOrganizationName(app_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    QSettings.setDefaultFormat(QSettings.IniFormat)
    settings = QSettings()
    if(num_args<=1):
        window = PhasmoCompanion(settings)
        sys.exit(app.exec())
    else:
        host = settings.value("PhasmoCompanion/host", "127.0.0.1")
        port = int(settings.value("PhasmoCompanion/port", 39211))
        msg = sys.argv[1]
        bytesToSend = str.encode(msg)
        serverAddressPort = (host, port)
        print(f"Sending UDP {host}:{port} {msg}")
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)


