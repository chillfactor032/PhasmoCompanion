# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QLabel, QListView, QMainWindow, QPushButton,
    QSizePolicy, QTabWidget, QTextBrowser, QTextEdit,
    QWidget)

class Ui_PhasmoCompanion(object):
    def setupUi(self, PhasmoCompanion):
        if not PhasmoCompanion.objectName():
            PhasmoCompanion.setObjectName(u"PhasmoCompanion")
        PhasmoCompanion.resize(1200, 800)
        self.centralwidget = QWidget(PhasmoCompanion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(680, 10, 511, 781))
        self.evidenceLabel1 = QLabel(self.groupBox)
        self.evidenceLabel1.setObjectName(u"evidenceLabel1")
        self.evidenceLabel1.setGeometry(QRect(60, 70, 371, 41))
        font = QFont()
        font.setPointSize(20)
        self.evidenceLabel1.setFont(font)
        self.evidenceLabel1.setAlignment(Qt.AlignCenter)
        self.cycleEvidenceButtonL1 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonL1.setObjectName(u"cycleEvidenceButtonL1")
        self.cycleEvidenceButtonL1.setGeometry(QRect(20, 70, 31, 41))
        self.cycleEvidenceButtonL2 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonL2.setObjectName(u"cycleEvidenceButtonL2")
        self.cycleEvidenceButtonL2.setGeometry(QRect(20, 150, 31, 41))
        self.cycleEvidenceButtonL3 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonL3.setObjectName(u"cycleEvidenceButtonL3")
        self.cycleEvidenceButtonL3.setGeometry(QRect(20, 230, 31, 41))
        self.cycleEvidenceButtonR1 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonR1.setObjectName(u"cycleEvidenceButtonR1")
        self.cycleEvidenceButtonR1.setGeometry(QRect(450, 70, 31, 41))
        self.cycleEvidenceButtonR3 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonR3.setObjectName(u"cycleEvidenceButtonR3")
        self.cycleEvidenceButtonR3.setGeometry(QRect(450, 230, 31, 41))
        self.cycleEvidenceButtonR2 = QPushButton(self.groupBox)
        self.cycleEvidenceButtonR2.setObjectName(u"cycleEvidenceButtonR2")
        self.cycleEvidenceButtonR2.setGeometry(QRect(450, 150, 31, 41))
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 200, 491, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 280, 491, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 120, 491, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.groupBox)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 40, 491, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.evidenceLabel2 = QLabel(self.groupBox)
        self.evidenceLabel2.setObjectName(u"evidenceLabel2")
        self.evidenceLabel2.setGeometry(QRect(60, 150, 371, 41))
        self.evidenceLabel2.setFont(font)
        self.evidenceLabel2.setAlignment(Qt.AlignCenter)
        self.evidenceLabel3 = QLabel(self.groupBox)
        self.evidenceLabel3.setObjectName(u"evidenceLabel3")
        self.evidenceLabel3.setGeometry(QRect(60, 230, 371, 41))
        self.evidenceLabel3.setFont(font)
        self.evidenceLabel3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 320, 121, 16))
        self.resetEvidenceButton = QPushButton(self.groupBox)
        self.resetEvidenceButton.setObjectName(u"resetEvidenceButton")
        self.resetEvidenceButton.setGeometry(QRect(410, 310, 75, 24))
        self.ghost_listwidget = QListView(self.groupBox)
        self.ghost_listwidget.setObjectName(u"ghost_listwidget")
        self.ghost_listwidget.setGeometry(QRect(10, 350, 491, 421))
        font1 = QFont()
        font1.setPointSize(14)
        self.ghost_listwidget.setFont(font1)
        self.infoTabWidget = QTabWidget(self.centralwidget)
        self.infoTabWidget.setObjectName(u"infoTabWidget")
        self.infoTabWidget.setGeometry(QRect(10, 10, 661, 781))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoTabWidget.sizePolicy().hasHeightForWidth())
        self.infoTabWidget.setSizePolicy(sizePolicy)
        self.ghost_tab = QWidget()
        self.ghost_tab.setObjectName(u"ghost_tab")
        self.info_browser = QTextBrowser(self.ghost_tab)
        self.info_browser.setObjectName(u"info_browser")
        self.info_browser.setGeometry(QRect(5, 11, 641, 741))
        self.infoTabWidget.addTab(self.ghost_tab, "")
        self.settings_tab = QWidget()
        self.settings_tab.setObjectName(u"settings_tab")
        self.log_edit = QTextEdit(self.settings_tab)
        self.log_edit.setObjectName(u"log_edit")
        self.log_edit.setGeometry(QRect(10, 60, 631, 691))
        self.verbose_checkbox = QCheckBox(self.settings_tab)
        self.verbose_checkbox.setObjectName(u"verbose_checkbox")
        self.verbose_checkbox.setGeometry(QRect(395, 30, 241, 20))
        self.label_2 = QLabel(self.settings_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 49, 16))
        self.infoTabWidget.addTab(self.settings_tab, "")
        PhasmoCompanion.setCentralWidget(self.centralwidget)

        self.retranslateUi(PhasmoCompanion)

        self.infoTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PhasmoCompanion)
    # setupUi

    def retranslateUi(self, PhasmoCompanion):
        PhasmoCompanion.setWindowTitle(QCoreApplication.translate("PhasmoCompanion", u"PhasmoCompanion", None))
        self.groupBox.setTitle(QCoreApplication.translate("PhasmoCompanion", u"Evidence", None))
        self.evidenceLabel1.setText(QCoreApplication.translate("PhasmoCompanion", u"Evidence", None))
        self.cycleEvidenceButtonL1.setText(QCoreApplication.translate("PhasmoCompanion", u"<", None))
        self.cycleEvidenceButtonL2.setText(QCoreApplication.translate("PhasmoCompanion", u"<", None))
        self.cycleEvidenceButtonL3.setText(QCoreApplication.translate("PhasmoCompanion", u"<", None))
        self.cycleEvidenceButtonR1.setText(QCoreApplication.translate("PhasmoCompanion", u">", None))
        self.cycleEvidenceButtonR3.setText(QCoreApplication.translate("PhasmoCompanion", u">", None))
        self.cycleEvidenceButtonR2.setText(QCoreApplication.translate("PhasmoCompanion", u">", None))
        self.evidenceLabel2.setText(QCoreApplication.translate("PhasmoCompanion", u"Evidence", None))
        self.evidenceLabel3.setText(QCoreApplication.translate("PhasmoCompanion", u"Evidence", None))
        self.label.setText(QCoreApplication.translate("PhasmoCompanion", u"Possible Ghosts", None))
        self.resetEvidenceButton.setText(QCoreApplication.translate("PhasmoCompanion", u"Reset", None))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.ghost_tab), QCoreApplication.translate("PhasmoCompanion", u"Ghost Info", None))
        self.verbose_checkbox.setText(QCoreApplication.translate("PhasmoCompanion", u"Verbose Logs (requires relaunch)", None))
        self.label_2.setText(QCoreApplication.translate("PhasmoCompanion", u"Log", None))
        self.infoTabWidget.setTabText(self.infoTabWidget.indexOf(self.settings_tab), QCoreApplication.translate("PhasmoCompanion", u"Logs", None))
    # retranslateUi



