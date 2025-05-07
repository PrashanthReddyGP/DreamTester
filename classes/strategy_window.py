import os
import importlib.util
import inspect
from line_profiler import LineProfiler

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QDateEdit, QWidget, QApplication, QFileDialog
from PySide6.QtCore import QSize, QDate, QCoreApplication, Qt

from .basestrategy import BaseStrategy  # Import basestrategy.py file from the current folder

class StrategyWindow(QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.parent = parent
        
        # Set pop-up window properties
        self.setWindowTitle("Strategy Editor")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet(u"background-color: rgb(71,71,71)")
        
        # Layouts for organizing the UI elements
        layout = QVBoxLayout()

        # STRATEGY
        strategy_layout = QHBoxLayout()
        strategy_label = QLabel("STRATEGY", self)
        self.strategy_button = QPushButton("Choose", self)
        self.strategy_button.setMinimumHeight(30)
        self.strategy_button.setStyleSheet(u"QPushButton {\n"
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
        self.strategy_button.clicked.connect(self.import_strategy_file)
        strategy_layout.addWidget(strategy_label)
        strategy_layout.addWidget(self.strategy_button)
        layout.addLayout(strategy_layout)

        # EXIT TYPE

        # SYMBOL
        symbol_layout = QHBoxLayout()
        symbol_label = QLabel("SYMBOL", self)
        self.symbol_combo = QComboBox(self)
        self.parent.populate_symbols(self.symbol_combo)
        self.symbol_combo.setMinimumHeight(30)
        self.symbol_combo.setStyleSheet(u"border:none; \n"
                                        "background-color: rgb(62, 62, 62)")
        symbol_layout.addWidget(symbol_label)
        symbol_layout.addWidget(self.symbol_combo)
        layout.addLayout(symbol_layout)

        # TIMEFRAME
        timeframe_layout = QHBoxLayout()
        timeframe_label = QLabel("TIMEFRAME", self)
        self.timeframe_combo = QComboBox(self)
        self.parent.populate_timeframes(self.timeframe_combo)
        self.timeframe_combo.setMinimumHeight(30)
        self.timeframe_combo.setStyleSheet(u"border:none; \n"
                                        "background-color: rgb(62, 62, 62)")
        timeframe_layout.addWidget(timeframe_label)
        timeframe_layout.addWidget(self.timeframe_combo)
        layout.addLayout(timeframe_layout)

        # TIME RANGE
        startdate_layout = QHBoxLayout()
        startdate_label = QLabel("START DATE", self)
        self.startdate_dateedit = QDateEdit(self)
        self.startdate_dateedit.setObjectName(u"startdate_dateedit")
        self.startdate_dateedit.setMinimumSize(QSize(0, 30))
        self.startdate_dateedit.setStyleSheet(u"border:none; \n"
                                        "background-color: rgb(62, 62, 62)")
        self.startdate_dateedit.setCalendarPopup(True)
        self.startdate_dateedit.setDate(QDate.currentDate())
        
        enddate_layout = QHBoxLayout()
        enddate_label = QLabel("END DATE", self)
        self.enddate_dateedit = QDateEdit(self)
        self.enddate_dateedit.setObjectName(u"enddate_dateedit")
        self.enddate_dateedit.setMinimumSize(QSize(0, 30))
        self.enddate_dateedit.setStyleSheet(u"border:none; \n"
                                        "background-color: rgb(62, 62, 62)")
        self.enddate_dateedit.setCalendarPopup(True)
        self.enddate_dateedit.setDate(QDate.currentDate())
        
        startdate_layout.addWidget(startdate_label)
        startdate_layout.addWidget(self.startdate_dateedit)
        layout.addLayout(startdate_layout)

        enddate_layout.addWidget(enddate_label)
        enddate_layout.addWidget(self.enddate_dateedit)
        layout.addLayout(enddate_layout)
        
        # INDICATORS
        indicator_layout = QHBoxLayout()
        indicator_label = QLabel("INDICATORS", self)
        indicator_label.setMinimumHeight(30)
        indicator_label.setMaximumHeight(30)
        indicator_add_button = QPushButton("Add", self)
        indicator_add_button.setMinimumHeight(30)
        indicator_add_button.setStyleSheet(u"QPushButton {\n"
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
        indicator_add_button.clicked.connect(lambda: self.parent.add_indicator_widget(self.I_Contents_Container, self.I_Holder_Layout))
        indicator_layout.addWidget(indicator_label)
        indicator_layout.addWidget(indicator_add_button)
        layout.addLayout(indicator_layout)
        
        self.I_Contents_Container = QWidget(self)
        self.I_Contents_Container.setObjectName(u"I_Contents_Container")
        
        self.I_Holder_Layout = QVBoxLayout(self.I_Contents_Container)
        self.I_Holder_Layout.setSpacing(0)
        self.I_Holder_Layout.setObjectName(u"I_Holder_Layout")
        self.I_Holder_Layout.setContentsMargins(0, 0, 0, 0)
        
        self.I_Placeholder_Label = QLabel(self.I_Contents_Container)
        self.I_Placeholder_Label.setObjectName(u"I_Placeholder_Label")
        self.I_Placeholder_Label.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                    "color: rgb(130, 130, 130);")
        self.I_Placeholder_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.I_Placeholder_Label.setText(QCoreApplication.translate("Dream_Machine", u"Indicator goes here", None))
        
        self.I_Holder_Layout.addWidget(self.I_Placeholder_Label)
        layout.addWidget(self.I_Contents_Container)
        
        # ADD AND CLOSE
        add_close_layout = QHBoxLayout()
        self.add_button = QPushButton("Add", self)
        self.add_button.setMinimumHeight(30)
        self.add_button.setStyleSheet(u"QPushButton {\n"
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
        self.close_button = QPushButton("Close", self)
        self.close_button.setMinimumHeight(30)
        self.close_button.setStyleSheet(u"QPushButton {\n"
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
        self.add_button.clicked.connect(self.get_ohlcv_data)
        # self.add_button.clicked.connect(self.get_indicators_data)
        self.add_button.clicked.connect(self.add_strategy_widget)
        self.add_button.clicked.connect(self.script_editor)
        self.add_button.clicked.connect(self.close)
        self.close_button.clicked.connect(self.close)
        add_close_layout.addWidget(self.add_button)
        add_close_layout.addWidget(self.close_button)
        
        layout.addLayout(add_close_layout)
        
        # Set the layout for the pop-up window
        self.setLayout(layout)

        # Center the window
        self.center_window()

        self.parent.ui.savefile_button.clicked.connect(self.save_file)
        self.parent.ui.savefileas_button.clicked.connect(self.save_file_as)

    def center_window(self):
        
        # Get the screen's geometry using QScreen from QGuiApplication
        screen = QApplication.primaryScreen().availableGeometry()

        # Calculate the x and y position to center the window
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        
        # Move the window to the calculated position
        self.move(x, y)
    
    def import_strategy_file(self):
        if self.parent:
            self.filepath = self.parent.on_Import_Button_Click()
            
            self.update_strategy_editor()

    def update_strategy_editor(self):
        if self.filepath:
            
            module = self.load_module_from_file(self.filepath)

            strategy_class = self.get_strategy_class(module)
            
            if strategy_class:
                # Instantiate the class and print values of its attributes
                strategy_instance = strategy_class()
                self.update_strategy_UI(strategy_instance)
            else:
                print("No class found that inherits from 'BaseStrategy'.")
                
    # Function to dynamically load the Python file as a module
    def load_module_from_file(self, file_path):
        
        module_name = os.path.splitext(os.path.basename(file_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    
    # Function to get the class that inherits from BaseStrategy
    def get_strategy_class(self, module):
        
        # Iterate over all classes in the module and check if they inherit from BaseStrategy
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseStrategy) and obj != BaseStrategy:
                return obj
        return None
    
    # Function to print the values of certain attributes if they exist
    def update_strategy_UI(self, strategy_instance):
        
        if hasattr(strategy_instance, 'symbol'):
            self.symbol_combo.setCurrentText(strategy_instance.symbol)
        if hasattr(strategy_instance, 'timeframe'):
            self.timeframe_combo.setCurrentText(strategy_instance.timeframe)
        if hasattr(strategy_instance, 'start_date'):
            start_date = QDate.fromString(strategy_instance.start_date, 'yyyy-MM-dd')
            self.startdate_dateedit.setDate(start_date)
        if hasattr(strategy_instance, 'end_date'):
            end_date = QDate.fromString(strategy_instance.end_date, 'yyyy-MM-dd')
            self.enddate_dateedit.setDate(end_date)
            
        if hasattr(strategy_instance, 'indicators'):
            
            self.widget_list = []
            
            for i, indicator in enumerate(strategy_instance.indicators, start=1):
                
                name, timeframe, params = indicator
                
                IName_CBox, ITimeframe_CBox, IValues_Text, self.widget_list = self.parent.add_indicator_widget(self.I_Contents_Container, self.I_Holder_Layout, self.widget_list)
                
                if isinstance(params, tuple):  # Check if params is a tuple
                    # Join the tuple elements with a comma
                    params_str = ', '.join(map(str, params))
                else:
                    # If it's a single value, just convert it to a string
                    params_str = str(params)
                    
                IName_CBox.setCurrentText(name)
                ITimeframe_CBox.setCurrentText(timeframe)
                IValues_Text.setText(params_str)
    
    def get_ohlcv_data(self):
        
        # profiler = LineProfiler()
        # profiler.add_function(self.parent.download_ohlcv_data)
        # profiler.enable_by_count()
        
        self.df, self.df_3m, self.df_5m, self.df_15m, self.df_1H, self.df_1D  = self.parent.download_ohlcv_data(self.symbol_combo, self.timeframe_combo, self.startdate_dateedit, self.enddate_dateedit)
        
        # profiler.disable_by_count()
        # profiler.print_stats()  # Print the detailed report
        
    
    def get_indicators_data(self):
        self.df = self.parent.indicator_verification(self.widget_list, self.df, self.df_3m, self.df_5m, self.df_15m, self.df_1H, self.df_1D)

    def add_strategy_widget(self):
        if self.filepath:
            
            # Package all the dataframes into a dictionary
            ohlcv_data = {
                'widget': self.widget_list,
                'df': self.df,
                'df_3m': self.df_3m,
                'df_5m': self.df_5m,
                'df_15m': self.df_15m,
                'df_1H': self.df_1H,
                'df_1D': self.df_1D
            }
            
            self.parent.add_strategy_widget(self.filepath, ohlcv_data)
            self.parent.ui.Run_Backtest_Button.setEnabled(True)

    def script_editor(self):
        if self.filepath:
            with open(self.filepath, 'r') as file:
                code = file.read()
                self.parent.ui.script_editor_textedit.setPlainText(code)

    def save_file(self):
        """Save the file after editing"""
        if self.filepath:
            with open(self.strategy_file_path, 'w') as file:
                file.write(self.parent.ui.script_editor_textedit.toPlainText())

    def save_file_as(self):
        """Save the content to a new file chosen by the user"""
        if self.filepath:
            new_file_path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Python Files (*.py)")
            if new_file_path:
                self.filepath = new_file_path
                with open(self.filepath, 'w') as file:
                    file.write(self.parent.ui.script_editor_textedit.toPlainText())
                print(f"File saved as: {self.filepath}")
    # Add Indicators
    
    # Edit strategy