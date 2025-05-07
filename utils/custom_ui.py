from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QDate
from .app_ui import Ui_Dreamtester

class CustomUiDreamtester(QMainWindow, Ui_Dreamtester):
    def __init__(self, parent=None, backtester=None):
        super().__init__(parent)
        self.backtester = backtester
        self.setupUi(self)
        self.custom_setup()

    def custom_setup(self):
        # Add your custom setup code here
        self.Import_Strategy_Button.clicked.connect(self.backtester.edit_strategy)
        self.Run_Backtest_Button.setEnabled(False)
        self.Trade_Results_Button.setEnabled(False)
        self.Run_Backtest_Button.clicked.connect(lambda: self.backtester.start_backtest(type='backtest'))
        self.clear_strategies_button.clicked.connect(self.backtester.clear_strategies)