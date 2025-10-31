# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoadingDialog(object):
    def setupUi(self, LoadingDialog):
        if not LoadingDialog.objectName():
            LoadingDialog.setObjectName(u"LoadingDialog")
        LoadingDialog.resize(218, 250)
        LoadingDialog.setStyleSheet(u"#LoadingDialog {\n"
"	border: 5px outset grey;\n"
"	border-radius: 10px;\n"
"	background-color: #31363b;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(LoadingDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(LoadingDialog)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(200, 200))
        self.widget.setMaximumSize(QSize(200, 200))
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gif_label = QLabel(self.widget)
        self.gif_label.setObjectName(u"gif_label")
        self.gif_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.gif_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(LoadingDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(200, 30))
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.status_label = QLabel(self.widget_2)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.status_label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(LoadingDialog)

        QMetaObject.connectSlotsByName(LoadingDialog)
    # setupUi

    def retranslateUi(self, LoadingDialog):
        LoadingDialog.setWindowTitle(QCoreApplication.translate("LoadingDialog", u"Dialog", None))
        self.gif_label.setText("")
        self.status_label.setText("")
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_LogDialog(object):
    def setupUi(self, LogDialog):
        if not LogDialog.objectName():
            LogDialog.setObjectName(u"LogDialog")
        LogDialog.resize(579, 445)
        LogDialog.setStyleSheet(u"#LogDialog {\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"	background-color: #2c313c;\n"
"	color: #b0b8b6;\n"
"}")
        self.gridLayout = QGridLayout(LogDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.log_browser = QTextBrowser(LogDialog)
        self.log_browser.setObjectName(u"log_browser")

        self.gridLayout.addWidget(self.log_browser, 0, 0, 1, 1)


        self.retranslateUi(LogDialog)

        QMetaObject.connectSlotsByName(LogDialog)
    # setupUi

    def retranslateUi(self, LogDialog):
        LogDialog.setWindowTitle(QCoreApplication.translate("LogDialog", u"Log Viewer", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PhasmoCompanionGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import PhasmoCompanion_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(824, 549)
        MainWindow.setStyleSheet(u"/*\n"
"Dark: #16191d\n"
"Accent_1: #1f2322\n"
"Accent_2: #2c313c\n"
"Accent_3: #343b47\n"
"Text_1: #fff\n"
"Text_2: #838ea2\n"
"\n"
"DarkCyan\n"
"<color name=\"primaryColor\">#4dd0e1</color>\n"
" <color name=\"primaryLightColor\">#88ffff</color>\n"
" <color name=\"secondaryColor\">#232629</color>\n"
"  <color name=\"secondaryLightColor\">#4f5b62</color>\n"
"  <color name=\"secondaryDarkColor\">#31363b</color>\n"
"  <color name=\"primaryTextColor\">#000000</color>\n"
"  <color name=\"secondaryTextColor\">#ffffff</color>\n"
"*/\n"
"\n"
"QMainWindow {\n"
"	\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #4dd0e1;\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color: #232629;\n"
"	color: #88ffff;\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: #232629;\n"
"	color: #4dd0e1;\n"
"	gridline-color: #9ea6ae;\n"
"}\n"
"\n"
"\n"
"QLabel:disabled {\n"
"	background-color: #ced6d4;\n"
"	color: #b0b8b6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: #fff;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #fff;\n"
"}\n"
"\n"
"\n"
"#centralwidget {\n"
"	b"
                        "ackground-color: #31363b;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QTextBrowser {\n"
"	background-color: #16191d;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 7px;\n"
"	top: -10ox;\n"
"    padding: 0px 5px 0px 5px;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid silver;\n"
"    border-radius: 6px;\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"color:  #9ea6ae;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QSize(400, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.widget_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.groupBox_4)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_4 = QToolButton(self.widget_5)
        self.evidence_button_left_4.setObjectName(u"evidence_button_left_4")
        self.evidence_button_left_4.setMinimumSize(QSize(40, 40))
        icon = QIcon()
        icon.addFile(u":/resources/img/icon/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.evidence_button_left_4.setIcon(icon)
        self.evidence_button_left_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.evidence_button_left_4)

        self.evidence_label_4 = QLabel(self.widget_5)
        self.evidence_label_4.setObjectName(u"evidence_label_4")
        font = QFont()
        font.setPointSize(22)
        self.evidence_label_4.setFont(font)
        self.evidence_label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.evidence_label_4)

        self.evidence_button_right_4 = QToolButton(self.widget_5)
        self.evidence_button_right_4.setObjectName(u"evidence_button_right_4")
        self.evidence_button_right_4.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/resources/img/icon/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.evidence_button_right_4.setIcon(icon1)
        self.evidence_button_right_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.evidence_button_right_4)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.groupBox_4)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_5 = QToolButton(self.widget_7)
        self.evidence_button_left_5.setObjectName(u"evidence_button_left_5")
        self.evidence_button_left_5.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_5.setIcon(icon)
        self.evidence_button_left_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.evidence_button_left_5)

        self.evidence_label_5 = QLabel(self.widget_7)
        self.evidence_label_5.setObjectName(u"evidence_label_5")
        self.evidence_label_5.setFont(font)
        self.evidence_label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.evidence_label_5)

        self.evidence_button_right_5 = QToolButton(self.widget_7)
        self.evidence_button_right_5.setObjectName(u"evidence_button_right_5")
        self.evidence_button_right_5.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_5.setIcon(icon1)
        self.evidence_button_right_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.evidence_button_right_5)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.groupBox_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_6 = QToolButton(self.widget_8)
        self.evidence_button_left_6.setObjectName(u"evidence_button_left_6")
        self.evidence_button_left_6.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_6.setIcon(icon)
        self.evidence_button_left_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.evidence_button_left_6)

        self.evidence_label_6 = QLabel(self.widget_8)
        self.evidence_label_6.setObjectName(u"evidence_label_6")
        self.evidence_label_6.setFont(font)
        self.evidence_label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.evidence_label_6)

        self.evidence_button_right_6 = QToolButton(self.widget_8)
        self.evidence_button_right_6.setObjectName(u"evidence_button_right_6")
        self.evidence_button_right_6.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_6.setIcon(icon1)
        self.evidence_button_right_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.evidence_button_right_6)


        self.verticalLayout_4.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.groupBox_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_7 = QToolButton(self.widget_9)
        self.evidence_button_left_7.setObjectName(u"evidence_button_left_7")
        self.evidence_button_left_7.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_7.setIcon(icon)
        self.evidence_button_left_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.evidence_button_left_7)

        self.evidence_label_7 = QLabel(self.widget_9)
        self.evidence_label_7.setObjectName(u"evidence_label_7")
        self.evidence_label_7.setFont(font)
        self.evidence_label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.evidence_label_7)

        self.evidence_button_right_7 = QToolButton(self.widget_9)
        self.evidence_button_right_7.setObjectName(u"evidence_button_right_7")
        self.evidence_button_right_7.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_7.setIcon(icon1)
        self.evidence_button_right_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.evidence_button_right_7)


        self.verticalLayout_4.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.groupBox_4)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 52))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_8 = QToolButton(self.widget_10)
        self.evidence_button_left_8.setObjectName(u"evidence_button_left_8")
        self.evidence_button_left_8.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_8.setIcon(icon)
        self.evidence_button_left_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.evidence_button_left_8)

        self.evidence_label_8 = QLabel(self.widget_10)
        self.evidence_label_8.setObjectName(u"evidence_label_8")
        self.evidence_label_8.setFont(font)
        self.evidence_label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.evidence_label_8)

        self.evidence_button_right_8 = QToolButton(self.widget_10)
        self.evidence_button_right_8.setObjectName(u"evidence_button_right_8")
        self.evidence_button_right_8.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_8.setIcon(icon1)
        self.evidence_button_right_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.evidence_button_right_8)


        self.verticalLayout_4.addWidget(self.widget_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.widget_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 200))
        self.gridLayout = QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 12, -1, -1)
        self.eliminated_evidence_list = QListWidget(self.groupBox_5)
        self.eliminated_evidence_list.setObjectName(u"eliminated_evidence_list")

        self.gridLayout.addWidget(self.eliminated_evidence_list, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_5)


        self.horizontalLayout_4.addWidget(self.widget_6)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(400, 0))
        self.widget_4.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.widget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(400, 200))
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 52))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_1 = QToolButton(self.widget)
        self.evidence_button_left_1.setObjectName(u"evidence_button_left_1")
        self.evidence_button_left_1.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_1.setIcon(icon)
        self.evidence_button_left_1.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.evidence_button_left_1)

        self.evidence_label_1 = QLabel(self.widget)
        self.evidence_label_1.setObjectName(u"evidence_label_1")
        self.evidence_label_1.setFont(font)
        self.evidence_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.evidence_label_1)

        self.evidence_button_right_1 = QToolButton(self.widget)
        self.evidence_button_right_1.setObjectName(u"evidence_button_right_1")
        self.evidence_button_right_1.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_1.setIcon(icon1)
        self.evidence_button_right_1.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.evidence_button_right_1)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_2 = QToolButton(self.widget_2)
        self.evidence_button_left_2.setObjectName(u"evidence_button_left_2")
        self.evidence_button_left_2.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_2.setIcon(icon)
        self.evidence_button_left_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.evidence_button_left_2)

        self.evidence_label_2 = QLabel(self.widget_2)
        self.evidence_label_2.setObjectName(u"evidence_label_2")
        self.evidence_label_2.setFont(font)
        self.evidence_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.evidence_label_2)

        self.evidence_button_right_2 = QToolButton(self.widget_2)
        self.evidence_button_right_2.setObjectName(u"evidence_button_right_2")
        self.evidence_button_right_2.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_2.setIcon(icon1)
        self.evidence_button_right_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.evidence_button_right_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.groupBox)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.evidence_button_left_3 = QToolButton(self.widget_3)
        self.evidence_button_left_3.setObjectName(u"evidence_button_left_3")
        self.evidence_button_left_3.setMinimumSize(QSize(40, 40))
        self.evidence_button_left_3.setIcon(icon)
        self.evidence_button_left_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.evidence_button_left_3)

        self.evidence_label_3 = QLabel(self.widget_3)
        self.evidence_label_3.setObjectName(u"evidence_label_3")
        self.evidence_label_3.setFont(font)
        self.evidence_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.evidence_label_3)

        self.evidence_button_right_3 = QToolButton(self.widget_3)
        self.evidence_button_right_3.setObjectName(u"evidence_button_right_3")
        self.evidence_button_right_3.setMinimumSize(QSize(40, 40))
        self.evidence_button_right_3.setIcon(icon1)
        self.evidence_button_right_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.evidence_button_right_3)


        self.verticalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.possible_ghost_table = QTableWidget(self.groupBox_2)
        if (self.possible_ghost_table.columnCount() < 3):
            self.possible_ghost_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.possible_ghost_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.possible_ghost_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.possible_ghost_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.possible_ghost_table.rowCount() < 3):
            self.possible_ghost_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.possible_ghost_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.possible_ghost_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.possible_ghost_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.possible_ghost_table.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.possible_ghost_table.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.possible_ghost_table.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.possible_ghost_table.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.possible_ghost_table.setItem(1, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.possible_ghost_table.setItem(1, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.possible_ghost_table.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.possible_ghost_table.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.possible_ghost_table.setItem(2, 2, __qtablewidgetitem14)
        self.possible_ghost_table.setObjectName(u"possible_ghost_table")
        font1 = QFont()
        font1.setPointSize(14)
        self.possible_ghost_table.setFont(font1)
        self.possible_ghost_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.possible_ghost_table.setAlternatingRowColors(False)
        self.possible_ghost_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.possible_ghost_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.possible_ghost_table.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.possible_ghost_table, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.widget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.reset_button = QPushButton(self.groupBox_3)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMinimumSize(QSize(60, 40))

        self.horizontalLayout_10.addWidget(self.reset_button)

        self.horizontalSpacer = QSpacerItem(205, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.log_button = QToolButton(self.groupBox_3)
        self.log_button.setObjectName(u"log_button")
        self.log_button.setMinimumSize(QSize(39, 40))
        icon2 = QIcon()
        icon2.addFile(u":/resources/img/icon/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.log_button.setIcon(icon2)
        self.log_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.log_button)

        self.settings_button = QToolButton(self.groupBox_3)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/resources/img/icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon3)
        self.settings_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.settings_button)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.horizontalLayout_4.addWidget(self.widget_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Ruled Out", None))
        self.evidence_button_left_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_4.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_4.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_5.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_5.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_6.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_6.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_7.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_7.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_8.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_8.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Eliminated", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Discovered Evidence", None))
        self.evidence_button_left_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_1.setText(QCoreApplication.translate("MainWindow", u"Dots Projector", None))
        self.evidence_button_right_1.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_2.setText(QCoreApplication.translate("MainWindow", u"Fingerprints", None))
        self.evidence_button_right_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_button_left_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.evidence_label_3.setText(QCoreApplication.translate("MainWindow", u"Freezing Temps", None))
        self.evidence_button_right_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Possible Ghosts", None))
        ___qtablewidgetitem = self.possible_ghost_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Max %", None));
        ___qtablewidgetitem1 = self.possible_ghost_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ghost", None));
        ___qtablewidgetitem2 = self.possible_ghost_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Missing Evidence", None));
        ___qtablewidgetitem3 = self.possible_ghost_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.possible_ghost_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.possible_ghost_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.possible_ghost_table.isSortingEnabled()
        self.possible_ghost_table.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.possible_ghost_table.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem7 = self.possible_ghost_table.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phantom", None));
        ___qtablewidgetitem8 = self.possible_ghost_table.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"DOTS", None));
        ___qtablewidgetitem9 = self.possible_ghost_table.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem10 = self.possible_ghost_table.item(1, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Poltergeist", None));
        ___qtablewidgetitem11 = self.possible_ghost_table.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Writing", None));
        ___qtablewidgetitem12 = self.possible_ghost_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"?", None));
        ___qtablewidgetitem13 = self.possible_ghost_table.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"The Mimic", None));
        ___qtablewidgetitem14 = self.possible_ghost_table.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Freezing, Orb", None));
        self.possible_ghost_table.setSortingEnabled(__sortingEnabled)

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.log_button.setToolTip(QCoreApplication.translate("MainWindow", u"Show Log", None))
#endif // QT_CONFIG(tooltip)
        self.log_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 226)
        SettingsDialog.setStyleSheet(u"#SettingsDialog {\n"
"	background-color: #31363b;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #4dd0e1;\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: #4dd0e1;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 7px;\n"
"	top: -10ox;\n"
"    padding: 0px 5px 0px 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: #4dd0e1;\n"
"	background-color: #232629;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    font: bold;\n"
"    border: 1px solid silver;\n"
"    border-radius: 6px;\n"
"    margin-top: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"color:  #9ea6ae;\n"
"}")
        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 201))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 91, 21))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.browser_source_url_edit = QLineEdit(self.groupBox)
        self.browser_source_url_edit.setObjectName(u"browser_source_url_edit")
        self.browser_source_url_edit.setGeometry(QRect(130, 20, 221, 20))
        self.browser_source_url_edit.setReadOnly(True)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 120, 181, 61))
        font = QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.enable_overlay_checkbox = QCheckBox(self.groupBox)
        self.enable_overlay_checkbox.setObjectName(u"enable_overlay_checkbox")
        self.enable_overlay_checkbox.setGeometry(QRect(240, 120, 111, 31))
        self.save_button = QPushButton(self.groupBox)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(240, 160, 111, 23))
        self.open_overlay_dir_button = QPushButton(self.groupBox)
        self.open_overlay_dir_button.setObjectName(u"open_overlay_dir_button")
        self.open_overlay_dir_button.setGeometry(QRect(130, 80, 221, 23))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 50, 71, 20))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.overlay_dir_edit = QLineEdit(self.groupBox)
        self.overlay_dir_edit.setObjectName(u"overlay_dir_edit")
        self.overlay_dir_edit.setGeometry(QRect(130, 50, 221, 20))
        self.overlay_dir_edit.setReadOnly(True)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Overlays", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Overlay Base URL:", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"PhasmoCompanion exposes a webserver on localhost to host browser sources for OBS overlays.", None))
        self.enable_overlay_checkbox.setText(QCoreApplication.translate("SettingsDialog", u"Enable Overlays", None))
        self.save_button.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
        self.open_overlay_dir_button.setText(QCoreApplication.translate("SettingsDialog", u"Open Overlay Directory", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Overlay Dir:", None))
    # retranslateUi



