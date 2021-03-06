# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_popup.ui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-truck.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-file.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setMaximumSize(QSize(1600, 100))
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.row_1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.row_1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_15.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.row_1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_15.addWidget(self.lineEdit_2)

        self.label_9 = QLabel(self.row_1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_15.addWidget(self.label_9)

        self.lineEdit_10 = QLineEdit(self.row_1)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_15.addWidget(self.lineEdit_10)


        self.gridLayout.addLayout(self.horizontalLayout_15, 3, 0, 1, 2)

        self.lineEdit = QLineEdit(self.row_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.row_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(112, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/cil-transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_7 = QLabel(self.row_1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_20.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.row_1)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_20.addWidget(self.lineEdit_3)

        self.label_10 = QLabel(self.row_1)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_20.addWidget(self.label_10)

        self.lineEdit_6 = QLineEdit(self.row_1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_20.addWidget(self.lineEdit_6)


        self.gridLayout.addLayout(self.horizontalLayout_20, 2, 0, 1, 2)


        self.horizontalLayout_6.addLayout(self.gridLayout)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_8 = QLabel(self.row_1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.lineEdit_4 = QLineEdit(self.row_1)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_16.addWidget(self.lineEdit_4)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.row_1)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.lineEdit_9 = QLineEdit(self.row_1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_12.addWidget(self.lineEdit_9)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.row_1)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.lineEdit_8 = QLineEdit(self.row_1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_10.addWidget(self.lineEdit_8)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.row_1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.lineEdit_5 = QLineEdit(self.row_1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_8.addWidget(self.lineEdit_5)


        self.gridLayout_3.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_2 = QLabel(self.row_1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.lineEdit_7 = QLineEdit(self.row_1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_9.addWidget(self.lineEdit_7)


        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_3)


        self.verticalLayout.addWidget(self.row_1)

        self.frame_2 = QFrame(self.widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 790, 659))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_7)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.gridLayout_36 = QGridLayout()
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.horizontalLayout_175 = QHBoxLayout()
        self.horizontalLayout_175.setObjectName(u"horizontalLayout_175")
        self.lineEdit_223 = QLineEdit(self.frame_7)
        self.lineEdit_223.setObjectName(u"lineEdit_223")
        self.lineEdit_223.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_223.setStyleSheet(u"background-color: rgb(195, 159, 0);")
        self.lineEdit_223.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_175.addWidget(self.lineEdit_223)


        self.gridLayout_36.addLayout(self.horizontalLayout_175, 0, 0, 1, 1)

        self.horizontalLayout_176 = QHBoxLayout()
        self.horizontalLayout_176.setObjectName(u"horizontalLayout_176")
        self.horizontalLayout_177 = QHBoxLayout()
        self.horizontalLayout_177.setObjectName(u"horizontalLayout_177")
        self.label_222 = QLabel(self.frame_7)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_177.addWidget(self.label_222)

        self.lineEdit_224 = QLineEdit(self.frame_7)
        self.lineEdit_224.setObjectName(u"lineEdit_224")
        self.lineEdit_224.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_177.addWidget(self.lineEdit_224)


        self.horizontalLayout_176.addLayout(self.horizontalLayout_177)

        self.horizontalLayout_178 = QHBoxLayout()
        self.horizontalLayout_178.setObjectName(u"horizontalLayout_178")
        self.label_223 = QLabel(self.frame_7)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_178.addWidget(self.label_223)

        self.lineEdit_225 = QLineEdit(self.frame_7)
        self.lineEdit_225.setObjectName(u"lineEdit_225")
        self.lineEdit_225.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_178.addWidget(self.lineEdit_225)


        self.horizontalLayout_176.addLayout(self.horizontalLayout_178)


        self.gridLayout_36.addLayout(self.horizontalLayout_176, 1, 0, 1, 1)

        self.horizontalLayout_179 = QHBoxLayout()
        self.horizontalLayout_179.setObjectName(u"horizontalLayout_179")
        self.verticalLayout_179 = QVBoxLayout()
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.label_224 = QLabel(self.frame_7)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_179.addWidget(self.label_224)

        self.lineEdit_226 = QLineEdit(self.frame_7)
        self.lineEdit_226.setObjectName(u"lineEdit_226")
        self.lineEdit_226.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_179.addWidget(self.lineEdit_226)


        self.horizontalLayout_179.addLayout(self.verticalLayout_179)

        self.verticalLayout_180 = QVBoxLayout()
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.label_225 = QLabel(self.frame_7)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_180.addWidget(self.label_225)

        self.lineEdit_227 = QLineEdit(self.frame_7)
        self.lineEdit_227.setObjectName(u"lineEdit_227")
        self.lineEdit_227.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_180.addWidget(self.lineEdit_227)


        self.horizontalLayout_179.addLayout(self.verticalLayout_180)

        self.verticalLayout_181 = QVBoxLayout()
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.label_226 = QLabel(self.frame_7)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_181.addWidget(self.label_226)

        self.lineEdit_228 = QLineEdit(self.frame_7)
        self.lineEdit_228.setObjectName(u"lineEdit_228")
        self.lineEdit_228.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_181.addWidget(self.lineEdit_228)


        self.horizontalLayout_179.addLayout(self.verticalLayout_181)


        self.gridLayout_36.addLayout(self.horizontalLayout_179, 2, 0, 1, 1)

        self.horizontalLayout_180 = QHBoxLayout()
        self.horizontalLayout_180.setObjectName(u"horizontalLayout_180")
        self.verticalLayout_182 = QVBoxLayout()
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.label_227 = QLabel(self.frame_7)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_182.addWidget(self.label_227)

        self.lineEdit_229 = QLineEdit(self.frame_7)
        self.lineEdit_229.setObjectName(u"lineEdit_229")
        self.lineEdit_229.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_182.addWidget(self.lineEdit_229)


        self.horizontalLayout_180.addLayout(self.verticalLayout_182)

        self.verticalLayout_183 = QVBoxLayout()
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.label_228 = QLabel(self.frame_7)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_183.addWidget(self.label_228)

        self.lineEdit_230 = QLineEdit(self.frame_7)
        self.lineEdit_230.setObjectName(u"lineEdit_230")
        self.lineEdit_230.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_183.addWidget(self.lineEdit_230)


        self.horizontalLayout_180.addLayout(self.verticalLayout_183)

        self.verticalLayout_184 = QVBoxLayout()
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.label_229 = QLabel(self.frame_7)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_184.addWidget(self.label_229)

        self.pushButton_30 = QPushButton(self.frame_7)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_184.addWidget(self.pushButton_30)


        self.horizontalLayout_180.addLayout(self.verticalLayout_184)


        self.gridLayout_36.addLayout(self.horizontalLayout_180, 3, 0, 1, 1)


        self.verticalLayout_30.addLayout(self.gridLayout_36)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_8)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.gridLayout_37 = QGridLayout()
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.horizontalLayout_181 = QHBoxLayout()
        self.horizontalLayout_181.setObjectName(u"horizontalLayout_181")
        self.lineEdit_231 = QLineEdit(self.frame_8)
        self.lineEdit_231.setObjectName(u"lineEdit_231")
        self.lineEdit_231.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_231.setStyleSheet(u"background-color: rgb(82, 153, 0);")
        self.lineEdit_231.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_181.addWidget(self.lineEdit_231)


        self.gridLayout_37.addLayout(self.horizontalLayout_181, 0, 0, 1, 1)

        self.horizontalLayout_182 = QHBoxLayout()
        self.horizontalLayout_182.setObjectName(u"horizontalLayout_182")
        self.horizontalLayout_183 = QHBoxLayout()
        self.horizontalLayout_183.setObjectName(u"horizontalLayout_183")
        self.label_230 = QLabel(self.frame_8)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_183.addWidget(self.label_230)

        self.lineEdit_232 = QLineEdit(self.frame_8)
        self.lineEdit_232.setObjectName(u"lineEdit_232")
        self.lineEdit_232.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_183.addWidget(self.lineEdit_232)


        self.horizontalLayout_182.addLayout(self.horizontalLayout_183)

        self.horizontalLayout_184 = QHBoxLayout()
        self.horizontalLayout_184.setObjectName(u"horizontalLayout_184")
        self.label_231 = QLabel(self.frame_8)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_184.addWidget(self.label_231)

        self.lineEdit_233 = QLineEdit(self.frame_8)
        self.lineEdit_233.setObjectName(u"lineEdit_233")
        self.lineEdit_233.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_184.addWidget(self.lineEdit_233)


        self.horizontalLayout_182.addLayout(self.horizontalLayout_184)


        self.gridLayout_37.addLayout(self.horizontalLayout_182, 1, 0, 1, 1)

        self.horizontalLayout_185 = QHBoxLayout()
        self.horizontalLayout_185.setObjectName(u"horizontalLayout_185")
        self.verticalLayout_185 = QVBoxLayout()
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.label_232 = QLabel(self.frame_8)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_185.addWidget(self.label_232)

        self.lineEdit_234 = QLineEdit(self.frame_8)
        self.lineEdit_234.setObjectName(u"lineEdit_234")
        self.lineEdit_234.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_185.addWidget(self.lineEdit_234)


        self.horizontalLayout_185.addLayout(self.verticalLayout_185)

        self.verticalLayout_186 = QVBoxLayout()
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.label_233 = QLabel(self.frame_8)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_186.addWidget(self.label_233)

        self.lineEdit_235 = QLineEdit(self.frame_8)
        self.lineEdit_235.setObjectName(u"lineEdit_235")
        self.lineEdit_235.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_186.addWidget(self.lineEdit_235)


        self.horizontalLayout_185.addLayout(self.verticalLayout_186)

        self.verticalLayout_187 = QVBoxLayout()
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.label_234 = QLabel(self.frame_8)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_187.addWidget(self.label_234)

        self.lineEdit_236 = QLineEdit(self.frame_8)
        self.lineEdit_236.setObjectName(u"lineEdit_236")
        self.lineEdit_236.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_187.addWidget(self.lineEdit_236)


        self.horizontalLayout_185.addLayout(self.verticalLayout_187)


        self.gridLayout_37.addLayout(self.horizontalLayout_185, 2, 0, 1, 1)

        self.horizontalLayout_186 = QHBoxLayout()
        self.horizontalLayout_186.setObjectName(u"horizontalLayout_186")
        self.verticalLayout_188 = QVBoxLayout()
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.label_235 = QLabel(self.frame_8)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_188.addWidget(self.label_235)

        self.lineEdit_237 = QLineEdit(self.frame_8)
        self.lineEdit_237.setObjectName(u"lineEdit_237")
        self.lineEdit_237.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_188.addWidget(self.lineEdit_237)


        self.horizontalLayout_186.addLayout(self.verticalLayout_188)

        self.verticalLayout_189 = QVBoxLayout()
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.label_236 = QLabel(self.frame_8)
        self.label_236.setObjectName(u"label_236")
        self.label_236.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_189.addWidget(self.label_236)

        self.lineEdit_238 = QLineEdit(self.frame_8)
        self.lineEdit_238.setObjectName(u"lineEdit_238")
        self.lineEdit_238.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_189.addWidget(self.lineEdit_238)


        self.horizontalLayout_186.addLayout(self.verticalLayout_189)

        self.verticalLayout_190 = QVBoxLayout()
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.label_237 = QLabel(self.frame_8)
        self.label_237.setObjectName(u"label_237")
        self.label_237.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_190.addWidget(self.label_237)

        self.pushButton_31 = QPushButton(self.frame_8)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_190.addWidget(self.pushButton_31)


        self.horizontalLayout_186.addLayout(self.verticalLayout_190)


        self.gridLayout_37.addLayout(self.horizontalLayout_186, 3, 0, 1, 1)


        self.verticalLayout_31.addLayout(self.gridLayout_37)


        self.horizontalLayout_11.addWidget(self.frame_8)


        self.verticalLayout_29.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.horizontalLayout_187 = QHBoxLayout()
        self.horizontalLayout_187.setObjectName(u"horizontalLayout_187")
        self.lineEdit_239 = QLineEdit(self.frame_9)
        self.lineEdit_239.setObjectName(u"lineEdit_239")
        self.lineEdit_239.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_239.setStyleSheet(u"background-color: rgb(95, 85, 149);")
        self.lineEdit_239.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_187.addWidget(self.lineEdit_239)


        self.gridLayout_38.addLayout(self.horizontalLayout_187, 0, 0, 1, 1)

        self.horizontalLayout_188 = QHBoxLayout()
        self.horizontalLayout_188.setObjectName(u"horizontalLayout_188")
        self.horizontalLayout_189 = QHBoxLayout()
        self.horizontalLayout_189.setObjectName(u"horizontalLayout_189")
        self.label_238 = QLabel(self.frame_9)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_189.addWidget(self.label_238)

        self.lineEdit_240 = QLineEdit(self.frame_9)
        self.lineEdit_240.setObjectName(u"lineEdit_240")
        self.lineEdit_240.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_189.addWidget(self.lineEdit_240)


        self.horizontalLayout_188.addLayout(self.horizontalLayout_189)

        self.horizontalLayout_190 = QHBoxLayout()
        self.horizontalLayout_190.setObjectName(u"horizontalLayout_190")
        self.label_239 = QLabel(self.frame_9)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_190.addWidget(self.label_239)

        self.lineEdit_241 = QLineEdit(self.frame_9)
        self.lineEdit_241.setObjectName(u"lineEdit_241")
        self.lineEdit_241.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_190.addWidget(self.lineEdit_241)


        self.horizontalLayout_188.addLayout(self.horizontalLayout_190)


        self.gridLayout_38.addLayout(self.horizontalLayout_188, 1, 0, 1, 1)

        self.horizontalLayout_191 = QHBoxLayout()
        self.horizontalLayout_191.setObjectName(u"horizontalLayout_191")
        self.verticalLayout_191 = QVBoxLayout()
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.label_240 = QLabel(self.frame_9)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_191.addWidget(self.label_240)

        self.lineEdit_242 = QLineEdit(self.frame_9)
        self.lineEdit_242.setObjectName(u"lineEdit_242")
        self.lineEdit_242.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_191.addWidget(self.lineEdit_242)


        self.horizontalLayout_191.addLayout(self.verticalLayout_191)

        self.verticalLayout_192 = QVBoxLayout()
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.label_241 = QLabel(self.frame_9)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_192.addWidget(self.label_241)

        self.lineEdit_243 = QLineEdit(self.frame_9)
        self.lineEdit_243.setObjectName(u"lineEdit_243")
        self.lineEdit_243.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_192.addWidget(self.lineEdit_243)


        self.horizontalLayout_191.addLayout(self.verticalLayout_192)

        self.verticalLayout_193 = QVBoxLayout()
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.label_242 = QLabel(self.frame_9)
        self.label_242.setObjectName(u"label_242")
        self.label_242.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_193.addWidget(self.label_242)

        self.lineEdit_244 = QLineEdit(self.frame_9)
        self.lineEdit_244.setObjectName(u"lineEdit_244")
        self.lineEdit_244.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_193.addWidget(self.lineEdit_244)


        self.horizontalLayout_191.addLayout(self.verticalLayout_193)


        self.gridLayout_38.addLayout(self.horizontalLayout_191, 2, 0, 1, 1)

        self.horizontalLayout_192 = QHBoxLayout()
        self.horizontalLayout_192.setObjectName(u"horizontalLayout_192")
        self.verticalLayout_194 = QVBoxLayout()
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.label_243 = QLabel(self.frame_9)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_194.addWidget(self.label_243)

        self.lineEdit_245 = QLineEdit(self.frame_9)
        self.lineEdit_245.setObjectName(u"lineEdit_245")
        self.lineEdit_245.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_194.addWidget(self.lineEdit_245)


        self.horizontalLayout_192.addLayout(self.verticalLayout_194)

        self.verticalLayout_195 = QVBoxLayout()
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.label_244 = QLabel(self.frame_9)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_195.addWidget(self.label_244)

        self.lineEdit_246 = QLineEdit(self.frame_9)
        self.lineEdit_246.setObjectName(u"lineEdit_246")
        self.lineEdit_246.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_195.addWidget(self.lineEdit_246)


        self.horizontalLayout_192.addLayout(self.verticalLayout_195)

        self.verticalLayout_196 = QVBoxLayout()
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.label_245 = QLabel(self.frame_9)
        self.label_245.setObjectName(u"label_245")
        self.label_245.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_196.addWidget(self.label_245)

        self.pushButton_32 = QPushButton(self.frame_9)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_196.addWidget(self.pushButton_32)


        self.horizontalLayout_192.addLayout(self.verticalLayout_196)


        self.gridLayout_38.addLayout(self.horizontalLayout_192, 3, 0, 1, 1)


        self.verticalLayout_32.addLayout(self.gridLayout_38)


        self.horizontalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_10)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.gridLayout_39 = QGridLayout()
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.horizontalLayout_193 = QHBoxLayout()
        self.horizontalLayout_193.setObjectName(u"horizontalLayout_193")
        self.lineEdit_247 = QLineEdit(self.frame_10)
        self.lineEdit_247.setObjectName(u"lineEdit_247")
        self.lineEdit_247.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_247.setStyleSheet(u"background-color: rgb(204, 85, 179);")
        self.lineEdit_247.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_193.addWidget(self.lineEdit_247)


        self.gridLayout_39.addLayout(self.horizontalLayout_193, 0, 0, 1, 1)

        self.horizontalLayout_194 = QHBoxLayout()
        self.horizontalLayout_194.setObjectName(u"horizontalLayout_194")
        self.horizontalLayout_195 = QHBoxLayout()
        self.horizontalLayout_195.setObjectName(u"horizontalLayout_195")
        self.label_246 = QLabel(self.frame_10)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_195.addWidget(self.label_246)

        self.lineEdit_248 = QLineEdit(self.frame_10)
        self.lineEdit_248.setObjectName(u"lineEdit_248")
        self.lineEdit_248.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_195.addWidget(self.lineEdit_248)


        self.horizontalLayout_194.addLayout(self.horizontalLayout_195)

        self.horizontalLayout_196 = QHBoxLayout()
        self.horizontalLayout_196.setObjectName(u"horizontalLayout_196")
        self.label_247 = QLabel(self.frame_10)
        self.label_247.setObjectName(u"label_247")
        self.label_247.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_196.addWidget(self.label_247)

        self.lineEdit_249 = QLineEdit(self.frame_10)
        self.lineEdit_249.setObjectName(u"lineEdit_249")
        self.lineEdit_249.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_196.addWidget(self.lineEdit_249)


        self.horizontalLayout_194.addLayout(self.horizontalLayout_196)


        self.gridLayout_39.addLayout(self.horizontalLayout_194, 1, 0, 1, 1)

        self.horizontalLayout_197 = QHBoxLayout()
        self.horizontalLayout_197.setObjectName(u"horizontalLayout_197")
        self.verticalLayout_197 = QVBoxLayout()
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.label_248 = QLabel(self.frame_10)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_197.addWidget(self.label_248)

        self.lineEdit_250 = QLineEdit(self.frame_10)
        self.lineEdit_250.setObjectName(u"lineEdit_250")
        self.lineEdit_250.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_197.addWidget(self.lineEdit_250)


        self.horizontalLayout_197.addLayout(self.verticalLayout_197)

        self.verticalLayout_198 = QVBoxLayout()
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.label_249 = QLabel(self.frame_10)
        self.label_249.setObjectName(u"label_249")
        self.label_249.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_198.addWidget(self.label_249)

        self.lineEdit_251 = QLineEdit(self.frame_10)
        self.lineEdit_251.setObjectName(u"lineEdit_251")
        self.lineEdit_251.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_198.addWidget(self.lineEdit_251)


        self.horizontalLayout_197.addLayout(self.verticalLayout_198)

        self.verticalLayout_199 = QVBoxLayout()
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.label_250 = QLabel(self.frame_10)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_199.addWidget(self.label_250)

        self.lineEdit_252 = QLineEdit(self.frame_10)
        self.lineEdit_252.setObjectName(u"lineEdit_252")
        self.lineEdit_252.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_199.addWidget(self.lineEdit_252)


        self.horizontalLayout_197.addLayout(self.verticalLayout_199)


        self.gridLayout_39.addLayout(self.horizontalLayout_197, 2, 0, 1, 1)

        self.horizontalLayout_198 = QHBoxLayout()
        self.horizontalLayout_198.setObjectName(u"horizontalLayout_198")
        self.verticalLayout_200 = QVBoxLayout()
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.label_251 = QLabel(self.frame_10)
        self.label_251.setObjectName(u"label_251")
        self.label_251.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_200.addWidget(self.label_251)

        self.lineEdit_253 = QLineEdit(self.frame_10)
        self.lineEdit_253.setObjectName(u"lineEdit_253")
        self.lineEdit_253.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_200.addWidget(self.lineEdit_253)


        self.horizontalLayout_198.addLayout(self.verticalLayout_200)

        self.verticalLayout_201 = QVBoxLayout()
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.label_252 = QLabel(self.frame_10)
        self.label_252.setObjectName(u"label_252")
        self.label_252.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_201.addWidget(self.label_252)

        self.lineEdit_254 = QLineEdit(self.frame_10)
        self.lineEdit_254.setObjectName(u"lineEdit_254")
        self.lineEdit_254.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_201.addWidget(self.lineEdit_254)


        self.horizontalLayout_198.addLayout(self.verticalLayout_201)

        self.verticalLayout_202 = QVBoxLayout()
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.label_253 = QLabel(self.frame_10)
        self.label_253.setObjectName(u"label_253")
        self.label_253.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_202.addWidget(self.label_253)

        self.pushButton_33 = QPushButton(self.frame_10)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_202.addWidget(self.pushButton_33)


        self.horizontalLayout_198.addLayout(self.verticalLayout_202)


        self.gridLayout_39.addLayout(self.horizontalLayout_198, 3, 0, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_39)


        self.horizontalLayout_13.addWidget(self.frame_10)


        self.verticalLayout_29.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.horizontalLayout_199 = QHBoxLayout()
        self.horizontalLayout_199.setObjectName(u"horizontalLayout_199")
        self.lineEdit_255 = QLineEdit(self.frame_11)
        self.lineEdit_255.setObjectName(u"lineEdit_255")
        self.lineEdit_255.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_255.setStyleSheet(u"background-color: rgb(222, 110, 75);")
        self.lineEdit_255.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_199.addWidget(self.lineEdit_255)


        self.gridLayout_40.addLayout(self.horizontalLayout_199, 0, 0, 1, 1)

        self.horizontalLayout_200 = QHBoxLayout()
        self.horizontalLayout_200.setObjectName(u"horizontalLayout_200")
        self.horizontalLayout_201 = QHBoxLayout()
        self.horizontalLayout_201.setObjectName(u"horizontalLayout_201")
        self.label_254 = QLabel(self.frame_11)
        self.label_254.setObjectName(u"label_254")
        self.label_254.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_201.addWidget(self.label_254)

        self.lineEdit_256 = QLineEdit(self.frame_11)
        self.lineEdit_256.setObjectName(u"lineEdit_256")
        self.lineEdit_256.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_201.addWidget(self.lineEdit_256)


        self.horizontalLayout_200.addLayout(self.horizontalLayout_201)

        self.horizontalLayout_202 = QHBoxLayout()
        self.horizontalLayout_202.setObjectName(u"horizontalLayout_202")
        self.label_255 = QLabel(self.frame_11)
        self.label_255.setObjectName(u"label_255")
        self.label_255.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_202.addWidget(self.label_255)

        self.lineEdit_257 = QLineEdit(self.frame_11)
        self.lineEdit_257.setObjectName(u"lineEdit_257")
        self.lineEdit_257.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_202.addWidget(self.lineEdit_257)


        self.horizontalLayout_200.addLayout(self.horizontalLayout_202)


        self.gridLayout_40.addLayout(self.horizontalLayout_200, 1, 0, 1, 1)

        self.horizontalLayout_203 = QHBoxLayout()
        self.horizontalLayout_203.setObjectName(u"horizontalLayout_203")
        self.verticalLayout_203 = QVBoxLayout()
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.label_256 = QLabel(self.frame_11)
        self.label_256.setObjectName(u"label_256")
        self.label_256.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_203.addWidget(self.label_256)

        self.lineEdit_258 = QLineEdit(self.frame_11)
        self.lineEdit_258.setObjectName(u"lineEdit_258")
        self.lineEdit_258.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_203.addWidget(self.lineEdit_258)


        self.horizontalLayout_203.addLayout(self.verticalLayout_203)

        self.verticalLayout_204 = QVBoxLayout()
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.label_257 = QLabel(self.frame_11)
        self.label_257.setObjectName(u"label_257")
        self.label_257.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_204.addWidget(self.label_257)

        self.lineEdit_259 = QLineEdit(self.frame_11)
        self.lineEdit_259.setObjectName(u"lineEdit_259")
        self.lineEdit_259.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_204.addWidget(self.lineEdit_259)


        self.horizontalLayout_203.addLayout(self.verticalLayout_204)

        self.verticalLayout_205 = QVBoxLayout()
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.label_258 = QLabel(self.frame_11)
        self.label_258.setObjectName(u"label_258")
        self.label_258.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_205.addWidget(self.label_258)

        self.lineEdit_260 = QLineEdit(self.frame_11)
        self.lineEdit_260.setObjectName(u"lineEdit_260")
        self.lineEdit_260.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_205.addWidget(self.lineEdit_260)


        self.horizontalLayout_203.addLayout(self.verticalLayout_205)


        self.gridLayout_40.addLayout(self.horizontalLayout_203, 2, 0, 1, 1)

        self.horizontalLayout_204 = QHBoxLayout()
        self.horizontalLayout_204.setObjectName(u"horizontalLayout_204")
        self.verticalLayout_206 = QVBoxLayout()
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.label_259 = QLabel(self.frame_11)
        self.label_259.setObjectName(u"label_259")
        self.label_259.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_206.addWidget(self.label_259)

        self.lineEdit_261 = QLineEdit(self.frame_11)
        self.lineEdit_261.setObjectName(u"lineEdit_261")
        self.lineEdit_261.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_206.addWidget(self.lineEdit_261)


        self.horizontalLayout_204.addLayout(self.verticalLayout_206)

        self.verticalLayout_207 = QVBoxLayout()
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.label_260 = QLabel(self.frame_11)
        self.label_260.setObjectName(u"label_260")
        self.label_260.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_207.addWidget(self.label_260)

        self.lineEdit_262 = QLineEdit(self.frame_11)
        self.lineEdit_262.setObjectName(u"lineEdit_262")
        self.lineEdit_262.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_207.addWidget(self.lineEdit_262)


        self.horizontalLayout_204.addLayout(self.verticalLayout_207)

        self.verticalLayout_208 = QVBoxLayout()
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.label_261 = QLabel(self.frame_11)
        self.label_261.setObjectName(u"label_261")
        self.label_261.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_208.addWidget(self.label_261)

        self.pushButton_34 = QPushButton(self.frame_11)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_208.addWidget(self.pushButton_34)


        self.horizontalLayout_204.addLayout(self.verticalLayout_208)


        self.gridLayout_40.addLayout(self.horizontalLayout_204, 3, 0, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout_40)


        self.horizontalLayout_14.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_12)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.gridLayout_41 = QGridLayout()
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.horizontalLayout_205 = QHBoxLayout()
        self.horizontalLayout_205.setObjectName(u"horizontalLayout_205")
        self.lineEdit_263 = QLineEdit(self.frame_12)
        self.lineEdit_263.setObjectName(u"lineEdit_263")
        self.lineEdit_263.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_263.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.lineEdit_263.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_205.addWidget(self.lineEdit_263)


        self.gridLayout_41.addLayout(self.horizontalLayout_205, 0, 0, 1, 1)

        self.horizontalLayout_206 = QHBoxLayout()
        self.horizontalLayout_206.setObjectName(u"horizontalLayout_206")
        self.horizontalLayout_207 = QHBoxLayout()
        self.horizontalLayout_207.setObjectName(u"horizontalLayout_207")
        self.label_262 = QLabel(self.frame_12)
        self.label_262.setObjectName(u"label_262")
        self.label_262.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_207.addWidget(self.label_262)

        self.lineEdit_264 = QLineEdit(self.frame_12)
        self.lineEdit_264.setObjectName(u"lineEdit_264")
        self.lineEdit_264.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_207.addWidget(self.lineEdit_264)


        self.horizontalLayout_206.addLayout(self.horizontalLayout_207)

        self.horizontalLayout_208 = QHBoxLayout()
        self.horizontalLayout_208.setObjectName(u"horizontalLayout_208")
        self.label_263 = QLabel(self.frame_12)
        self.label_263.setObjectName(u"label_263")
        self.label_263.setMaximumSize(QSize(16777215, 10))

        self.horizontalLayout_208.addWidget(self.label_263)

        self.lineEdit_265 = QLineEdit(self.frame_12)
        self.lineEdit_265.setObjectName(u"lineEdit_265")
        self.lineEdit_265.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_208.addWidget(self.lineEdit_265)


        self.horizontalLayout_206.addLayout(self.horizontalLayout_208)


        self.gridLayout_41.addLayout(self.horizontalLayout_206, 1, 0, 1, 1)

        self.horizontalLayout_209 = QHBoxLayout()
        self.horizontalLayout_209.setObjectName(u"horizontalLayout_209")
        self.verticalLayout_209 = QVBoxLayout()
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.label_264 = QLabel(self.frame_12)
        self.label_264.setObjectName(u"label_264")
        self.label_264.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_209.addWidget(self.label_264)

        self.lineEdit_266 = QLineEdit(self.frame_12)
        self.lineEdit_266.setObjectName(u"lineEdit_266")
        self.lineEdit_266.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_209.addWidget(self.lineEdit_266)


        self.horizontalLayout_209.addLayout(self.verticalLayout_209)

        self.verticalLayout_210 = QVBoxLayout()
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.label_265 = QLabel(self.frame_12)
        self.label_265.setObjectName(u"label_265")
        self.label_265.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_210.addWidget(self.label_265)

        self.lineEdit_267 = QLineEdit(self.frame_12)
        self.lineEdit_267.setObjectName(u"lineEdit_267")
        self.lineEdit_267.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_210.addWidget(self.lineEdit_267)


        self.horizontalLayout_209.addLayout(self.verticalLayout_210)

        self.verticalLayout_211 = QVBoxLayout()
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.label_266 = QLabel(self.frame_12)
        self.label_266.setObjectName(u"label_266")
        self.label_266.setMaximumSize(QSize(16777215, 10))

        self.verticalLayout_211.addWidget(self.label_266)

        self.lineEdit_268 = QLineEdit(self.frame_12)
        self.lineEdit_268.setObjectName(u"lineEdit_268")
        self.lineEdit_268.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_211.addWidget(self.lineEdit_268)


        self.horizontalLayout_209.addLayout(self.verticalLayout_211)


        self.gridLayout_41.addLayout(self.horizontalLayout_209, 2, 0, 1, 1)

        self.horizontalLayout_210 = QHBoxLayout()
        self.horizontalLayout_210.setObjectName(u"horizontalLayout_210")
        self.verticalLayout_212 = QVBoxLayout()
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.label_267 = QLabel(self.frame_12)
        self.label_267.setObjectName(u"label_267")
        self.label_267.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_212.addWidget(self.label_267)

        self.lineEdit_269 = QLineEdit(self.frame_12)
        self.lineEdit_269.setObjectName(u"lineEdit_269")
        self.lineEdit_269.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_212.addWidget(self.lineEdit_269)


        self.horizontalLayout_210.addLayout(self.verticalLayout_212)

        self.verticalLayout_213 = QVBoxLayout()
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.label_268 = QLabel(self.frame_12)
        self.label_268.setObjectName(u"label_268")
        self.label_268.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_213.addWidget(self.label_268)

        self.lineEdit_270 = QLineEdit(self.frame_12)
        self.lineEdit_270.setObjectName(u"lineEdit_270")
        self.lineEdit_270.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_213.addWidget(self.lineEdit_270)


        self.horizontalLayout_210.addLayout(self.verticalLayout_213)

        self.verticalLayout_214 = QVBoxLayout()
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.label_269 = QLabel(self.frame_12)
        self.label_269.setObjectName(u"label_269")
        self.label_269.setMaximumSize(QSize(16777215, 13))

        self.verticalLayout_214.addWidget(self.label_269)

        self.pushButton_35 = QPushButton(self.frame_12)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"background-color: rgb(0, 40, 0);")

        self.verticalLayout_214.addWidget(self.pushButton_35)


        self.horizontalLayout_210.addLayout(self.verticalLayout_214)


        self.gridLayout_41.addLayout(self.horizontalLayout_210, 3, 0, 1, 1)


        self.verticalLayout_35.addLayout(self.gridLayout_41)


        self.horizontalLayout_14.addWidget(self.frame_12)


        self.verticalLayout_29.addWidget(self.frame_4)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_17.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PneusTyres.com", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Melhor Valor : ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Valor : ", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pedido", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"   Buscar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Melhor Prazo :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Prazo : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Prazo Cliente", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Frete Cliente", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Valor Pedido:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Produto: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.lineEdit_223.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
        self.label_222.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_223.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_224.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_225.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_226.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_227.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_228.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_229.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit_231.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Expresso S\u00e3o Miguel", None))
        self.label_230.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_231.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_232.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_233.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_234.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_235.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit_239.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_239.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_240.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_245.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit_247.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
        self.label_246.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_247.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_248.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_249.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_250.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_251.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_252.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_253.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit_255.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora MID", None))
        self.label_254.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_255.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_256.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_257.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_258.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_259.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_260.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_261.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.lineEdit_263.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora", None))
        self.label_262.setText(QCoreApplication.translate("MainWindow", u"Cota\u00e7\u00e3o:", None))
        self.label_263.setText(QCoreApplication.translate("MainWindow", u"Valor :", None))
        self.label_264.setText(QCoreApplication.translate("MainWindow", u"Prazo ", None))
        self.label_265.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_266.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_267.setText(QCoreApplication.translate("MainWindow", u"Medidas", None))
        self.label_268.setText(QCoreApplication.translate("MainWindow", u"Cubagem", None))
        self.label_269.setText(QCoreApplication.translate("MainWindow", u"Usar Cota\u00e7\u00e3o", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Gabriel Moura", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

