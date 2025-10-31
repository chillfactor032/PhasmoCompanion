# Python Imports
import sys
import datetime
import json
import keyboard
import requests
import os
import time
import copy
from enum import Enum, auto

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QDialog, QTableWidgetItem, QHeaderView, QListWidgetItem
from PySide6.QtCore import Qt, Signal, QObject, QThread, QSettings, QFile, QTextStream, QStandardPaths, QTimer
from PySide6.QtGui import QPixmap, QIcon, QMovie

# PhasmoCompanion Imports
from UI_Components import Ui_MainWindow, Ui_LoadingDialog, Ui_LogDialog, Ui_SettingsDialog
from chillmessenger import ChillMessenger
from overlayserver import OverlayServer
from PhasmoClasses import Evidence, ghosts_data

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
    CYCLE_EVIDENCE_1_RIGHT = 1
    CYCLE_EVIDENCE_2_RIGHT = 2
    CYCLE_EVIDENCE_3_RIGHT = 3
    CYCLE_EVIDENCE_1_LEFT = 4
    CYCLE_EVIDENCE_2_LEFT = 5
    CYCLE_EVIDENCE_3_LEFT = 6
    RESET = 7
    RULEOUT_EVIDENCE_1_LEFT = 8
    RULEOUT_EVIDENCE_1_RIGHT = 9
    RULEOUT_EVIDENCE_2_LEFT = 10
    RULEOUT_EVIDENCE_2_RIGHT = 11
    RULEOUT_EVIDENCE_3_LEFT = 12
    RULEOUT_EVIDENCE_3_RIGHT = 13
    RULEOUT_EVIDENCE_4_LEFT = 14
    RULEOUT_EVIDENCE_4_RIGHT = 15
    RULEOUT_EVIDENCE_5_LEFT = 16
    RULEOUT_EVIDENCE_5_RIGHT = 17


class PhasmoCompanion(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()

        #Load UI Components
        self.setupUi(self)
        self.log_dialog = LogDialog(self)

        #App Vars
        self.ghost_data_version = 0
        self.ghost_data = []
        self.evidence = []
        self.overlay_server = None

        #Ghost Data URL
        self.ghostdata_url = "https://chillaspect.com/api/phasmo/ghost_data_test.json"

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
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        self.overlay_dir = os.path.join(self.config_dir, "overlays").replace("\\", "/")
        if not os.path.isdir(self.config_dir):
            os.makedirs(self.config_dir)
        if not os.path.isdir(self.overlay_dir):
            os.makedirs(self.overlay_dir)
        self.ini_path = os.path.join(self.config_dir, "PhasmoCompanion.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)
        try:
            self.overlay_enabled = int(self.settings.value("PhasmoCompanion/overlay_enabled", "0")) == 1
        except ValueError:
            self.overlay_enabled = False
        self.ghost_data_file_path = os.path.join(self.config_dir, "ghost_data.json").replace("\\", "/")
        
        # Setup Loading Dialog Gifs
        loading_gif = QMovie(":resources/img/icon/loading.gif")
        check_gif = QMovie(":resources/img/icon/check.gif")
        x_gif = QMovie(":resources/img/icon/x.gif")

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        #Initialize the starting evidence
        self.selectedEvidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]

        #Initialize the ruled out evidence
        self.ruled_out_evidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        
        #Setup Button Signals
        self.evidence_button_left_1.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_1.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_2.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_2.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_3.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_3.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_4.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_4.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_5.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_5.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_6.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_6.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_7.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_7.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_left_8.clicked.connect(self.cycle_evidence_button_clicked)
        self.evidence_button_right_8.clicked.connect(self.cycle_evidence_button_clicked)
        self.reset_button.clicked.connect(self.reset_evidence)
        self.log_button.clicked.connect(self.show_log)
        self.evidence_label_1.setText(str(Evidence.NOEVIDENCE))
        self.evidence_label_2.setText(str(Evidence.NOEVIDENCE))
        self.evidence_label_3.setText(str(Evidence.NOEVIDENCE))
        self.settings_button.clicked.connect(self.show_settings)

        #Local KeyEvent Listener to Communicate with Stream Deck
        self.key_listener = KeyListener()
        self.key_listener.signals.key_event.connect(self.process_key_event)
        self.key_listener.signals.log.connect(self.log)
        self.key_listener.start()

        self.log(f"Config File Loaded: {self.config_dir}", LogLevel.DEBUG)
        self.log(f"Local Ghost Data File: {self.ghost_data_file_path}")
        self.log(f"Ghost Data URL: {self.ghostdata_url}", LogLevel.DEBUG)
        self.log(f"Overlay Directory: {self.overlay_dir}")

        # Set Possible Ghost Table Column Widths
        header = self.possible_ghost_table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Fixed)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        self.possible_ghost_table.setColumnWidth(0, 50)
        self.possible_ghost_table.setColumnWidth(1, 120)
        self.reset_evidence()

        #Build Phasmo Object with Ghost Data
        self.phasmo = None

        #Finally, Show the UI
        geometry = self.settings.value("PhasmoCompanion/geometry")
        window_state = self.settings.value("PhasmoCompanion/windowState")
        if geometry and window_state:
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()

        self.loading_dialog = LoadingDialog(self, loading_gif, check_gif, x_gif)
        QTimer.singleShot(2000, self.checkStart)

        self.chillmessenger = ChillMessenger()
        self.chillmessenger.signals.on_msg.connect(self.on_chillmessage)
        self.chillmessenger.start()

        if self.overlay_enabled:
            self.start_overlay_server()

        #Update Ghost Data
        self.evidence = list(Evidence)
        self.refresh_ghost_data()
    
    def send_overlay_data(self, data):
        if self.overlay_server is not None:
            self.overlay_server.send_event("update", {"data": data})

    def start_overlay_server(self):
        if self.overlay_server is None:
            self.overlay_server = OverlayServer(base_dir=self.overlay_dir)
            self.overlay_server.start()
            self.log("Overlay Server Started")
            self.log(self.overlay_server.get_url())

    def stop_overlay_server(self):
        if self.overlay_server is not None:
            self.loading_dialog.start("Stopping overlay server...", "Timeout")
            self.overlay_server.shutdown()
            self.overlay_server.join()
            self.overlay_server = None
            self.log("Overlay Server Stopped")
            self.loading_dialog.complete("Done")

    def update_possible_ghosts(self):
        possible_ghosts = []
        eliminated_ghosts = []
        eliminated_evidence = list(Evidence)
        eliminated_evidence.remove(Evidence.NOEVIDENCE)

        update_data = {
            "possible_ghosts": [],
            "selected_evidence": [],
            "eliminated_evidence": [],
            "ruled_out_evidence": []
        }

        # Selected Evidence
        for evidence in self.selectedEvidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            if evidence in eliminated_evidence:
                eliminated_evidence.remove(evidence)
            for ghost in ghosts_data:
                if evidence not in ghost["evidence"]:
                    eliminated_ghosts.append(ghost["name"])
        
        # Ruled Out Evidence
        for evidence in self.ruled_out_evidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            for ghost in ghosts_data:
                if evidence in ghost["evidence"]:
                    eliminated_ghosts.append(ghost["name"])

        for ghost in ghosts_data:
            if ghost["name"] not in eliminated_ghosts:
                possible_ghosts.append(ghost)
        
        # Gather Update Data
        if len(possible_ghosts) <= 5:
            for ghost in possible_ghosts:
                ghost_obj = {
                    "name": ghost["name"],
                    "evidence": [],
                    "hunt_threshold": ghost["hunt_threshold"]
                }
                for evidence in ghost["evidence"]:
                    if evidence not in self.selectedEvidence:
                        ghost_obj["evidence"].append(str(evidence))
                update_data["possible_ghosts"].append(ghost_obj)
        for evidence in eliminated_evidence:
            update_data["eliminated_evidence"].append(str(evidence))
        for evidence in self.selectedEvidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            update_data["selected_evidence"].append(str(evidence))
        for evidence in self.ruled_out_evidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            update_data["ruled_out_evidence"].append(str(evidence))
        self.send_overlay_data(update_data)
        
        #Update the UI
        while self.possible_ghost_table.rowCount() > 0:
            self.possible_ghost_table.removeRow(0)
        
        if len(possible_ghosts) > 5:
            return
        
        self.possible_ghost_table.setRowCount(len(possible_ghosts))
        for x in range(len(possible_ghosts)):
            name = QTableWidgetItem(possible_ghosts[x]["name"])
            possible_evidence = []
            for evidence in possible_ghosts[x]["evidence"]:
                if evidence not in self.selectedEvidence:
                    if evidence in eliminated_evidence:
                        eliminated_evidence.remove(evidence)
                    possible_evidence.append(str(evidence))
            evidence_item = QTableWidgetItem(", ".join(possible_evidence))
            hunt_item = QTableWidgetItem(possible_ghosts[x]["hunt_threshold"])
            self.possible_ghost_table.setItem(x, 0, hunt_item)
            self.possible_ghost_table.setItem(x, 1, name)
            self.possible_ghost_table.setItem(x, 2, evidence_item)
        
        self.eliminated_evidence_list.clear()
        for evidence in eliminated_evidence:
            self.eliminated_evidence_list.addItem(QListWidgetItem(str(evidence)))
            
    def show_settings(self):
        url = ""
        if self.overlay_server is not None:
            url = self.overlay_server.get_url()
        settings_dialog = SettingsDialog(self, self.overlay_dir, self.overlay_enabled, url)
        result = settings_dialog.exec()
        if result == QDialog.Accepted:
            print("Accepted")
            self.overlay_enabled = settings_dialog.enable_overlays
            if self.overlay_enabled:
                self.settings.setValue("PhasmoCompanion/overlay_enabled", "1")
                self.start_overlay_server()
            else:
                self.settings.setValue("PhasmoCompanion/overlay_enabled", "0")
                self.stop_overlay_server()

    def show_log(self):
        self.log_dialog.setVisible(not self.log_dialog.isVisible())

    def checkStart(self):
        start = time.time()
        keylistener_started = False
        chillmessenger_started = False
        #Check KeyListener and ChillMessenger Started
        while time.time() - start < 3:
            if self.key_listener and self.key_listener.started:
                keylistener_started = True
                self.log("KeyListener Started")
            if self.chillmessenger and self.chillmessenger.running():
                chillmessenger_started = True
                self.log("ChillMessenger Server Started")
            if keylistener_started and chillmessenger_started:
                break
        if not keylistener_started:
            self.log("KeyEventListener did not start! (5 sec timeout)", LogLevel.ERROR)
        if not chillmessenger_started:
            self.log("ChillMessenger Server did not start! (5 sec timeout)", LogLevel.ERROR)

    def process_key_event(self, event=KeyEvent.RESET):
        self.log(f"Key Event: {event}", LogLevel.DEBUG)
        if event == KeyEvent.CYCLE_EVIDENCE_1_LEFT:
            self.cycle_evidence(0, -1)
        if event == KeyEvent.CYCLE_EVIDENCE_1_RIGHT:
            self.cycle_evidence(0, 1)
        if event == KeyEvent.CYCLE_EVIDENCE_2_LEFT:
            self.cycle_evidence(1, -1)
        if event == KeyEvent.CYCLE_EVIDENCE_2_RIGHT:
            self.cycle_evidence(1, 1)
        if event == KeyEvent.CYCLE_EVIDENCE_3_LEFT:
            self.cycle_evidence(2, -1)
        if event == KeyEvent.CYCLE_EVIDENCE_3_RIGHT:
            self.cycle_evidence(2, 1)
        if event == KeyEvent.RESET:
            self.reset_evidence()
        if event == KeyEvent.RULEOUT_EVIDENCE_1_LEFT:
            self.cycle_ruled_out_evidence(0, -1)
        if event == KeyEvent.RULEOUT_EVIDENCE_1_RIGHT:
            self.cycle_ruled_out_evidence(0, 1)
        if event == KeyEvent.RULEOUT_EVIDENCE_2_LEFT:
            self.cycle_ruled_out_evidence(1, -1)
        if event == KeyEvent.RULEOUT_EVIDENCE_2_RIGHT:
            self.cycle_ruled_out_evidence(1, 1)
        if event == KeyEvent.RULEOUT_EVIDENCE_3_LEFT:
            self.cycle_ruled_out_evidence(2, -1)
        if event == KeyEvent.RULEOUT_EVIDENCE_3_RIGHT:
            self.cycle_ruled_out_evidence(2, 1)
        if event == KeyEvent.RULEOUT_EVIDENCE_4_LEFT:
            self.cycle_ruled_out_evidence(3, -1)
        if event == KeyEvent.RULEOUT_EVIDENCE_4_RIGHT:
            self.cycle_ruled_out_evidence(3, 1)
        if event == KeyEvent.RULEOUT_EVIDENCE_5_LEFT:
            self.cycle_ruled_out_evidence(4, -1)
        if event == KeyEvent.RULEOUT_EVIDENCE_5_RIGHT:
            self.cycle_ruled_out_evidence(4, 1)
        self.update_possible_ghosts()

    def refresh_ghost_data(self):
        self.log("Refreshing Ghost Data")
        local_ghost_data = self.read_ghost_data_file()
        remote_ghost_data = self.fetch_remote_ghost_data()

        if remote_ghost_data is None:
            self.log("Could not fetch remote ghost data. Must rely on local ghost data.", LogLevel.ERROR)

        
        if local_ghost_data is None and remote_ghost_data is None:
            # Both remote and local data not available
            pass
        elif local_ghost_data is None and remote_ghost_data is not None:
            # Local data not available but remote is available
            pass
        else:
            # Either local data is available and remote
            pass
        
        """
        if (local_ghost_data is not None and remote_ghost_data is None) or (remote_ghost_data["version"] > local_ghost_data["version"]):
            self.log("New Ghost Data Available. Updating Local Ghost File.")
            self.ghost_data = remote_ghost_data["ghost_data"]
            self.ghost_data_version = remote_ghost_data["version"]
            self.evidence = remote_ghost_data["evidence"]
            try:
                with open(self.ghost_data_file_path, "w") as ghost_file:
                    json.dump(self.ghost_data, ghost_file, indent=2)
            except Exception as e:
                self.log(repr(e), LogLevel.ERROR)

        """
        # Both remote and local data cannot be found
        if remote_ghost_data is None and local_ghost_data is None:
            self.log("No local ghost data or remote ghost data! Resorting to default ghost data.", LogLevel.INFO)
            default_ghost_file = QFile(":version.json")
            default_ghost_file.open(QFile.ReadOnly)
            text_stream = QTextStream(default_ghost_file)
            default_ghost_file_text = text_stream.readAll()
            data = json.loads(default_ghost_file_text)
            self.version = data["version"]
            self.ghost_data = data["ghost_data"]
            self.evidence = data["evidence"]
            return
        
        """
        # If remote ghost file is newer, update
        if remote_ghost_data["version"] > local_ghost_data["version"]:
            self.log("New Ghost Data Available. Updating Local Ghost File.")
            self.ghost_data = remote_ghost_data["ghost_data"]
            self.ghost_data_version = remote_ghost_data["version"]
            self.evidence = remote_ghost_data["evidence"]
            try:
                with open(self.ghost_data_file_path, "w") as ghost_file:
                    json.dump(self.ghost_data, ghost_file, indent=2)
            except Exception as e:
                self.log(repr(e), LogLevel.ERROR)
        else:
            self.log("Local ghost data is latest version")
            self.ghost_data = local_ghost_data["ghost_data"]
            self.ghost_data_version = local_ghost_data["version"]
            self.evidence = local_ghost_data["evidence"]
        """
        n = len(self.ghost_data)
        self.log(f"Ghost data version: {self.ghost_data_version}")
        self.log(f"Loaded {n} Ghosts")

    def on_chillmessage(self, msg:int):
        print(f"RECV: {msg}")
        evt = None
        try:
            evt = KeyEvent(msg)
        except ValueError:
            self.log(f"Unknown Message From ChillMessenger: {msg}", LogLevel.ERROR)
            return
        self.process_key_event(evt)
        
    def read_ghost_data_file(self):
        self.log("Reading local ghost data file")

        if not os.path.exists(self.ghost_data_file_path): 
            self.log("Local ghost file is not found", LogLevel.ERROR)
            return None

        ghost_json = None
        with open(self.ghost_data_file_path, "r") as ghost_file:
            ghost_json = json.load(ghost_file)
            
        if ghost_json is not None:
            return ghost_json
        return None
        
    def fetch_remote_ghost_data(self):
        self.log("Reading remote ghost data file")
        self.loading_dialog.start("Retrieving Ghost Data...", "Timeout Fetching Ghost Data")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
        }
        data = None
        try:
            r = requests.get(self.ghostdata_url, headers=headers, timeout=5)
            if r.status_code >= 200 and r.status_code < 300:
                data = r.json()
                self.loading_dialog.complete("Ghost Data Loaded - Success!")
                return data
            else:
                self.log(f"Error HTTP Status Code: {r.status_code}", LogLevel.ERROR)
        except Exception as e:
            self.log(repr(e), LogLevel.ERROR)
        self.log("Remote ghost data could not be fetched.", LogLevel.ERROR)
        self.loading_dialog.error("Error Retrieving Ghost Data")
        return data

    def refresh_ruled_out_evidence_labels(self):
        self.evidence_label_4.setText(str(self.ruled_out_evidence[0]))
        self.evidence_label_5.setText(str(self.ruled_out_evidence[1]))
        self.evidence_label_6.setText(str(self.ruled_out_evidence[2]))
        self.evidence_label_7.setText(str(self.ruled_out_evidence[3]))
        self.evidence_label_8.setText(str(self.ruled_out_evidence[4]))
    
    def refresh_evidence_labels(self):
        self.evidence_label_1.setText(str(self.selectedEvidence[0]))
        self.evidence_label_2.setText(str(self.selectedEvidence[1]))
        self.evidence_label_3.setText(str(self.selectedEvidence[2]))

    def cycle_evidence_button_clicked(self, src):
        src = self.sender()
        if src == self.evidence_button_left_1:
            self.cycle_evidence(0, -1)
        if src == self.evidence_button_right_1:
            self.cycle_evidence(0, 1)
        if src == self.evidence_button_left_2:
            self.cycle_evidence(1, -1)
        if src == self.evidence_button_right_2:
            self.cycle_evidence(1, 1)
        if src == self.evidence_button_left_3:
            self.cycle_evidence(2, -1)
        if src == self.evidence_button_right_3:
            self.cycle_evidence(2, 1)
        if src == self.evidence_button_left_4:
            self.cycle_ruled_out_evidence(0, -1)
        if src == self.evidence_button_right_4:
            self.cycle_ruled_out_evidence(0, 1)
        if src == self.evidence_button_left_5:
            self.cycle_ruled_out_evidence(1, -1)
        if src == self.evidence_button_right_5:
            self.cycle_ruled_out_evidence(1, 1)
        if src == self.evidence_button_left_6:
            self.cycle_ruled_out_evidence(2, -1)
        if src == self.evidence_button_right_6:
            self.cycle_ruled_out_evidence(2, 1)
        if src == self.evidence_button_left_7:
            self.cycle_ruled_out_evidence(3, -1)
        if src == self.evidence_button_right_7:
            self.cycle_ruled_out_evidence(3, 1)
        if src == self.evidence_button_left_8:
            self.cycle_ruled_out_evidence(4, -1)
        if src == self.evidence_button_right_8:
            self.cycle_ruled_out_evidence(4, 1)
        self.update_possible_ghosts()

    def cycle_ruled_out_evidence(self, evidence=0, step=1):
        next_val = self.ruled_out_evidence[evidence].value+step
        if next_val < 0:
            next_val = len(self.evidence)-1
        if next_val >= len(self.evidence):
            next_val = 0
        self.ruled_out_evidence[evidence] = Evidence(next_val)
        self.refresh_ruled_out_evidence_labels()

    def cycle_evidence(self, evidence=0, step=1):
        next_val = self.selectedEvidence[evidence].value+step
        if next_val < 0:
            next_val = len(self.evidence)-1
        if next_val >= len(self.evidence):
            next_val = 0
        self.selectedEvidence[evidence] = Evidence(next_val)
        self.refresh_evidence_labels()
        
    def reset_evidence(self):
        #Reset Evidence
        self.selectedEvidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.ruled_out_evidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.refresh_ruled_out_evidence_labels()
        self.refresh_evidence_labels()
        self.update_possible_ghosts()
        self.eliminated_evidence_list.clear()

    def closeEvent(self, evt):
        self.stop_overlay_server()
        self.chillmessenger.stop()
        self.chillmessenger.join()
        self.key_listener.die()
        self.settings.setValue("PhasmoCompanion/geometry", self.saveGeometry())
        self.settings.setValue("PhasmoCompanion/windowState", self.saveState())
        if self.overlay_enabled:
            self.settings.setValue("PhasmoCompanion/overlay_enabled", "1")
        else:
            self.settings.setValue("PhasmoCompanion/overlay_enabled", "0")
        self.settings.sync()
        self.log("Closing PhasmoCompanion")

    def log(self, msg, level=LogLevel.INFO):
        self.log_dialog.log(msg, level)

class LogDialog(QDialog):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog)
        self.ui = Ui_LogDialog()
        self.ui.setupUi(self)
    
    def log(self, msg, level=LogLevel.INFO):
        if not msg:
            return
        if level == LogLevel.ERROR:
            style = "color: #cc0000;"
        elif level == LogLevel.DEBUG:  
            style = "color: #006600;"
        elif level == LogLevel.INFO:
            style = "color: #000000;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
        print(msg)
        self.ui.log_browser.append(msg)

class SettingsDialog(QDialog):
    
    def __init__(self, parent, overlay_dir, enable_overlays, url):
        super().__init__(parent)
        self.setWindowFlags(Qt.Dialog)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.ui.browser_source_url_edit.setText(url)
        self.ui.overlay_dir_edit.setText(overlay_dir)
        self.overlay_dir = overlay_dir
        self.ui.save_button.clicked.connect(self.save_settings)
        self.ui.open_overlay_dir_button.clicked.connect(self.open_overlay_dir)
        self.enable_overlays = enable_overlays
        self.ui.enable_overlay_checkbox.setChecked(self.enable_overlays)
        self.ui.enable_overlay_checkbox.toggled.connect(self.overlay_checkbox_toggled)
    
    def open_overlay_dir(self):
        os.startfile(self.overlay_dir)

    def overlay_checkbox_toggled(self):
        self.enable_overlays = self.ui.enable_overlay_checkbox.isChecked()

    def save_settings(self):
        self.accept()


class LoadingDialog(QDialog):

    class Signals(QObject):
        log = Signal(str, LogLevel)
    
    def __init__(self, parent, loading_gif, check_gif, x_gif):
        super().__init__(parent)
        self.loading_gif = loading_gif
        self.check_gif = check_gif
        self.x_gif = x_gif
        self.signals = self.Signals()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.ui = Ui_LoadingDialog()
        self.ui.setupUi(self)
        self.timeout_timer = None

    def start(self, msg="Please wait...", timeout_msg="Timeout Error", timeout_secs=10):
        self.ui.gif_label.setMovie(self.loading_gif)
        self.loading_gif.start()
        self.ui.status_label.setText(msg)
        self.timeout_timer = QTimer(self)
        self.timeout_timer.setSingleShot(True)
        self.timeout_timer.setInterval(timeout_secs*1000)
        self.timeout_timer.timeout.connect(lambda : self.error(timeout_msg))
        self.timeout_timer.start()
        self.show()
        
    def set_status_msg(self, msg=""):
        self.ui.status_label.setText(msg)

    def error(self, msg=""):
        self.ui.status_label.setText(msg)
        self.ui.gif_label.setMovie(self.x_gif)
        self.x_gif.start()
        if self.timeout_timer is not None and self.timeout_timer.isActive():
            self.timeout_timer.stop()
        QTimer.singleShot(1500, self.hide)

    def complete(self, msg=""):
        self.ui.status_label.setText(msg)
        self.ui.gif_label.setMovie(self.check_gif)
        self.check_gif.start()
        if self.timeout_timer is not None and self.timeout_timer.isActive():
            self.timeout_timer.stop()
        QTimer.singleShot(1500, self.hide)

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
        keyboard.add_hotkey('ctrl+shift+1', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_1_RIGHT))
        keyboard.add_hotkey('ctrl+shift+2', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_2_RIGHT))
        keyboard.add_hotkey('ctrl+shift+3', lambda: self.signals.key_event.emit(KeyEvent.CYCLE_EVIDENCE_3_RIGHT))
        keyboard.add_hotkey('ctrl+shift+4', lambda: self.signals.key_event.emit(KeyEvent.RESET))
        self.started = True
        self.log("KeyEvent Listener Started")

    def die(self):
        # In case KeyListener needs a Deconstructor
        self.log("KeyEvent Listener Stopped")

    def log(self, msg, level=LogLevel.INFO):
        self.signals.log.emit(msg, level)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    version = "3"
    org_name = "ChillAspect"
    app_name = "PhasmoCompanion"
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = PhasmoCompanion()
    sys.exit(app.exec())
