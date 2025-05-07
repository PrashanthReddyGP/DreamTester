# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QTabWidget,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dreamtester(object):
    def setupUi(self, Dreamtester):
        if not Dreamtester.objectName():
            Dreamtester.setObjectName(u"Dreamtester")
        Dreamtester.resize(1749, 1031)
        Dreamtester.setMinimumSize(QSize(1036, 735))
        Dreamtester.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaTape))
        Dreamtester.setWindowIcon(icon)
        Dreamtester.setStyleSheet(u"background-color: rgb(42, 42, 42);\n"
"")
        Dreamtester.setTabShape(QTabWidget.TabShape.Rounded)
        self.Master_Widget = QWidget(Dreamtester)
        self.Master_Widget.setObjectName(u"Master_Widget")
        self.Master_Widget.setStyleSheet(u"\n"
"\n"
"/* Styles for QDateTimeEdit */\n"
"QDateEdit {\n"
"	background-color: rgb(62, 62, 62);\n"
"    border: none; /* Removes the border for QDateTimeEdit */\n"
"}\n"
"\n"
"/* Remove the up and down arrows */\n"
"QDateEdit::up-button,\n"
"QDateEdit::down-button {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right; /* Position the button if needed */\n"
"    width: 0px; /* Set width to 0 to hide */\n"
"    height: 0px; /* Set height to 0 to hide */\n"
"}\n"
"\n"
"/* Hover effect for QDateTimeEdit (when mouse hovers over the widget) */\n"
"QDateEdit:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Focused effect for QDateTimeEdit */\n"
"QDateEdit:focus {\n"
"    border: 2px solid #0078d7; /* Optional: Adds a border when focused */\n"
"    background-color: #e0e0e0; /* Optional: Change background color on focus */\n"
"}\n"
"\n"
"QLineEdit  {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(62, 62, 62);  /* Default"
                        " background color */\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a4a4a;  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.Master_Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Application_Tabs = QTabWidget(self.Master_Widget)
        self.Application_Tabs.setObjectName(u"Application_Tabs")
        self.Application_Tabs.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Application_Tabs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Application_Tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.Application_Tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.Application_Tabs.setDocumentMode(False)
        self.Application_Tabs.setTabsClosable(False)
        self.Application_Tabs.setMovable(False)
        self.Application_Tabs.setTabBarAutoHide(False)
        self.Portfolio_Tab = QWidget()
        self.Portfolio_Tab.setObjectName(u"Portfolio_Tab")
        self.horizontalLayout_14 = QHBoxLayout(self.Portfolio_Tab)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.Portfolio_Tab)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(400, 0))
        self.widget_12.setMaximumSize(QSize(400, 16777215))
        self.widget_12.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.verticalLayout_24 = QVBoxLayout(self.widget_12)
        self.verticalLayout_24.setSpacing(7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_27 = QLabel(self.widget_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 50))
        self.label_27.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_27)

        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_25 = QVBoxLayout(self.widget_14)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 5)
        self.widget_13 = QWidget(self.widget_14)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 30))
        self.widget_13.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.widget_13)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 30))
        self.pushButton_4.setMaximumSize(QSize(16777215, 30))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_27.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.widget_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(16777215, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_27.addWidget(self.pushButton_6)

        self.clear_strategies_button = QPushButton(self.widget_13)
        self.clear_strategies_button.setObjectName(u"clear_strategies_button")
        self.clear_strategies_button.setMinimumSize(QSize(0, 30))
        self.clear_strategies_button.setMaximumSize(QSize(16777215, 30))
        self.clear_strategies_button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_27.addWidget(self.clear_strategies_button)


        self.verticalLayout_25.addWidget(self.widget_13)

        self.Manager_Widget = QWidget(self.widget_14)
        self.Manager_Widget.setObjectName(u"Manager_Widget")
        self.Manager_Widget.setStyleSheet(u"")
        self.verticalLayout_26 = QVBoxLayout(self.Manager_Widget)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 11, 0, 11)

        self.verticalLayout_25.addWidget(self.Manager_Widget)


        self.verticalLayout_24.addWidget(self.widget_14)

        self.widget_16 = QWidget(self.widget_12)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMaximumSize(QSize(16777215, 30))
        self.verticalLayout_27 = QVBoxLayout(self.widget_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_23 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.Import_Strategy_Button = QPushButton(self.widget_18)
        self.Import_Strategy_Button.setObjectName(u"Import_Strategy_Button")
        self.Import_Strategy_Button.setMinimumSize(QSize(0, 30))
        self.Import_Strategy_Button.setMaximumSize(QSize(16777215, 30))
        self.Import_Strategy_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_23.addWidget(self.Import_Strategy_Button)


        self.verticalLayout_27.addWidget(self.widget_18)


        self.verticalLayout_24.addWidget(self.widget_16)

        self.Run_Backtest_Button = QPushButton(self.widget_12)
        self.Run_Backtest_Button.setObjectName(u"Run_Backtest_Button")
        self.Run_Backtest_Button.setMinimumSize(QSize(0, 30))
        self.Run_Backtest_Button.setMaximumSize(QSize(16777215, 30))
        self.Run_Backtest_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.verticalLayout_24.addWidget(self.Run_Backtest_Button)

        self.Trade_Results_Button = QPushButton(self.widget_12)
        self.Trade_Results_Button.setObjectName(u"Trade_Results_Button")
        self.Trade_Results_Button.setMinimumSize(QSize(0, 30))
        self.Trade_Results_Button.setMaximumSize(QSize(16777215, 30))
        self.Trade_Results_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.verticalLayout_24.addWidget(self.Trade_Results_Button)


        self.horizontalLayout_21.addWidget(self.widget_12)

        self.Portfolio_Tabs = QTabWidget(self.widget_11)
        self.Portfolio_Tabs.setObjectName(u"Portfolio_Tabs")
        self.Portfolio_Tabs.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Portfolio_Tabs.setStyleSheet(u"/* When hovering over a tab */\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(78. 78, 78);\n"
"}\n"
"\n"
"/* Selected tab customization */\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(71, 71, 71);\n"
"}\n"
"\n"
"/* Disabled tab */\n"
"QTabBar::tab:disabled {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"")
        self.Portfolio_Tabs.setTabPosition(QTabWidget.TabPosition.West)
        self.Portfolio_Tabs.setTabShape(QTabWidget.TabShape.Rounded)
        self.Portfolio_Tabs.setElideMode(Qt.TextElideMode.ElideNone)
        self.Portfolio_Tabs.setUsesScrollButtons(True)
        self.Portfolio_Tabs.setDocumentMode(False)
        self.Portfolio_Tabs.setTabsClosable(False)
        self.Portfolio_Tabs.setMovable(False)
        self.Portfolio_Tabs.setTabBarAutoHide(False)
        self.Script_Editor = QWidget()
        self.Script_Editor.setObjectName(u"Script_Editor")
        self.Script_Editor.setStyleSheet(u"")
        self.verticalLayout_28 = QVBoxLayout(self.Script_Editor)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.Script_Editor)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.verticalLayout_29 = QVBoxLayout(self.widget_21)
        self.verticalLayout_29.setSpacing(7)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_29 = QLabel(self.widget_21)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 50))
        self.label_29.setMaximumSize(QSize(16777215, 50))
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_29.setIndent(10)

        self.verticalLayout_29.addWidget(self.label_29)

        self.widget_22 = QWidget(self.widget_21)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.widget_22)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setMaximumSize(QSize(16777215, 30))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_29.addWidget(self.pushButton_7)

        self.savefile_button = QPushButton(self.widget_22)
        self.savefile_button.setObjectName(u"savefile_button")
        self.savefile_button.setMinimumSize(QSize(0, 30))
        self.savefile_button.setMaximumSize(QSize(16777215, 30))
        self.savefile_button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_29.addWidget(self.savefile_button)

        self.savefileas_button = QPushButton(self.widget_22)
        self.savefileas_button.setObjectName(u"savefileas_button")
        self.savefileas_button.setMinimumSize(QSize(0, 30))
        self.savefileas_button.setMaximumSize(QSize(16777215, 30))
        self.savefileas_button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_29.addWidget(self.savefileas_button)

        self.comboBox_3 = QComboBox(self.widget_22)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 30))
        self.comboBox_3.setMaximumSize(QSize(16777215, 30))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(62, 62, 62);")

        self.horizontalLayout_29.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.widget_22)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 30))
        self.comboBox_4.setMaximumSize(QSize(16777215, 30))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(62, 62, 62);")

        self.horizontalLayout_29.addWidget(self.comboBox_4)


        self.verticalLayout_29.addWidget(self.widget_22)

        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.script_editor_textedit = QTextEdit(self.widget_23)
        self.script_editor_textedit.setObjectName(u"script_editor_textedit")
        self.script_editor_textedit.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"")
        self.script_editor_textedit.setFrameShape(QFrame.Shape.NoFrame)
        self.script_editor_textedit.setFrameShadow(QFrame.Shadow.Plain)
        self.script_editor_textedit.setLineWidth(1)
        self.script_editor_textedit.setMidLineWidth(0)
        self.script_editor_textedit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)

        self.horizontalLayout_30.addWidget(self.script_editor_textedit)


        self.verticalLayout_29.addWidget(self.widget_23)


        self.verticalLayout_28.addWidget(self.widget_21)

        self.Portfolio_Tabs.addTab(self.Script_Editor, "")
        self.Price_Charts = QWidget()
        self.Price_Charts.setObjectName(u"Price_Charts")
        self.horizontalLayout_2 = QHBoxLayout(self.Price_Charts)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.Price_Charts)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Ohlcv_Chart_Group = QGroupBox(self.widget)
        self.Ohlcv_Chart_Group.setObjectName(u"Ohlcv_Chart_Group")
        self.horizontalLayout_16 = QHBoxLayout(self.Ohlcv_Chart_Group)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Ohlcv_Chart_Placeholder = QLabel(self.Ohlcv_Chart_Group)
        self.Ohlcv_Chart_Placeholder.setObjectName(u"Ohlcv_Chart_Placeholder")
        self.Ohlcv_Chart_Placeholder.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(130, 130, 130);")
        self.Ohlcv_Chart_Placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.Ohlcv_Chart_Placeholder)


        self.verticalLayout_7.addWidget(self.Ohlcv_Chart_Group)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 250))
        self.verticalLayout_8 = QVBoxLayout(self.widget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
"color: rgb(130, 130, 130);")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.widget_4)


        self.horizontalLayout_2.addWidget(self.widget)

        self.Portfolio_Tabs.addTab(self.Price_Charts, "")
        self.Equity_Charts = QWidget()
        self.Equity_Charts.setObjectName(u"Equity_Charts")
        self.verticalLayout_30 = QVBoxLayout(self.Equity_Charts)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.Equity_Charts)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy)
        self.widget_19.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.verticalLayout_31 = QVBoxLayout(self.widget_19)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.Equity_Chart_Groupbox = QGroupBox(self.widget_19)
        self.Equity_Chart_Groupbox.setObjectName(u"Equity_Chart_Groupbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(7)
        sizePolicy1.setHeightForWidth(self.Equity_Chart_Groupbox.sizePolicy().hasHeightForWidth())
        self.Equity_Chart_Groupbox.setSizePolicy(sizePolicy1)
        self.Equity_Chart_Groupbox.setStyleSheet(u"")
        self.Equity_Chart_Groupbox.setFlat(False)
        self.verticalLayout_32 = QVBoxLayout(self.Equity_Chart_Groupbox)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.Equity_Chart_Groupbox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(130, 130, 130);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_13)


        self.verticalLayout_31.addWidget(self.Equity_Chart_Groupbox)

        self.Drawdown_Chart_Groupbox = QGroupBox(self.widget_19)
        self.Drawdown_Chart_Groupbox.setObjectName(u"Drawdown_Chart_Groupbox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.Drawdown_Chart_Groupbox.sizePolicy().hasHeightForWidth())
        self.Drawdown_Chart_Groupbox.setSizePolicy(sizePolicy2)
        self.Drawdown_Chart_Groupbox.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.Drawdown_Chart_Groupbox)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(5, 5, 5, 5)
        self.label_62 = QLabel(self.Drawdown_Chart_Groupbox)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"color: rgb(130, 130, 130);")
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_62)


        self.verticalLayout_31.addWidget(self.Drawdown_Chart_Groupbox)


        self.verticalLayout_30.addWidget(self.widget_19)

        self.Portfolio_Tabs.addTab(self.Equity_Charts, "")
        self.Portfolio_Metrics = QWidget()
        self.Portfolio_Metrics.setObjectName(u"Portfolio_Metrics")
        self.verticalLayout_34 = QVBoxLayout(self.Portfolio_Metrics)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.Portfolio_Metrics)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setStyleSheet(u"background-color: rgb(71, 71, 71);")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.groupBox_3 = QGroupBox(self.widget_25)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"background-color: rgb(54, 54, 54);\n"
"")
        self.groupBox_3.setFlat(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.Max_Runup_Output = QLabel(self.groupBox_3)
        self.Max_Runup_Output.setObjectName(u"Max_Runup_Output")
        self.Max_Runup_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Max_Runup_Output, 32, 1, 1, 1)

        self.Largest_Loss_Output = QLabel(self.groupBox_3)
        self.Largest_Loss_Output.setObjectName(u"Largest_Loss_Output")
        self.Largest_Loss_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Largest_Loss_Output, 25, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)

        self.Total_Wins_Output = QLabel(self.groupBox_3)
        self.Total_Wins_Output.setObjectName(u"Total_Wins_Output")
        self.Total_Wins_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Total_Wins_Output, 20, 1, 1, 1)

        self.Avg_Runup_Output = QLabel(self.groupBox_3)
        self.Avg_Runup_Output.setObjectName(u"Avg_Runup_Output")
        self.Avg_Runup_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Runup_Output, 33, 1, 1, 1)

        self.Max_Drawdown_Duration_Output = QLabel(self.groupBox_3)
        self.Max_Drawdown_Duration_Output.setObjectName(u"Max_Drawdown_Duration_Output")
        self.Max_Drawdown_Duration_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Max_Drawdown_Duration_Output, 12, 1, 1, 1)

        self.Avg_Win_Output = QLabel(self.groupBox_3)
        self.Avg_Win_Output.setObjectName(u"Avg_Win_Output")
        self.Avg_Win_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Win_Output, 27, 1, 1, 1)

        self.Max_Open_Trades_Output = QLabel(self.groupBox_3)
        self.Max_Open_Trades_Output.setObjectName(u"Max_Open_Trades_Output")
        self.Max_Open_Trades_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Max_Open_Trades_Output, 36, 1, 1, 1)

        self.Annual_Return_Output = QLabel(self.groupBox_3)
        self.Annual_Return_Output.setObjectName(u"Annual_Return_Output")
        self.Annual_Return_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Annual_Return_Output, 7, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 33, 0, 1, 1)

        self.Avg_Loss_Output = QLabel(self.groupBox_3)
        self.Avg_Loss_Output.setObjectName(u"Avg_Loss_Output")
        self.Avg_Loss_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Loss_Output, 28, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 26, 0, 1, 1)

        self.Equity_Efficiency_Rate_Output = QLabel(self.groupBox_3)
        self.Equity_Efficiency_Rate_Output.setObjectName(u"Equity_Efficiency_Rate_Output")
        self.Equity_Efficiency_Rate_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Equity_Efficiency_Rate_Output, 17, 1, 1, 1)

        self.Total_Trades_Label = QLabel(self.groupBox_3)
        self.Total_Trades_Label.setObjectName(u"Total_Trades_Label")
        self.Total_Trades_Label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Total_Trades_Label, 8, 0, 1, 1)

        self.Profit_Factor_Output = QLabel(self.groupBox_3)
        self.Profit_Factor_Output.setObjectName(u"Profit_Factor_Output")
        self.Profit_Factor_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Profit_Factor_Output, 14, 1, 1, 1)

        self.label_36 = QLabel(self.groupBox_3)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout.addWidget(self.label_36, 30, 0, 1, 1)

        self.Consecutive_Losses_Output = QLabel(self.groupBox_3)
        self.Consecutive_Losses_Output.setObjectName(u"Consecutive_Losses_Output")
        self.Consecutive_Losses_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Consecutive_Losses_Output, 23, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 20, 0, 1, 1)

        self.Max_Drawdown_Output = QLabel(self.groupBox_3)
        self.Max_Drawdown_Output.setObjectName(u"Max_Drawdown_Output")
        self.Max_Drawdown_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Max_Drawdown_Output, 11, 1, 1, 1)

        self.Gross_Profit_Output = QLabel(self.groupBox_3)
        self.Gross_Profit_Output.setObjectName(u"Gross_Profit_Output")
        self.Gross_Profit_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Gross_Profit_Output, 5, 1, 1, 1)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Shadow.Plain)
        self.line_2.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)

        self.Largest_Win_Output = QLabel(self.groupBox_3)
        self.Largest_Win_Output.setObjectName(u"Largest_Win_Output")
        self.Largest_Win_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Largest_Win_Output, 24, 1, 1, 1)

        self.Initial_Capital_Input = QLineEdit(self.groupBox_3)
        self.Initial_Capital_Input.setObjectName(u"Initial_Capital_Input")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Initial_Capital_Input.sizePolicy().hasHeightForWidth())
        self.Initial_Capital_Input.setSizePolicy(sizePolicy3)
        self.Initial_Capital_Input.setMaximumSize(QSize(16777215, 16777215))
        self.Initial_Capital_Input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Initial_Capital_Input.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Initial_Capital_Input, 2, 1, 1, 1)

        self.RR_Output = QLabel(self.groupBox_3)
        self.RR_Output.setObjectName(u"RR_Output")
        self.RR_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.RR_Output, 35, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 37, 0, 1, 1)

        self.Closed_Trades_Label = QLabel(self.groupBox_3)
        self.Closed_Trades_Label.setObjectName(u"Closed_Trades_Label")
        self.Closed_Trades_Label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Closed_Trades_Label, 9, 0, 1, 1)

        self.Avg_Trade_Output = QLabel(self.groupBox_3)
        self.Avg_Trade_Output.setObjectName(u"Avg_Trade_Output")
        self.Avg_Trade_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Trade_Output, 26, 1, 1, 1)

        self.Avg_Loss_Time_Output = QLabel(self.groupBox_3)
        self.Avg_Loss_Time_Output.setObjectName(u"Avg_Loss_Time_Output")
        self.Avg_Loss_Time_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Loss_Time_Output, 31, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox_3)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 31, 0, 1, 1)

        self.Closed_Trades_Output = QLabel(self.groupBox_3)
        self.Closed_Trades_Output.setObjectName(u"Closed_Trades_Output")
        self.Closed_Trades_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Closed_Trades_Output, 10, 1, 1, 1)

        self.label_59 = QLabel(self.groupBox_3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout.addWidget(self.label_59, 35, 0, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 24, 0, 1, 1)

        self.Avg_Win_Time_Output = QLabel(self.groupBox_3)
        self.Avg_Win_Time_Output.setObjectName(u"Avg_Win_Time_Output")
        self.Avg_Win_Time_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Win_Time_Output, 30, 1, 1, 1)

        self.Calmar_Ratio_Output = QLabel(self.groupBox_3)
        self.Calmar_Ratio_Output.setObjectName(u"Calmar_Ratio_Output")
        self.Calmar_Ratio_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Calmar_Ratio_Output, 16, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(90, 0))
        self.label_45.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(False)
        self.label_45.setFont(font1)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_45, 0, 1, 1, 1)

        self.Total_Trades_Output = QLabel(self.groupBox_3)
        self.Total_Trades_Output.setObjectName(u"Total_Trades_Output")
        self.Total_Trades_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Total_Trades_Output, 8, 1, 1, 1)

        self.label_38 = QLabel(self.groupBox_3)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 32, 0, 1, 1)

        self.label_76 = QLabel(self.groupBox_3)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout.addWidget(self.label_76, 17, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 15, 0, 1, 1)

        self.Avg_Open_Trades_Output = QLabel(self.groupBox_3)
        self.Avg_Open_Trades_Output.setObjectName(u"Avg_Open_Trades_Output")
        self.Avg_Open_Trades_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Open_Trades_Output, 37, 1, 1, 1)

        self.Avg_Drawdown_Output = QLabel(self.groupBox_3)
        self.Avg_Drawdown_Output.setObjectName(u"Avg_Drawdown_Output")
        self.Avg_Drawdown_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Drawdown_Output, 13, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_63 = QLabel(self.groupBox_3)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout.addWidget(self.label_63, 19, 0, 1, 1)

        self.Net_Profit_Output = QLabel(self.groupBox_3)
        self.Net_Profit_Output.setObjectName(u"Net_Profit_Output")
        self.Net_Profit_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Net_Profit_Output, 3, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 29, 0, 1, 1)

        self.Open_Trades_Output = QLabel(self.groupBox_3)
        self.Open_Trades_Output.setObjectName(u"Open_Trades_Output")
        self.Open_Trades_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Open_Trades_Output, 9, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 22, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(175, 0))

        self.gridLayout.addWidget(self.label_18, 23, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 25, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 28, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_3)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 3, 0, 1, 1)

        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Shadow.Plain)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.Kelly_Output = QLabel(self.groupBox_3)
        self.Kelly_Output.setObjectName(u"Kelly_Output")
        self.Kelly_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Kelly_Output, 19, 1, 1, 1)

        self.label_78 = QLabel(self.groupBox_3)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout.addWidget(self.label_78, 12, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 36, 0, 1, 1)

        self.Total_Losses_Output = QLabel(self.groupBox_3)
        self.Total_Losses_Output.setObjectName(u"Total_Losses_Output")
        self.Total_Losses_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Total_Losses_Output, 21, 1, 1, 1)

        self.Avg_Trade_Time_Output = QLabel(self.groupBox_3)
        self.Avg_Trade_Time_Output.setObjectName(u"Avg_Trade_Time_Output")
        self.Avg_Trade_Time_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Avg_Trade_Time_Output, 29, 1, 1, 1)

        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout.addWidget(self.label_60, 16, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.Profit_Percentage_Output = QLabel(self.groupBox_3)
        self.Profit_Percentage_Output.setObjectName(u"Profit_Percentage_Output")
        self.Profit_Percentage_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Profit_Percentage_Output, 6, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox_3)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout.addWidget(self.label_42, 34, 0, 1, 1)

        self.Consecutive_Wins_Output = QLabel(self.groupBox_3)
        self.Consecutive_Wins_Output.setObjectName(u"Consecutive_Wins_Output")
        self.Consecutive_Wins_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Consecutive_Wins_Output, 22, 1, 1, 1)

        self.label_61 = QLabel(self.groupBox_3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout.addWidget(self.label_61, 7, 0, 1, 1)

        self.Winrate_Output = QLabel(self.groupBox_3)
        self.Winrate_Output.setObjectName(u"Winrate_Output")
        self.Winrate_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Winrate_Output, 34, 1, 1, 1)

        self.Sharpe_Ratio_Output = QLabel(self.groupBox_3)
        self.Sharpe_Ratio_Output.setObjectName(u"Sharpe_Ratio_Output")
        self.Sharpe_Ratio_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Sharpe_Ratio_Output, 15, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 10, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 21, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 27, 0, 1, 1)

        self.label_77 = QLabel(self.groupBox_3)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout.addWidget(self.label_77, 18, 0, 1, 1)

        self.Strategy_Quality_Output = QLabel(self.groupBox_3)
        self.Strategy_Quality_Output.setObjectName(u"Strategy_Quality_Output")
        self.Strategy_Quality_Output.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.Strategy_Quality_Output, 18, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.horizontalLayout_28.addWidget(self.groupBox_3)


        self.verticalLayout_34.addWidget(self.widget_25)

        self.Portfolio_Tabs.addTab(self.Portfolio_Metrics, "")

        self.horizontalLayout_21.addWidget(self.Portfolio_Tabs)


        self.horizontalLayout_14.addWidget(self.widget_11)

        self.Application_Tabs.addTab(self.Portfolio_Tab, "")
        self.ML_Tab = QWidget()
        self.ML_Tab.setObjectName(u"ML_Tab")
        self.ML_Tab.setStyleSheet(u"\n"
"\n"
"/* Global QComboBox styles */\n"
"QComboBox {\n"
"    background-color: rgb(62, 62, 62); /* Default background color */\n"
"    padding-left: 10px; /* Space on the left */\n"
"}\n"
"\n"
"/* Hover effect for QComboBox */\n"
"QComboBox:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Pressed (clicked) effect for QComboBox */\n"
"QComboBox:pressed {\n"
"    background-color: #b0b0b0; /* Background color when clicked */\n"
"}\n"
"\n"
"/* For the popup list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #a0a0a0; /* Optional: Add border to the popup */\n"
"    selection-background-color: #0078d7; /* Background color for selected items */\n"
"    selection-color: #fff; /* Text color for selected items */\n"
"}\n"
"\n"
"/* Highlighting the item when hovered in the popup */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0078d7; /* Background color on hover */\n"
"    color: #fff; /* Text color on hover */\n"
"}")
        self.horizontalLayout_34 = QHBoxLayout(self.ML_Tab)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.widget_45 = QWidget(self.ML_Tab)
        self.widget_45.setObjectName(u"widget_45")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_45.sizePolicy().hasHeightForWidth())
        self.widget_45.setSizePolicy(sizePolicy4)
        self.widget_45.setMinimumSize(QSize(375, 0))
        self.widget_45.setMaximumSize(QSize(375, 16777215))
        self.widget_45.setStyleSheet(u"/* Global QComboBox styles */\n"
"QComboBox {\n"
"    background-color: rgb(62, 62, 62); /* Default background color */\n"
"    padding-left: 10px; /* Space on the left */\n"
"}\n"
"\n"
"/* Hover effect for QComboBox */\n"
"QComboBox:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Pressed (clicked) effect for QComboBox */\n"
"QComboBox:pressed {\n"
"    background-color: #b0b0b0; /* Background color when clicked */\n"
"}\n"
"\n"
"/* For the popup list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #a0a0a0; /* Optional: Add border to the popup */\n"
"    selection-background-color: #0078d7; /* Background color for selected items */\n"
"    selection-color: #fff; /* Text color for selected items */\n"
"}\n"
"\n"
"/* Highlighting the item when hovered in the popup */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0078d7; /* Background color on hover */\n"
"    color: #fff; /* Text color on hover */\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.widget_45)
        self.verticalLayout_39.setSpacing(7)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_47 = QWidget(self.widget_45)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setStyleSheet(u"QWidget	{\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        self.verticalLayout_41 = QVBoxLayout(self.widget_47)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.widget_47)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 30))
        self.label_64.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setBold(True)
        self.label_64.setFont(font2)
        self.label_64.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_64.setIndent(10)

        self.verticalLayout_41.addWidget(self.label_64)

        self.widget_44 = QWidget(self.widget_47)
        self.widget_44.setObjectName(u"widget_44")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget_44.sizePolicy().hasHeightForWidth())
        self.widget_44.setSizePolicy(sizePolicy5)
        self.widget_44.setStyleSheet(u"/* Global QComboBox styles */\n"
"QComboBox {\n"
"    background-color: rgb(62, 62, 62); /* Default background color */\n"
"    padding-left: 10px; /* Space on the left */\n"
"}\n"
"\n"
"/* Hover effect for QComboBox */\n"
"QComboBox:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Pressed (clicked) effect for QComboBox */\n"
"QComboBox:pressed {\n"
"    background-color: #b0b0b0; /* Background color when clicked */\n"
"}\n"
"\n"
"/* For the popup list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #a0a0a0; /* Optional: Add border to the popup */\n"
"    selection-background-color: #0078d7; /* Background color for selected items */\n"
"    selection-color: #fff; /* Text color for selected items */\n"
"}\n"
"\n"
"/* Highlighting the item when hovered in the popup */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0078d7; /* Background color on hover */\n"
"    color: #fff; /* Text color on hover */\n"
"}")
        self.verticalLayout_38 = QVBoxLayout(self.widget_44)
        self.verticalLayout_38.setSpacing(7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(11, 11, 11, 11)
        self.widget_42 = QWidget(self.widget_44)
        self.widget_42.setObjectName(u"widget_42")
        self.widget_42.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.widget_42)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(125, 30))
        self.label_65.setMaximumSize(QSize(125, 30))
        self.label_65.setIndent(10)

        self.horizontalLayout_35.addWidget(self.label_65)

        self.ml_symbol_selection_Combobox = QComboBox(self.widget_42)
        self.ml_symbol_selection_Combobox.setObjectName(u"ml_symbol_selection_Combobox")
        self.ml_symbol_selection_Combobox.setMinimumSize(QSize(0, 30))
        self.ml_symbol_selection_Combobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_35.addWidget(self.ml_symbol_selection_Combobox)


        self.verticalLayout_38.addWidget(self.widget_42)

        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.widget_46)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(125, 30))
        self.label_66.setMaximumSize(QSize(125, 30))
        self.label_66.setIndent(10)

        self.horizontalLayout_36.addWidget(self.label_66)

        self.ml_timeframe_selection_Combobox = QComboBox(self.widget_46)
        self.ml_timeframe_selection_Combobox.setObjectName(u"ml_timeframe_selection_Combobox")
        self.ml_timeframe_selection_Combobox.setMinimumSize(QSize(0, 30))
        self.ml_timeframe_selection_Combobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_36.addWidget(self.ml_timeframe_selection_Combobox)


        self.verticalLayout_38.addWidget(self.widget_46)

        self.widget_48 = QWidget(self.widget_44)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 30))
        self.widget_48.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.widget_48)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(125, 30))
        self.label_67.setMaximumSize(QSize(125, 30))
        self.label_67.setIndent(10)

        self.horizontalLayout_37.addWidget(self.label_67)

        self.ml_startdate_Dateedit = QDateEdit(self.widget_48)
        self.ml_startdate_Dateedit.setObjectName(u"ml_startdate_Dateedit")
        self.ml_startdate_Dateedit.setMinimumSize(QSize(0, 30))
        self.ml_startdate_Dateedit.setMaximumSize(QSize(16777215, 30))
        self.ml_startdate_Dateedit.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.ml_startdate_Dateedit.setFrame(True)
        self.ml_startdate_Dateedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ml_startdate_Dateedit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(16, 0, 0)))
        self.ml_startdate_Dateedit.setMinimumDate(QDate(1899, 12, 27))
        self.ml_startdate_Dateedit.setCalendarPopup(True)
        self.ml_startdate_Dateedit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.ml_startdate_Dateedit.setDate(QDate(2000, 1, 1))

        self.horizontalLayout_37.addWidget(self.ml_startdate_Dateedit)


        self.verticalLayout_38.addWidget(self.widget_48)

        self.widget_49 = QWidget(self.widget_44)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMinimumSize(QSize(0, 30))
        self.widget_49.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_38 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.widget_49)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(125, 30))
        self.label_68.setMaximumSize(QSize(125, 30))
        self.label_68.setIndent(10)

        self.horizontalLayout_38.addWidget(self.label_68)

        self.ml_enddate_Dateedit = QDateEdit(self.widget_49)
        self.ml_enddate_Dateedit.setObjectName(u"ml_enddate_Dateedit")
        self.ml_enddate_Dateedit.setMinimumSize(QSize(0, 30))
        self.ml_enddate_Dateedit.setMaximumSize(QSize(16777215, 30))
        self.ml_enddate_Dateedit.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.ml_enddate_Dateedit.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ml_enddate_Dateedit.setDateTime(QDateTime(QDate(2100, 1, 1), QTime(16, 0, 0)))
        self.ml_enddate_Dateedit.setCalendarPopup(True)
        self.ml_enddate_Dateedit.setTimeSpec(Qt.TimeSpec.LocalTime)
        self.ml_enddate_Dateedit.setDate(QDate(2100, 1, 1))

        self.horizontalLayout_38.addWidget(self.ml_enddate_Dateedit)


        self.verticalLayout_38.addWidget(self.widget_49)

        self.verticalSpacer_13 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_13)

        self.ml_fetchdata_Button = QPushButton(self.widget_44)
        self.ml_fetchdata_Button.setObjectName(u"ml_fetchdata_Button")
        self.ml_fetchdata_Button.setMinimumSize(QSize(0, 30))
        self.ml_fetchdata_Button.setMaximumSize(QSize(16777215, 30))
        self.ml_fetchdata_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.verticalLayout_38.addWidget(self.ml_fetchdata_Button)

        self.verticalSpacer_16 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_16)

        self.ml_debug_Textedit = QPlainTextEdit(self.widget_44)
        self.ml_debug_Textedit.setObjectName(u"ml_debug_Textedit")
        self.ml_debug_Textedit.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.ml_debug_Textedit.setFrameShape(QFrame.Shape.NoFrame)
        self.ml_debug_Textedit.setFrameShadow(QFrame.Shadow.Plain)
        self.ml_debug_Textedit.setLineWrapMode(QPlainTextEdit.LineWrapMode.NoWrap)
        self.ml_debug_Textedit.setReadOnly(True)

        self.verticalLayout_38.addWidget(self.ml_debug_Textedit)

        self.widget_59 = QWidget(self.widget_44)
        self.widget_59.setObjectName(u"widget_59")
        self.widget_59.setMinimumSize(QSize(0, 30))
        self.widget_59.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_43.setSpacing(7)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.ml_backtest_selection_Combobox = QComboBox(self.widget_59)
        self.ml_backtest_selection_Combobox.setObjectName(u"ml_backtest_selection_Combobox")
        self.ml_backtest_selection_Combobox.setMinimumSize(QSize(0, 30))
        self.ml_backtest_selection_Combobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_43.addWidget(self.ml_backtest_selection_Combobox)

        self.ml_backtest_Button = QPushButton(self.widget_59)
        self.ml_backtest_Button.setObjectName(u"ml_backtest_Button")
        self.ml_backtest_Button.setMinimumSize(QSize(0, 30))
        self.ml_backtest_Button.setMaximumSize(QSize(16777215, 30))
        self.ml_backtest_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.horizontalLayout_43.addWidget(self.ml_backtest_Button)


        self.verticalLayout_38.addWidget(self.widget_59)


        self.verticalLayout_41.addWidget(self.widget_44)


        self.verticalLayout_39.addWidget(self.widget_47)

        self.widget_53 = QWidget(self.widget_45)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setStyleSheet(u"QWidget	{\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.widget_53)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.widget_53)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 30))
        self.label_72.setMaximumSize(QSize(16777215, 30))
        self.label_72.setFont(font2)
        self.label_72.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_72.setIndent(10)

        self.verticalLayout_42.addWidget(self.label_72)

        self.widget_52 = QWidget(self.widget_53)
        self.widget_52.setObjectName(u"widget_52")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_52.sizePolicy().hasHeightForWidth())
        self.widget_52.setSizePolicy(sizePolicy6)
        self.widget_52.setStyleSheet(u"/* Global QComboBox styles */\n"
"QComboBox {\n"
"    background-color: rgb(62, 62, 62); /* Default background color */\n"
"    padding-left: 10px; /* Space on the left */\n"
"}\n"
"\n"
"/* Hover effect for QComboBox */\n"
"QComboBox:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Pressed (clicked) effect for QComboBox */\n"
"QComboBox:pressed {\n"
"    background-color: #b0b0b0; /* Background color when clicked */\n"
"}\n"
"\n"
"/* For the popup list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #a0a0a0; /* Optional: Add border to the popup */\n"
"    selection-background-color: #0078d7; /* Background color for selected items */\n"
"    selection-color: #fff; /* Text color for selected items */\n"
"}\n"
"\n"
"/* Highlighting the item when hovered in the popup */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0078d7; /* Background color on hover */\n"
"    color: #fff; /* Text color on hover */\n"
"}")
        self.verticalLayout_40 = QVBoxLayout(self.widget_52)
        self.verticalLayout_40.setSpacing(7)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 11, -1, 11)
        self.widget_54 = QWidget(self.widget_52)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setMinimumSize(QSize(0, 30))
        self.widget_54.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_73 = QLabel(self.widget_54)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(0, 30))
        self.label_73.setMaximumSize(QSize(125, 30))
        self.label_73.setIndent(10)

        self.horizontalLayout_41.addWidget(self.label_73)

        self.ml_models_Combobox = QComboBox(self.widget_54)
        self.ml_models_Combobox.setObjectName(u"ml_models_Combobox")
        self.ml_models_Combobox.setMinimumSize(QSize(0, 30))
        self.ml_models_Combobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_41.addWidget(self.ml_models_Combobox)


        self.verticalLayout_40.addWidget(self.widget_54)

        self.widget_50 = QWidget(self.widget_52)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMinimumSize(QSize(0, 30))
        self.widget_50.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_39 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_39.setSpacing(7)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.widget_50)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(125, 30))
        self.label_69.setMaximumSize(QSize(125, 30))
        self.label_69.setIndent(10)

        self.horizontalLayout_39.addWidget(self.label_69)

        self.ml_datasplit_Slider = QSlider(self.widget_50)
        self.ml_datasplit_Slider.setObjectName(u"ml_datasplit_Slider")
        self.ml_datasplit_Slider.setMinimumSize(QSize(0, 30))
        self.ml_datasplit_Slider.setMaximumSize(QSize(16777215, 30))
        self.ml_datasplit_Slider.setStyleSheet(u"")
        self.ml_datasplit_Slider.setMinimum(0)
        self.ml_datasplit_Slider.setMaximum(100)
        self.ml_datasplit_Slider.setSingleStep(10)
        self.ml_datasplit_Slider.setPageStep(20)
        self.ml_datasplit_Slider.setValue(80)
        self.ml_datasplit_Slider.setTracking(True)
        self.ml_datasplit_Slider.setOrientation(Qt.Orientation.Horizontal)
        self.ml_datasplit_Slider.setInvertedAppearance(False)
        self.ml_datasplit_Slider.setInvertedControls(False)

        self.horizontalLayout_39.addWidget(self.ml_datasplit_Slider)

        self.ml_datasplit_Label = QLabel(self.widget_50)
        self.ml_datasplit_Label.setObjectName(u"ml_datasplit_Label")
        self.ml_datasplit_Label.setMinimumSize(QSize(40, 30))
        self.ml_datasplit_Label.setMaximumSize(QSize(40, 30))
        self.ml_datasplit_Label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ml_datasplit_Label.setIndent(10)

        self.horizontalLayout_39.addWidget(self.ml_datasplit_Label)


        self.verticalLayout_40.addWidget(self.widget_50)

        self.widget_51 = QWidget(self.widget_52)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMinimumSize(QSize(0, 30))
        self.widget_51.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_40 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.widget_51)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(0, 30))
        self.label_71.setMaximumSize(QSize(125, 30))
        self.label_71.setIndent(10)

        self.horizontalLayout_40.addWidget(self.label_71)

        self.ml_fitness_function_Combobox = QComboBox(self.widget_51)
        self.ml_fitness_function_Combobox.setObjectName(u"ml_fitness_function_Combobox")
        self.ml_fitness_function_Combobox.setMinimumSize(QSize(0, 30))
        self.ml_fitness_function_Combobox.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_40.addWidget(self.ml_fitness_function_Combobox)


        self.verticalLayout_40.addWidget(self.widget_51)

        self.verticalSpacer_12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_40.addItem(self.verticalSpacer_12)

        self.ml_simulate_Button = QPushButton(self.widget_52)
        self.ml_simulate_Button.setObjectName(u"ml_simulate_Button")
        self.ml_simulate_Button.setMinimumSize(QSize(0, 30))
        self.ml_simulate_Button.setMaximumSize(QSize(16777215, 30))
        self.ml_simulate_Button.setStyleSheet(u"QPushButton {\n"
"    border: none;  /* Removes the border */\n"
"    background-color: rgb(90, 90, 90);  /* Default background color */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #353535;  /* Background color when pressed */\n"
"}")

        self.verticalLayout_40.addWidget(self.ml_simulate_Button)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_15)


        self.verticalLayout_42.addWidget(self.widget_52)


        self.verticalLayout_39.addWidget(self.widget_53)


        self.horizontalLayout_34.addWidget(self.widget_45)

        self.widget_43 = QWidget(self.ML_Tab)
        self.widget_43.setObjectName(u"widget_43")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(7)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_43.sizePolicy().hasHeightForWidth())
        self.widget_43.setSizePolicy(sizePolicy7)
        self.widget_43.setStyleSheet(u"")
        self.verticalLayout_37 = QVBoxLayout(self.widget_43)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.widget_55 = QWidget(self.widget_43)
        self.widget_55.setObjectName(u"widget_55")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(6)
        sizePolicy8.setHeightForWidth(self.widget_55.sizePolicy().hasHeightForWidth())
        self.widget_55.setSizePolicy(sizePolicy8)
        self.horizontalLayout_42 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.widget_57 = QWidget(self.widget_55)
        self.widget_57.setObjectName(u"widget_57")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(8)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.widget_57.sizePolicy().hasHeightForWidth())
        self.widget_57.setSizePolicy(sizePolicy9)
        self.widget_57.setStyleSheet(u"QWidget	{\n"
"	background-color: rgb(71, 71, 71);\n"
"}\n"
"/* Global QComboBox styles */\n"
"QComboBox {\n"
"    background-color: rgb(62, 62, 62); /* Default background color */\n"
"    padding-left: 10px; /* Space on the left */\n"
"}\n"
"\n"
"/* Hover effect for QComboBox */\n"
"QComboBox:hover {\n"
"    background-color: #d0d0d0; /* Background color on hover */\n"
"}\n"
"\n"
"/* Pressed (clicked) effect for QComboBox */\n"
"QComboBox:pressed {\n"
"    background-color: #b0b0b0; /* Background color when clicked */\n"
"}\n"
"\n"
"/* For the popup list */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #a0a0a0; /* Optional: Add border to the popup */\n"
"    selection-background-color: #0078d7; /* Background color for selected items */\n"
"    selection-color: #fff; /* Text color for selected items */\n"
"}\n"
"\n"
"/* Highlighting the item when hovered in the popup */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #0078d7; /* Background color on hover */\n"
"    color: #"
                        "fff; /* Text color on hover */\n"
"}")
        self.verticalLayout_43 = QVBoxLayout(self.widget_57)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.widget_63 = QWidget(self.widget_57)
        self.widget_63.setObjectName(u"widget_63")
        self.widget_63.setMinimumSize(QSize(0, 30))
        self.widget_63.setMaximumSize(QSize(16777215, 30))
        self.widget_63.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.widget_63)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(0, 30))
        self.label_70.setMaximumSize(QSize(16777215, 30))
        self.label_70.setFont(font2)
        self.label_70.setStyleSheet(u"")
        self.label_70.setIndent(10)

        self.horizontalLayout_44.addWidget(self.label_70)

        self.comboBox = QComboBox(self.widget_63)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 30))
        self.comboBox.setMaximumSize(QSize(150, 30))
        self.comboBox.setFrame(False)

        self.horizontalLayout_44.addWidget(self.comboBox)


        self.verticalLayout_43.addWidget(self.widget_63)

        self.widget_62 = QWidget(self.widget_57)
        self.widget_62.setObjectName(u"widget_62")
        self.verticalLayout_46 = QVBoxLayout(self.widget_62)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(5, 5, 5, 5)
        self.chart_placeholder_Label = QLabel(self.widget_62)
        self.chart_placeholder_Label.setObjectName(u"chart_placeholder_Label")
        self.chart_placeholder_Label.setStyleSheet(u"color: rgb(130, 130, 130);")
        self.chart_placeholder_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_46.addWidget(self.chart_placeholder_Label)


        self.verticalLayout_43.addWidget(self.widget_62)


        self.horizontalLayout_42.addWidget(self.widget_57)

        self.widget_58 = QWidget(self.widget_55)
        self.widget_58.setObjectName(u"widget_58")
        sizePolicy4.setHeightForWidth(self.widget_58.sizePolicy().hasHeightForWidth())
        self.widget_58.setSizePolicy(sizePolicy4)
        self.widget_58.setStyleSheet(u"QWidget	{\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        self.verticalLayout_45 = QVBoxLayout(self.widget_58)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_75 = QLabel(self.widget_58)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(0, 30))
        self.label_75.setMaximumSize(QSize(16777215, 30))
        self.label_75.setFont(font2)
        self.label_75.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_75.setIndent(10)

        self.verticalLayout_45.addWidget(self.label_75)

        self.widget_60 = QWidget(self.widget_58)
        self.widget_60.setObjectName(u"widget_60")

        self.verticalLayout_45.addWidget(self.widget_60)


        self.horizontalLayout_42.addWidget(self.widget_58)


        self.verticalLayout_37.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.widget_43)
        self.widget_56.setObjectName(u"widget_56")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(2)
        sizePolicy10.setHeightForWidth(self.widget_56.sizePolicy().hasHeightForWidth())
        self.widget_56.setSizePolicy(sizePolicy10)
        self.widget_56.setStyleSheet(u"QWidget	{\n"
"	background-color: rgb(71, 71, 71);\n"
"}")
        self.verticalLayout_44 = QVBoxLayout(self.widget_56)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_74 = QLabel(self.widget_56)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(0, 30))
        self.label_74.setMaximumSize(QSize(16777215, 30))
        self.label_74.setFont(font2)
        self.label_74.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.label_74.setIndent(10)

        self.verticalLayout_44.addWidget(self.label_74)

        self.widget_61 = QWidget(self.widget_56)
        self.widget_61.setObjectName(u"widget_61")

        self.verticalLayout_44.addWidget(self.widget_61)


        self.verticalLayout_37.addWidget(self.widget_56)


        self.horizontalLayout_34.addWidget(self.widget_43)

        self.Application_Tabs.addTab(self.ML_Tab, "")

        self.horizontalLayout.addWidget(self.Application_Tabs)

        Dreamtester.setCentralWidget(self.Master_Widget)

        self.retranslateUi(Dreamtester)

        self.Application_Tabs.setCurrentIndex(0)
        self.Portfolio_Tabs.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dreamtester)
    # setupUi

    def retranslateUi(self, Dreamtester):
        Dreamtester.setWindowTitle(QCoreApplication.translate("Dreamtester", u"Dreamtester", None))
        self.label_27.setText(QCoreApplication.translate("Dreamtester", u"PORTFOLIO MANAGER", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dreamtester", u"Toggle Selection", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dreamtester", u"Toggle Visibility", None))
        self.clear_strategies_button.setText(QCoreApplication.translate("Dreamtester", u"Clear All", None))
        self.Import_Strategy_Button.setText(QCoreApplication.translate("Dreamtester", u"Import Strategy", None))
        self.Run_Backtest_Button.setText(QCoreApplication.translate("Dreamtester", u"Run Backtest", None))
        self.Trade_Results_Button.setText(QCoreApplication.translate("Dreamtester", u"Trade Results", None))
        self.label_29.setText(QCoreApplication.translate("Dreamtester", u"SCRIPT EDITOR", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dreamtester", u"New file", None))
        self.savefile_button.setText(QCoreApplication.translate("Dreamtester", u"Save file", None))
        self.savefileas_button.setText(QCoreApplication.translate("Dreamtester", u"Save file as", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("Dreamtester", u"Strategy Name", None))
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("Dreamtester", u"Available Variables", None))
        self.script_editor_textedit.setDocumentTitle("")
        self.script_editor_textedit.setPlaceholderText(QCoreApplication.translate("Dreamtester", u"Strategy code goes here...", None))
        self.Portfolio_Tabs.setTabText(self.Portfolio_Tabs.indexOf(self.Script_Editor), QCoreApplication.translate("Dreamtester", u"Script Editor", None))
        self.Ohlcv_Chart_Group.setTitle(QCoreApplication.translate("Dreamtester", u"Charts tab", None))
        self.Ohlcv_Chart_Placeholder.setText(QCoreApplication.translate("Dreamtester", u"Chart goes here", None))
        self.label_3.setText(QCoreApplication.translate("Dreamtester", u"Data preview...", None))
        self.Portfolio_Tabs.setTabText(self.Portfolio_Tabs.indexOf(self.Price_Charts), QCoreApplication.translate("Dreamtester", u"Price Charts", None))
        self.Equity_Chart_Groupbox.setTitle(QCoreApplication.translate("Dreamtester", u"Equity Chart", None))
        self.label_13.setText(QCoreApplication.translate("Dreamtester", u"Equity Chart goes here", None))
        self.Drawdown_Chart_Groupbox.setTitle(QCoreApplication.translate("Dreamtester", u"Drawdown Chart", None))
        self.label_62.setText(QCoreApplication.translate("Dreamtester", u"Drawdown Chart goes here", None))
        self.Portfolio_Tabs.setTabText(self.Portfolio_Tabs.indexOf(self.Equity_Charts), QCoreApplication.translate("Dreamtester", u"Equity Charts", None))
        self.groupBox_3.setTitle("")
        self.Max_Runup_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Largest_Loss_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Dreamtester", u"Max Drawdown", None))
        self.Total_Wins_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Avg_Runup_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Max_Drawdown_Duration_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Avg_Win_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Max_Open_Trades_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Annual_Return_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Dreamtester", u"Avg Run-up", None))
        self.Avg_Loss_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_21.setText(QCoreApplication.translate("Dreamtester", u"Avg Trade", None))
        self.Equity_Efficiency_Rate_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Total_Trades_Label.setText(QCoreApplication.translate("Dreamtester", u"Total Trades", None))
        self.Profit_Factor_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_36.setText(QCoreApplication.translate("Dreamtester", u"Avg Win Time", None))
        self.Consecutive_Losses_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Dreamtester", u"Total Winning Trades", None))
        self.Max_Drawdown_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Gross_Profit_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Largest_Win_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Initial_Capital_Input.setText(QCoreApplication.translate("Dreamtester", u"1000", None))
        self.RR_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_15.setText(QCoreApplication.translate("Dreamtester", u"Avg Open Trades", None))
        self.Closed_Trades_Label.setText(QCoreApplication.translate("Dreamtester", u"Open Trades", None))
        self.Avg_Trade_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Avg_Loss_Time_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_37.setText(QCoreApplication.translate("Dreamtester", u"Avg Loss Time", None))
        self.Closed_Trades_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_59.setText(QCoreApplication.translate("Dreamtester", u"Risk-to-Reward Ratio", None))
        self.label_19.setText(QCoreApplication.translate("Dreamtester", u"Largest Win", None))
        self.Avg_Win_Time_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Calmar_Ratio_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_45.setText(QCoreApplication.translate("Dreamtester", u"PORTFOLIO", None))
        self.Total_Trades_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_38.setText(QCoreApplication.translate("Dreamtester", u"Max Run-up", None))
        self.label_76.setText(QCoreApplication.translate("Dreamtester", u"Equity Efficiency Rate", None))
        self.label_10.setText(QCoreApplication.translate("Dreamtester", u"Sharpe Ratio", None))
        self.Avg_Open_Trades_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Avg_Drawdown_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Dreamtester", u"Profit Percentage", None))
        self.label_63.setText(QCoreApplication.translate("Dreamtester", u"Kelly's Criterion", None))
        self.Net_Profit_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_24.setText(QCoreApplication.translate("Dreamtester", u"Avg Trade Time", None))
        self.Open_Trades_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_17.setText(QCoreApplication.translate("Dreamtester", u"Max Consecutive Wins", None))
        self.label_18.setText(QCoreApplication.translate("Dreamtester", u"Max Consecutive Losses", None))
        self.label_20.setText(QCoreApplication.translate("Dreamtester", u"Largest Loss", None))
        self.label_23.setText(QCoreApplication.translate("Dreamtester", u"Avg Loosing Trade", None))
        self.label_9.setText(QCoreApplication.translate("Dreamtester", u"Profit Factor", None))
        self.label_8.setText(QCoreApplication.translate("Dreamtester", u"Avg Drawdown", None))
        self.label_34.setText(QCoreApplication.translate("Dreamtester", u"Net Profit", None))
        self.Kelly_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_78.setText(QCoreApplication.translate("Dreamtester", u"Max Drawdown Duration", None))
        self.label_14.setText(QCoreApplication.translate("Dreamtester", u"Max Open Trades", None))
        self.Total_Losses_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Avg_Trade_Time_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label.setText(QCoreApplication.translate("Dreamtester", u"Gross Profit", None))
        self.label_60.setText(QCoreApplication.translate("Dreamtester", u"Calmar Ratio", None))
        self.label_12.setText(QCoreApplication.translate("Dreamtester", u"Initial Capital", None))
        self.Profit_Percentage_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_42.setText(QCoreApplication.translate("Dreamtester", u"Win rate", None))
        self.Consecutive_Wins_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_61.setText(QCoreApplication.translate("Dreamtester", u"Annual Return", None))
        self.Winrate_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Sharpe_Ratio_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Dreamtester", u"Closed Trades", None))
        self.label_16.setText(QCoreApplication.translate("Dreamtester", u"Total Loosing Trades", None))
        self.label_22.setText(QCoreApplication.translate("Dreamtester", u"Avg Winning Trade", None))
        self.label_77.setText(QCoreApplication.translate("Dreamtester", u"Strategy Quality", None))
        self.Strategy_Quality_Output.setText(QCoreApplication.translate("Dreamtester", u"0", None))
        self.Portfolio_Tabs.setTabText(self.Portfolio_Tabs.indexOf(self.Portfolio_Metrics), QCoreApplication.translate("Dreamtester", u"Portfolio Metrics", None))
        self.Application_Tabs.setTabText(self.Application_Tabs.indexOf(self.Portfolio_Tab), QCoreApplication.translate("Dreamtester", u"Portfolio", None))
        self.label_64.setText(QCoreApplication.translate("Dreamtester", u"ASSET PARAMETERS", None))
        self.label_65.setText(QCoreApplication.translate("Dreamtester", u"Symbol", None))
        self.label_66.setText(QCoreApplication.translate("Dreamtester", u"Timeframe", None))
        self.label_67.setText(QCoreApplication.translate("Dreamtester", u"Start Date", None))
        self.label_68.setText(QCoreApplication.translate("Dreamtester", u"End Date", None))
        self.ml_fetchdata_Button.setText(QCoreApplication.translate("Dreamtester", u"FETCH DATA", None))
        self.ml_debug_Textedit.setPlaceholderText(QCoreApplication.translate("Dreamtester", u"Debugging . . .", None))
        self.ml_backtest_Button.setText(QCoreApplication.translate("Dreamtester", u"BACKTEST", None))
        self.label_72.setText(QCoreApplication.translate("Dreamtester", u"ML CONFIGURATION", None))
        self.label_73.setText(QCoreApplication.translate("Dreamtester", u"ML Model", None))
        self.label_69.setText(QCoreApplication.translate("Dreamtester", u"Train/Test Split", None))
        self.ml_datasplit_Label.setText(QCoreApplication.translate("Dreamtester", u"80%", None))
        self.label_71.setText(QCoreApplication.translate("Dreamtester", u"Fitness Function", None))
        self.ml_simulate_Button.setText(QCoreApplication.translate("Dreamtester", u"SIMULATE", None))
        self.label_70.setText(QCoreApplication.translate("Dreamtester", u"VISUALIZATION", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dreamtester", u"Equity Curve", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dreamtester", u"Drawdown", None))

        self.chart_placeholder_Label.setText(QCoreApplication.translate("Dreamtester", u"Chart goes here", None))
        self.label_75.setText(QCoreApplication.translate("Dreamtester", u"PROPERTIES", None))
        self.label_74.setText(QCoreApplication.translate("Dreamtester", u"DATAFRAME", None))
        self.Application_Tabs.setTabText(self.Application_Tabs.indexOf(self.ML_Tab), QCoreApplication.translate("Dreamtester", u"Machine Learning", None))
    # retranslateUi

