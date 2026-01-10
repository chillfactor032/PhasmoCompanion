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
from PySide6.QtCore import Qt, Signal, QObject, QThread, QSettings, QFile, QTextStream, QStandardPaths, QTimer, QResource
from PySide6.QtGui import QPixmap, QIcon, QMovie, QDesktopServices

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
    RESET_RULEOUT_EVIDENCE = 18


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
        self.help_url = "https://github.com/chillfactor032/PhasmoCompanion/blob/main/README.md"

        #Read Version File From Resources
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        print(self.version)
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
        
        #Copy overlay files from resources
        overlay_files = QResource(":overlays")
        for file in overlay_files.children():
            overlay_file_path = os.path.join(self.overlay_dir, file)
            if os.path.exists(overlay_file_path):
                continue
            file_obj = QFile(f":overlays/{file}")
            file_obj.open(QFile.ReadOnly)
            file_text = QTextStream(file_obj).readAll()
            with open(overlay_file_path, "w") as f:
                f.write(file_text)
            self.log(f"Created overlay file: overlays/{file}")

        # Setup Loading Dialog Gifs
        self.loading_gif = QMovie(":resources/img/icon/loading.gif")
        self.check_gif = QMovie(":resources/img/icon/check.gif")
        self.x_gif = QMovie(":resources/img/icon/x.gif")

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        pc_icon_pixmap = QPixmap(":resources/img/pc_icon.ico")
        pc_icon = QIcon(pc_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(pc_icon):
            self.setWindowIcon(pc_icon)
        else:
            self.setWindowIcon(default_icon)

        # List of all evidence (enum)
        self.evidence = list(Evidence)

        #Initialize the starting evidence
        self.selected_evidence = [
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
        self.help_button.clicked.connect(self.help_button_clicked)
        self.reset_ruled_out_button.clicked.connect(self.reset_ruled_out_button_clicked)

        #Local KeyEvent Listener to Communicate with Stream Deck
        self.key_listener = KeyListener()
        self.key_listener.signals.key_event.connect(self.process_key_event)
        self.key_listener.signals.log.connect(self.log)
        self.key_listener.start()

        self.log(f"Config File Loaded: {self.config_dir}", LogLevel.DEBUG)
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

        self.loading_dialog = LoadingDialog(self, self.loading_gif, self.check_gif, self.x_gif)
        self.loading_dialog.start("Starting Services", "Timeout...")

        QTimer.singleShot(2000, self.checkStart)

        self.chillmessenger = ChillMessenger()
        self.chillmessenger.signals.on_msg.connect(self.on_chillmessage)
        self.chillmessenger.start()

        if self.overlay_enabled:
            self.start_overlay_server()   
    
    def send_overlay_data(self, data):
        if self.overlay_server is not None:
            self.overlay_server.send_event("update", data)

    def start_overlay_server(self):
        if self.overlay_server is None:
            self.overlay_server = OverlayServer(base_dir=self.overlay_dir)
            self.overlay_server.start()
            self.log(f"Overlay Server Started {self.overlay_server.get_url()}")

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
        for evidence in self.selected_evidence:
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
        
        """
        for ghost in possible_ghosts:
            for evidence in ghost["evidence"]:
                if evidence not in self.selected_evidence:
                    eliminated_evidence.remove(evidence)
        """

        # Gather Update Data
        if len(possible_ghosts) <= 5:
            for ghost in possible_ghosts:
                ghost_obj = {
                    "name": ghost["name"],
                    "evidence": [],
                    "hunt_threshold": ghost["hunt_threshold"]
                }
                for evidence in ghost["evidence"]:
                    if evidence not in self.selected_evidence:
                        ghost_obj["evidence"].append(str(evidence))
                update_data["possible_ghosts"].append(ghost_obj)
        
        for evidence in self.selected_evidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            update_data["selected_evidence"].append(str(evidence))
        for evidence in self.ruled_out_evidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            update_data["ruled_out_evidence"].append(str(evidence))
        
        #Update the UI
        while self.possible_ghost_table.rowCount() > 0:
            self.possible_ghost_table.removeRow(0)
        
        self.possible_ghost_table.setRowCount(len(possible_ghosts))
        for x in range(len(possible_ghosts)):
            name = QTableWidgetItem(possible_ghosts[x]["name"])
            possible_evidence = []
            for evidence in possible_ghosts[x]["evidence"]:
                if evidence not in self.selected_evidence:
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

        #Update overlay update eliminated evidence
        for evidence in eliminated_evidence:
            if evidence == Evidence.NOEVIDENCE:
                continue
            update_data["eliminated_evidence"].append(str(evidence))
        self.send_overlay_data(update_data)

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

    def help_button_clicked(self):
        QDesktopServices.openUrl(self.help_url)

    def checkStart(self):
        start = time.time()
        keylistener_started = False
        chillmessenger_started = False
        overlayserver_started = False
        msgs = []
        #Check KeyListener and ChillMessenger Started
        while time.time() - start < 5:
            if self.key_listener and self.key_listener.started:
                keylistener_started = True
                msgs.append("KeyListener Started")
            if self.chillmessenger and self.chillmessenger.running():
                chillmessenger_started = True
                msgs.append("ChillMessenger Server Started")
            if self.overlay_enabled and self.overlay_server is not None:
                overlayserver_started = True
                msgs.append("OverlayServer Started")
            if keylistener_started and chillmessenger_started and overlayserver_started:
                for msg in msgs:
                    self.log(msg)
                break
        if not keylistener_started:
            self.log("KeyEventListener did not start! (5 sec timeout)", LogLevel.ERROR)
            self.loading_dialog.error("KeyListener Start Failed!")
        if not chillmessenger_started:
            self.log("ChillMessenger Server did not start! (5 sec timeout)", LogLevel.ERROR)
            self.loading_dialog.error("ChillMessenger Start Failed!")
        if not overlayserver_started:
            self.log("Overlay Server did not start! (5 sec timeout)", LogLevel.ERROR)
            self.loading_dialog.error("OverlayServer Start Failed!")
        self.loading_dialog.complete("Done!")

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

    def on_chillmessage(self, msg:int):
        print(f"RECV: {msg}")
        evt = None
        try:
            evt = KeyEvent(msg)
        except ValueError:
            self.log(f"Unknown Message From ChillMessenger: {msg}", LogLevel.ERROR)
            return
        self.process_key_event(evt)

    def refresh_ruled_out_evidence_labels(self):
        self.evidence_label_4.setText(str(self.ruled_out_evidence[0]))
        self.evidence_label_5.setText(str(self.ruled_out_evidence[1]))
        self.evidence_label_6.setText(str(self.ruled_out_evidence[2]))
        self.evidence_label_7.setText(str(self.ruled_out_evidence[3]))
        self.evidence_label_8.setText(str(self.ruled_out_evidence[4]))
    
    def refresh_evidence_labels(self):
        self.evidence_label_1.setText(str(self.selected_evidence[0]))
        self.evidence_label_2.setText(str(self.selected_evidence[1]))
        self.evidence_label_3.setText(str(self.selected_evidence[2]))

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
        next_val = self.selected_evidence[evidence].value+step
        if next_val < 0:
            next_val = len(self.evidence)-1
        if next_val >= len(self.evidence):
            next_val = 0
        self.selected_evidence[evidence] = Evidence(next_val)
        self.refresh_evidence_labels()
    
    def reset_ruled_out_button_clicked(self):
        self.ruled_out_evidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.refresh_ruled_out_evidence_labels()
        self.update_possible_ghosts()

    def reset_evidence(self):
        # Reset Ruled Out Evidence
        self.ruled_out_evidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]

        #Reset Evidence
        self.selected_evidence = [
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE,
            Evidence.NOEVIDENCE
        ]
        self.refresh_ruled_out_evidence_labels()
        self.refresh_evidence_labels()
        self.update_possible_ghosts()
        self.eliminated_evidence_list.clear()

    def closeEvent(self, evt):
        QApplication.setOverrideCursor(Qt.WaitCursor)
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
        QApplication.setOverrideCursor(Qt.ArrowCursor)
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
            style = "color: #ffffff;"
        else:
            style = "color: #000000;"
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        print(f'{level.name} - {timestamp} - {msg}')
        msg = f'<span style="{style}">{timestamp} - {msg}</span>'
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
