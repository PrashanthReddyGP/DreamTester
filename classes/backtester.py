import os
from datetime import datetime
import threading
from queue import Queue

from numba import njit
import pandas as pd
import numpy as np
from scipy.optimize import fsolve

import matplotlib
matplotlib.use('QtAgg')  # Use the QtAgg backend, which works with PySide6
from matplotlib.backends.qt_compat import QtCore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PySide6.QtCore import QDate, QThread, QSize, Qt, QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QHBoxLayout, QVBoxLayout, QCheckBox, QLabel, QLineEdit, QPushButton, QHeaderView, QTableWidgetItem, QTableWidget, QTextEdit, QFileDialog, QMessageBox, QWidgetItem

from utils import app_ui # import app_ui.py file from utils folder
from utils.custom_ui import CustomUiDreamtester
from utils.custom_ml_features_ui import CustomUiMLFeatures
from files import indicators # import indicators.py file from files folder
from . import backtest_worker # Import backtest_worker.py from the current folder
from . import strategy_window # Import strategy_window.py from the current folder
from . import machine_learning
import main

class Backtester(QMainWindow):
    def __init__(self, client, parent=None):
        super().__init__(parent)
        
        self.client = client
        self.ui = CustomUiDreamtester(parent=self, backtester=self)
        self.ml_ui = CustomUiMLFeatures(parent=self)
        self.ui.setupUi(self)
        self.ml_ui.setupUi()
        self.idk = indicators.Indicators()
        self.loaded_data = None
        self.batch_size = 1000
        self.widget_list = []
        self.entry_list = []
        self.exit_list = []
        self.equityWidgetList = []
        self.strategies_filepaths = []
        self.strategiesWidgetList = []
        self.strategy_file_path = None
        self.ui.Import_Strategy_Button.clicked.connect(self.edit_strategy)
        self.ui.Run_Backtest_Button.setEnabled(False)
        self.ui.Trade_Results_Button.setEnabled(False)
        self.ui.Run_Backtest_Button.clicked.connect(lambda: self.start_backtest(type='backtest'))
        self.ui.clear_strategies_button.clicked.connect(self.clear_strategies)
        
        self.machine_learning = machine_learning.MachineLearning(self)
        
        self.showMaximized()

    def start_backtest(self, type, threshold = 1, row = 1, above_thresholds = []):
        
        capital = int(self.ui.Initial_Capital_Input.text())
        
        worker = backtest_worker.BacktestWorker(self)
        
        result_queue = Queue()
        
        # Move the worker to the thread
        worker_thread = threading.Thread(target = worker.run_backtest(capital, self.strategies_filepaths, self.strategiesWidgetList, type, threshold, row, above_thresholds, result_queue))
        
        worker_thread.start()
        
        above_thresholds = result_queue.get()
        
        return above_thresholds
    
    def on_backtest_finished(self, strategiesList, initial_capital):
        
        self.ui.Trade_Results_Button.setEnabled(True)
        self.ui.Trade_Results_Button.clicked.connect(lambda: self.trade_results(strategiesList, initial_capital))
    
    def update_timer(self):
        self.elapsed_time += 1
        self.label_elapsed.setText(f"Elapsed Time: {self.elapsed_time}s")

    def set_progress(self, value):
        self.progress_bar.setValue(value)

        # Calculate the estimated remaining time
        if value > 0:
            elapsed_seconds = self.elapsed_time
            total_time_estimated = (elapsed_seconds / value) * 100  # Total time estimate based on progress
            remaining_time = total_time_estimated - elapsed_seconds  # Remaining time estimate
            self.label_estimated.setText(f"Estimated Time: {int(remaining_time)}s")
        else:
            self.label_estimated.setText("Estimated Time: Calculating...")

        
    def populate_symbols(self, widget):
        
        """Fetch and populate the combo box with sorted Binance Futures symbols."""
        
        try:
            # Fetch all symbols from Binance USDⓈ-M Futures
            futures_exchange_info = self.client.exchange_info()
            symbols = [symbol['symbol'] for symbol in futures_exchange_info['symbols'] if symbol['status'] == 'TRADING']
            
            # Sort symbols alphabetically
            sorted_symbols = sorted(symbols)
            
            # Add sorted symbols to the combo box
            widget.addItems(sorted_symbols)
            
        except Exception as e:
            print(f"Error fetching symbols: {e}")
            
    def populate_timeframes(self, widget):
        
        """Populate the combo box with available Binance-supported timeframes."""
        
        timeframes = [
            "1m", "3m", "5m", "15m", "30m",
            "1h", "2h", "4h", "6h", "8h", "12h",
            "1d", "3d", "1w", "1M"
        ]

        # Add timeframes to the combo box
        widget.addItems(timeframes)

    def download_ohlcv_data(self, symbolWidget, timeframeWidget, stratdateWidget, enddateWidget):
        
        symbol = symbolWidget.currentText()  # Get the selected symbol
        timeframe = timeframeWidget.currentText()  # Get the selected timeframe
        start_date = stratdateWidget.date()    # Get start date
        end_date = enddateWidget.date()    # Get end date
        
        # Convert QDate to integers for datetime
        start_time = int(datetime(start_date.year(), start_date.month(), start_date.day(), 0, 0, 0).timestamp() * 1000)
        end_time = int(datetime(end_date.year(), end_date.month(), end_date.day(), 23, 59, 0).timestamp() * 1000)

        ## Cache the data ##
        cache_file_path = os.path.join('data', f'{symbol}_{timeframe}_ohlcv_data.parquet')

        # Initialize an empty DataFrame to hold all data
        df_combined = pd.DataFrame()
        
        # Check if the cache file exists
        if os.path.exists(cache_file_path):
            
            # Read cached data
            cached_df = pd.read_parquet(cache_file_path)

            # Convert to pydatetime
            earliest = cached_df['timestamp'].iloc[0].to_pydatetime()
            latest = cached_df['timestamp'].iloc[-1].to_pydatetime()
            
            # Find the earliest and most recent timestamps in the cached data (milliseconds)
            earliest_cached_timestamp = int(earliest.timestamp() * 1000)
            latest_cached_timestamp = int(latest.timestamp() * 1000)
            
            # Filter cached data within the desired range
            filtered_cached_df = cached_df[(cached_df['timestamp'] >= datetime(start_date.year(), start_date.month(), start_date.day(), 0, 0, 0)) & 
                                            (cached_df['timestamp'] <= datetime(end_date.year(), end_date.month(), end_date.day(), 23, 59, 0))]

            # Initialize combined DataFrame with the filtered cached data
            df_combined = filtered_cached_df.copy()
            df_save = cached_df
            
            # Fetch missing data before the cached data (if start_time is before the cached range)
            if start_time < earliest_cached_timestamp:
                df_before = self.fetch_and_save_ohlcv_data(symbol, timeframe, start_time, earliest_cached_timestamp - 1)
                if not df_before.empty:  # Ensure df_before is not empty
                    df_combined = pd.concat([df_combined, df_before], ignore_index=True)
                    df_save = pd.concat([cached_df, df_before], ignore_index=True)
            
            # Fetch missing data after the cached data (if end_time is after the cached range)
            if end_time > latest_cached_timestamp:
                df_after = self.fetch_and_save_ohlcv_data(symbol, timeframe, latest_cached_timestamp + 1, end_time)
                if not df_after.empty:  # Ensure df_after is not empty
                    df_combined = pd.concat([df_combined, df_after], ignore_index=True)
                    df_save = pd.concat([cached_df, df_after], ignore_index=True)
            
            # Sort the data by timestamp to ensure it's in chronological order
            df_combined = df_combined.sort_values(by='timestamp').reset_index(drop=True)

            # Save the combined data back to the cache file
            df_save = df_save.sort_values(by='timestamp').reset_index(drop=True)
            df_save.to_parquet(cache_file_path, index=False, engine='pyarrow')

        else:
            # No cache exists, download all data
            df_combined = self.fetch_and_save_ohlcv_data(symbol, timeframe, start_time, end_time)

            # Save the newly downloaded data to the cache
            df_combined.to_parquet(cache_file_path, index=False, engine='pyarrow')
        
        # Ensure that all columns are numeric in one step using vectorized operation
        df_combined[['open', 'high', 'low', 'close', 'volume']] = df_combined[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric, errors='coerce')

        # self.df = df_combined
        
        df_combined.set_index('timestamp', inplace=True)
        df_3m = df_combined.resample('3min').agg({
            'open':'first',
            'high':'max',
            'low':'min',
            'close':'last',
            'volume':'sum'})
        df_5m = df_combined.resample('5min').agg({
            'open':'first',
            'high':'max',
            'low':'min',
            'close':'last',
            'volume':'sum'})
        df_15m = df_combined.resample('15min').agg({
            'open':'first',
            'high':'max',
            'low':'min',
            'close':'last',
            'volume':'sum'})
        df_1H = df_combined.resample('60min').agg({
            'open':'first',
            'high':'max',
            'low':'min',
            'close':'last',
            'volume':'sum'})
        df_1D = df_combined.resample('1D').agg({
            'open':'first',
            'high':'max',
            'low':'min',
            'close':'last',
            'volume':'sum'})
        
        df_3m.reset_index(inplace=True)
        df_5m.reset_index(inplace=True)
        df_15m.reset_index(inplace=True)
        df_1H.reset_index(inplace=True)
        df_1D.reset_index(inplace=True)

        df_combined.reset_index(inplace=True)
        
        return df_combined, df_3m, df_5m, df_15m, df_1H, df_1D
        
    # EXTENDED OHLCV DATA
    def fetch_ohlcv_paginated(self, symbol, timeframe, start_time, end_time, limit=1000):
        all_ohlcv = []
        
        while True:
            try:
                ohlcv = self.client.klines(symbol, timeframe, startTime=start_time, endTime=end_time, limit=limit)
                if not ohlcv:
                    break
                all_ohlcv.extend(ohlcv)
                start_time = ohlcv[-1][0] + 1  # Increment to the next millisecond
                if len(ohlcv) < limit:
                    break
            except Exception as e:
                print(f"Error fetching data: {e}")
                break
        return all_ohlcv

    # LIMITED OHLCV DATA
    def fetch_and_save_ohlcv_data(self, symbol, timeframe, start_time, end_time):
        
        ohlcv = self.fetch_ohlcv_paginated(symbol, timeframe, start_time, end_time)
        
        df = pd.DataFrame(ohlcv, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume', 
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        
        df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Vancouver').dt.tz_localize(None)
        
        return df
    
    def plot_candlestick(self, df, symbol):
        
        """Plot the candlestick chart with dynamic data loading."""
        
        self.df = df.drop_duplicates(subset = 'timestamp', keep = 'last')  # Full dataset

        self.loaded_data = self.df.tail(self.batch_size)  # Load the most recent batch
        df = self.loaded_data.copy()
        
        # Prepare the data as before
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M')
        df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']].copy()
        df.rename(columns={'timestamp': 'date'}, inplace=True)
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        
        # Convert DataFrame to JavaScript-friendly format
        chart_data = df.to_dict(orient='records')
        for data_point in chart_data:
            # Convert datetime string to timestamp (Unix time)
            data_point['time'] = int(pd.to_datetime(data_point['date']).timestamp())  # Keep the timestamp in seconds
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Candlestick Chart</title>
            <!-- Correctly loading the external Lightweight Charts library -->
            <script src="https://cdn.jsdelivr.net/npm/lightweight-charts@3.6.0/dist/lightweight-charts.standalone.production.js"></script>
            <style>
                html, body {{
                    margin: 0;
                    padding: 0;
                    height: 100%;
                    width: 100%;
                    background-color: #131722;  /* Match background color with the chart's */
                    overflow: hidden;  /* Prevent scrollbars */
                }}
                
                #chart {{
                    width: 100%;
                    height: 100%;
                }}
            </style>
        </head>
        <body>
            <div id="chart"></div>
            <script>
                // Ensure the chart is created after the script is loaded
                window.onload = function() {{
                    const chartData = {chart_data};  // Embed data from the DataFrame
                    
                    // Custom priceFormatter function to format price labels
                    const priceFormatter = (price) => {{
                        // Adjust decimal places based on the price value
                        if (price > 1) {{
                            return price.toFixed(2); // Show 2 decimal places for prices > 1
                        }} 
                        else if (price > 0.1) {{
                            return price.toFixed(3); // Show 3 decimal places for prices between 0.1 and 1
                        }} 
                        else {{
                            return price.toFixed(4); // Show 4 decimal places for prices <= 0.1
                        }}
                    }};
                    
                    const chart = LightweightCharts.createChart(document.getElementById('chart'), {{
                        width: document.getElementById('chart').clientWidth,
                        height: document.getElementById('chart').clientHeight,
                        layout: {{
                            backgroundColor: '#131722',
                            textColor: '#d1d4dc'
                        }},
                        grid: {{
                            vertLines: {{ color: '#2B2B43' }},
                            horzLines: {{ color: '#2B2B43' }}
                        }},
                        priceScale: {{
                            borderVisible: false,  // Hide border to prevent overflow
                            scaleMargins: {{
                                top: 0.1,
                                bottom: 0.1
                            }},  // Add margins to fit within the widget
                            priceFormatter: priceFormatter  // Use custom price formatting function
                        }},
                        timeScale: {{
                            borderVisible: false,  // Hide border to prevent overflow
                            rightOffset: 12,  // Adds space to the right to fit the time labels
                            fixLeftEdge: true,  // Prevents left side from cutting off labels
                            timeVisible: true,                 // Show hours and minutes
                            secondsVisible: false,             // Hide seconds (optional, since candlesticks are minute-based)
                        }},
                        crosshair: {{
                            vertLine: {{ color: '#758696', width: 1 }},
                            horzLine: {{ color: '#758696', width: 1 }},
                            mode: LightweightCharts.CrosshairMode.Normal,
                        }},
                        watermark: {{
                            visible: true,
                            fontSize: 30,
                            color: 'rgba(255, 255, 255, 0.1)',
                            text: '{symbol}',
                            horzAlign: 'center',
                            vertAlign: 'center',
                        }}
                    }});
                    
                    chart.addCandlestickSeries().setData(chartData);
                    
                    window.onresize = function() {{
                        chart.resize(document.getElementById('chart').clientWidth, document.getElementById('chart').clientHeight);
                    }};
                }};
            </script>
        </body>
        </html>
        """
        
        # Save Plotly figure as HTML, including custom CSS and Plotly JS
        # Get the current working directory
        current_dir = os.getcwd()

        # Define the temp folder path
        temp_dir = os.path.join(current_dir, 'temp')

        # Check if the temp directory exists, if not, create it
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # Define the file path inside the temp folder
        file_path = os.path.join(temp_dir, 'candlestick_plot.html')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Clear the layout and add the Plotly chart
        layout = self.ui.Ohlcv_Chart_Group.layout()  # Get the layout of the Ohlcv_Chart_Group
        
        # Display Plotly chart in QWebEngineView
        webview = QWebEngineView()
        
        for i in reversed(range(layout.count())):  # Clear existing widgets in the layout
            layout.itemAt(i).widget().deleteLater()
        
        layout.addWidget(webview)  # Add the webview with the Plotly chart
        with open(file_path, 'r', encoding='utf-8') as f:
            webview.setHtml(f.read())
        # webview.setHtml(open(file_path).read())
        
    def populate_indicators(self):
        
        """Populate the combo box with available indicators."""
        
        indicators = [
            "SELECT", "EMA", "RSI", "ATR", "SMA", "HMA", "WMA", "AMA", "MACD", "STOCASTIC RSI", "ADX", "CCI", "AROON",
            "WILLIAMS RANGE", "HL OSCILLATOR", "VWAP", "BOLLINDER BANDS", "MOMENTUM", "OBV", "EMA-CLOSE DISTANCE", 
            "RATE OF CHANGE", "ICHIMOKU", "PSAR", "SUPERTREND", "PIVOT POINTS", "DONCHIAN CHANNELS", "HEIKIN ASHI", 
            "CANDLESTICK PATTERNS", "SMA SLOPE", 'HH LL', 'VIX', 'MARKET REGIME', "LAG OHLCV", 'DATETIME SPLIT',
            'CANDLE LENGTH', 'PRICE MOVEMENT'
        ]
        
        timeframes = [
            "1m", "3m", "5m", "15m", "30m",
            "1h", "2h", "4h", "6h", "8h", "12h",
            "1d", "3d", "1w", "1M"
        ]

        # Add timeframes to the combo box
        self.I_Name_Combo.addItems(indicators)
        self.I_Timeframe_Combo.addItems(timeframes)
    
        return indicators
    
    def create_indicator_widget(self, I_Holder, I_Holder_Layout):
        
        # Check if the layout contains any QLabel
        has_label = False
        
        for i in range(I_Holder_Layout.count()):
            widget = I_Holder_Layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                has_label = True
                break  # Stop the loop since we only need to know if a QLabel exists
            
        if has_label:
            for i in reversed(range(I_Holder_Layout.count())):  # Clear existing widgets in the layout
                item = I_Holder_Layout.takeAt(i)  # Remove the widget from the layout
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()  # Safely delete the widget later
        
        I_Holder.setLayout(I_Holder_Layout)
        I_Holder_Layout.setAlignment(Qt.AlignTop)  # Apply top vertical alignment to the layout
        
        self.I_Widget = QWidget(I_Holder)
        self.I_Widget.setObjectName(u"I_Widget")
        self.I_Widget.setMaximumSize(QSize(16777215, 50))
        
        self.horizontalLayout_10 = QHBoxLayout(self.I_Widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        
        self.I_Selection_Button = QCheckBox(self.I_Widget)
        self.I_Selection_Button.setObjectName(u"I_Selection_Button")
        self.I_Selection_Button.setMinimumSize(QSize(30, 30))
        self.I_Selection_Button.setMaximumSize(QSize(30, 30))
        self.I_Selection_Button.setBaseSize(QSize(30, 30))
        self.I_Selection_Button.setIconSize(QSize(30, 30))
        self.I_Selection_Button.setChecked(True)

        self.horizontalLayout_10.addWidget(self.I_Selection_Button)
        
        self.I_Name_Combo = QComboBox(self.I_Widget)
        self.I_Name_Combo.setObjectName(u"I_Name_Combo")
        self.I_Name_Combo.setMinimumSize(QSize(75, 30))
        self.I_Name_Combo.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.I_Name_Combo.setEditable(False)
        self.I_Name_Combo.setCurrentText("")
        self.I_Name_Combo.currentIndexChanged.connect(self.insertDefaultValues)
        
        self.horizontalLayout_10.addWidget(self.I_Name_Combo)
        
        self.I_Timeframe_Combo = QComboBox(self.I_Widget)
        self.I_Timeframe_Combo.setObjectName(u"I_Timeframe_Combo")
        self.I_Timeframe_Combo.setMinimumSize(QSize(75, 30))
        self.I_Timeframe_Combo.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.I_Timeframe_Combo.setEditable(False)
        self.I_Timeframe_Combo.setCurrentText("")
        self.I_Timeframe_Combo.currentIndexChanged.connect(self.insertDefaultValues)
        
        self.horizontalLayout_10.addWidget(self.I_Timeframe_Combo)
        
        self.I_Variable_Text = QLineEdit(self.I_Widget)
        self.I_Variable_Text.setObjectName(u"I_Variable_Text")
        self.I_Variable_Text.setMinimumSize(QSize(0, 30))
        self.I_Variable_Text.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                        "border-color: rgb(74, 74, 74);\n"
                                        "")
        self.I_Variable_Text.setPlaceholderText(QCoreApplication.translate("Backtester", u"Enter required values...", None))

        self.horizontalLayout_10.addWidget(self.I_Variable_Text)

        self.I_Delete_Button = QPushButton(self.I_Widget)
        self.I_Delete_Button.setObjectName(u"I_Delete_Button")
        self.I_Delete_Button.setMinimumSize(QSize(30, 30))
        self.I_Delete_Button.setMaximumSize(QSize(30, 30))
        self.I_Delete_Button.setBaseSize(QSize(29, 30))
        self.I_Delete_Button.setStyleSheet(u"QPushButton {\n"
                                        "border: none;  /* Removes the border */\n"
                                        "background-color: rgb(90, 90, 90);  /* Default background color */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(80, 80, 80);  /* Background color when hovered */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "background-color: #353535;  /* Background color when pressed */\n"
                                        "}")
        
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditClear))
        self.I_Delete_Button.setIcon(icon1)
        self.I_Delete_Button.setIconSize(QSize(15, 15))
        
        self.horizontalLayout_10.addWidget(self.I_Delete_Button)
        self.I_Delete_Button.clicked.connect(lambda checked, currentWidget=self.I_Widget: self.remove_indicator_widget(currentWidget, I_Holder, I_Holder_Layout))

        self.I_Delete_Button.setText("")

        return self.I_Widget, self.I_Selection_Button, self.I_Name_Combo, self.I_Timeframe_Combo, self.I_Variable_Text
    
    def insertDefaultValues(self, index):
        
        if index == 0:
            self.I_Variable_Text.setPlaceholderText("Choose an Indicator")
        elif index == 1:
            self.I_Variable_Text.setText("200")
        elif index == 2:
            self.I_Variable_Text.setText("14")
        elif index == 8:
            self.I_Variable_Text.setText("12, 26, 9")
    
    def add_indicator_widget(self, I_Contents_Container, I_Holder_Layout, widget_list):
        
        new_widget, check_box, combo_box, cbox2, string = self.create_indicator_widget(I_Contents_Container, I_Holder_Layout)
        
        widget_list.append((new_widget, check_box, combo_box, cbox2, string))
        
        I_Holder_Layout.insertWidget(I_Holder_Layout.count(), new_widget)
        
        self.populate_indicators()
        
        return combo_box, cbox2, string, widget_list
    
    def remove_indicator_widget(self, currentWidget, I_Holder, I_Holder_Layout):
        
        # Safely remove and delete the widget
        for widget, check_box, combo_box, cbox2, string in self.widget_list:
            if widget == currentWidget:
                # Remove the widget from the layout and delete it
                I_Holder_Layout.removeWidget(widget)
                widget.deleteLater()
                self.widget_list.remove((widget, check_box, combo_box, cbox2, string))  # Remove it from our tracking list
                
                if self.widget_list == []:
                    
                    # Clear the layout and add the Plotly chart
                    I_Holder_Layout = I_Holder.layout()  # Get the layout of the Ohlcv_Chart_Group
                    
                    # Set the layout alignment to top vertical alignment
                    I_Holder.setLayout(I_Holder_Layout)  # Reset the layout to the container
                    I_Holder_Layout.setAlignment(Qt.AlignHCenter & Qt.AlignVCenter)  # Apply top vertical alignment to the layout
                    
                    self.label_2 = QLabel(self.ui.I_Contents_Container)
                    self.label_2.setObjectName(u"label_2")
                    self.label_2.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                                "color: rgb(130, 130, 130);")
                    self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

                    I_Holder_Layout.addWidget(self.label_2, 0)
                    self.label_2.setText(QCoreApplication.translate("Dream_Machine", u"Indicator goes here", None))
    
    # INDICATORS CONTENT START #
    
    def indicator_verification(self, widget_list, df, df_3m, df_5m, df_15m, df_1H, df_1D):
        
        if df is not None:
            
            df = df.copy()
            
            # Iterate through all the tracked widgets and return combobox selections
            for widget, check_box, combo_box, cbox2, string in widget_list:
                
                selected_indicator = combo_box.currentText()
                selected = check_box.isChecked()
                timeframe = cbox2.currentText()

                if selected:
                    
                    # Assuming you have a QLineEdit named self.I_Variable_Text
                    user_input = string.text()  # Get the text from the QLineEdit

                    # Split the input string by commas and strip any whitespace
                    values = [value.strip() for value in user_input.split(',')]

                    if selected_indicator == 'EMA':
                        
                        # Ensure you have only 1 value
                        if len(values) == 1:
                            # Convert the first three values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            df = self.idk.calculate_ema(df, length)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"EMA takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'WMA':
                        
                        # Ensure you have only 1 value
                        if len(values) == 1:
                            # Convert the first three values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            df = self.idk.calculate_wma(df, length)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"WMA takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'SMA':

                        # Ensure you have only 1 value
                        if len(values) == 1:
                            
                            # Convert the first three values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            
                            if timeframe == '1m':
                                df = self.idk.calculate_sma(df, length)
                            elif timeframe == '3m':
                                df_3m = self.idk.calculate_sma(df_3m, timeframe, length)
                                df = df.merge(df_3m[['timestamp', f'{timeframe}_SMA_{length}']], how='left', on='timestamp')
                                df[f'{timeframe}_SMA_{length}'] = df[f'{timeframe}_SMA_{length}'].ffill()
                            elif timeframe == '5m':
                                df_5m = self.idk.calculate_sma(df_5m, length)
                                df = df.merge(df_5m[['timestamp', f'sma_{length}']], how='left', on='timestamp')
                                df[f'sma_{length}'] = df[f'sma_{length}'].ffill()
                            elif timeframe == '15m':
                                df_15m = self.idk.calculate_sma(df_15m, length)
                                df = df.merge(df_15m[['timestamp', f'sma_{length}']], how='left', on='timestamp')
                                df[f'sma_{length}'] = df[f'sma_{length}'].ffill()
                            elif timeframe == '1h':
                                df_1h = self.idk.calculate_sma(df_1H, timeframe, length)
                                df = df.merge(df_1h[['timestamp', f'{timeframe}_SMA_{length}']], how='left', on='timestamp')
                                df[f'{timeframe}_SMA_{length}'] = df[f'{timeframe}_SMA_{length}'].ffill()
                            elif timeframe == '1d':
                                df_1d = self.idk.calculate_sma(df_1D, timeframe, length)
                                df = df.merge(df_1d[['timestamp', f'{timeframe}_SMA_{length}']], how='left', on='timestamp')
                                df[f'{timeframe}_SMA_{length}'] = df[f'{timeframe}_SMA_{length}'].ffill()
                                
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"SMA takes 1 Input Value, But {len(values)} were given...")
                        
                    if selected_indicator == 'RSI':
                        
                        # Ensure you have only 1 value
                        if len(values) == 1:
                            # Convert the first three values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            df = self.idk.calculate_rsi(df, length)
                            
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"RSI takes 1 Input Value, But {len(values)} were given...")
                        
                    if selected_indicator == 'STOCASTIC RSI':
                        
                        # Ensure you have only 1 value
                        if len(values) == 2:
                            # Convert the first three values to integers (or float, as needed)
                            k = int(values[0])  # or float(values[0]) if you need float
                            d = int(values[1])
                            df = self.idk.calculate_stocastic(df, k, d)
                            
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"STOCASTIC RSI takes 2 Input Value, But {len(values)} were given...")
                        
                    if selected_indicator == 'MACD':
                        
                        # Ensure you have at least 3 values
                        if len(values) == 3:
                            # Convert the first three values to integers (or float, as needed)
                            short_window = int(values[0])  # or float(values[0]) if you need float
                            long_window = int(values[1])  # or float(values[1]) if you need float
                            signal_window = int(values[2])  # or float(values[2]) if you need float
                            
                            df = self.idk.calculate_macd(df, short_window, long_window, signal_window)
                                                
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"MACD takes 3 Input Values, But {len(values)} were given...")
                            
                    if selected_indicator == 'BOLLINDER BANDS':
                        
                        # Ensure you have only 1 value
                        if len(values) == 2:
                            
                            # Convert the first three values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            deviation = int(values[1])
                            
                            if timeframe == '1m':
                                df = self.idk.calculate_bollinger_bands(df, timeframe, length, deviation)
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"BOLLINGER BANDS takes 2 Input Values, But {len(values)} were given...")
                    
                    if selected_indicator == 'ATR':
                        
                        # Ensure you have at least 2 values
                        if len(values) == 2:
                            # Convert the first two values to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            multiplier = float(values[1])  # or float(values[1]) if you need float
                            
                            df = self.idk.calculate_stop_loss(df, length, multiplier)
                        
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"ATR takes 2 Input Values, But {len(values)} were given...")
                            
                    if selected_indicator == 'SUPERTREND':
                        
                        # Ensure you have at least 2 values
                        if len(values) == 2:
                            # Convert the first two values to integers (or float, as needed)
                            period = int(values[0])  # or float(values[0]) if you need float
                            multiplier = float(values[1])  # or float(values[1]) if you need float
                            
                            df = self.idk.supertrend(df, period, multiplier)
                        
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"SUPERTREND takes 2 Input Values, But {len(values)} were given...")
                            
                    if selected_indicator == 'CCI':
                        
                        if len(values) == 1:
                            
                            length = int(values[0])
                            
                            df = self.idk.calculate_cci(df, length)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"CCI takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'AROON':
                        
                        if len(values) == 1:
                            
                            period = int(values[0])
                            
                            df = self.idk.calculate_aroon(df, period)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"AROON takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'WILLIAMS RANGE':
                        
                        if len(values) == 1:
                            
                            period = int(values[0])
                            
                            df = self.idk.williams_range(df, period)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"WILLIAMS RANGE takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'HL OSCILLATOR':
                        
                        if len(values) == 1:
                            
                            period = int(values[0])
                            
                            df = self.idk.calculate_hl_oscillator(df, period)
                            
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"HL OSCILLATOR takes 1 Input Value, But {len(values)} were given...")
                    
                    if selected_indicator == 'SMA SLOPE':
                        
                        # Ensure you have at least 3 values
                        if len(values) == 3:
                            # Convert the first value to integers (or float, as needed)
                            length = int(values[0])  # or float(values[0]) if you need float
                            smoothBars = int(values[1])  # or float(values[0]) if you need float
                            neutralZoneHeight = int(values[2])  # or float(values[0]) if you need float
                            
                            df = self.idk.calculate_sma_slope(df, length, smoothBars, neutralZoneHeight)
                            
                        else:
                            
                            string.setText('')
                            string.setPlaceholderText(f"EMA Slope takes 3 Input Values, But {len(values)} were given...")
                    
                    if selected_indicator == 'CANDLESTICK PATTERNS':
                        
                        df = self.idk.identify_candlestick_patterns(df)
                    
                    if selected_indicator == 'HH LL':
                        
                        if len(values) == 1:
                            period = int(values[0])
                            df = self.idk.hh_ll(df, period)
                        else:
                            string.setText('')
                            string.setPlaceholderText(f"HH LL takes 1 Input Value, But {len(values)} were given...")
                            
                    if selected_indicator == 'MARKET REGIME':
                        
                        df = self.idk.calculate_market_regime(df)
                        
                    if selected_indicator == 'PIVOT POINTS':
                        
                        df = self.idk.pivot_points(df)
                        
                    if selected_indicator == 'LAG OHLCV':
                        
                        if len(values) == 1:
                            lag = int(values[0])
                            df = self.idk.lag_ohlcv(df, lag)
                        else:
                            string.setText('')
                            string.setPlaceholderText(f'LAG OHLCV takes 1 input value, But {len(values)} were given')
                            
                    if selected_indicator == 'DATETIME SPLIT':
                        
                        df = self.idk.datetime_split(df)
                    
                    if selected_indicator == 'CANDLE LENGTH':
                        
                        df = self.idk.candle_lengths(df)
                    
                    if selected_indicator == 'PRICE MOVEMENT':
                        
                        df = self.idk.price_movement(df)
            
            df_tail = df.tail(20)
            self.display_dataframe(df_tail)
            
            return df
            
        else:
            self.display_error()
    def display_dataframe(self, df):

        df_layout = self.ui.widget_4.layout()
        
        for i in reversed(range(df_layout.count())):  # Clear existing widgets in the layout
            df_layout.itemAt(i).widget().deleteLater()
        
        # Table widget to display DataFrame
        self.table_widget = QTableWidget()
        
        # Set table rows and columns based on DataFrame shape
        self.table_widget.setRowCount(df.shape[0])
        self.table_widget.setColumnCount(df.shape[1])
        
        # Set the column headers
        self.table_widget.setHorizontalHeaderLabels(df.columns)
        
        # Fill the table with data from the DataFrame
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                # Set the alignment for each item to be horizontally and vertically centered
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table_widget.setItem(row, col, item)
        
        # Make the columns sortable
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_widget.setSortingEnabled(True)
        
        # Make the columns resizable by the user
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        
        # Resize columns and rows to fit contents
        self.table_widget.resizeColumnsToContents()
        
        # Now double the size of each column
        for col in range(self.table_widget.columnCount()):
            new_width = self.table_widget.columnWidth(col) * 1.5  # Double the width
            self.table_widget.setColumnWidth(col, new_width)
            
        # Align column headers
        self.table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Align row headers (if using row labels)
        self.table_widget.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the background color of the table to rgb(62, 62, 62)
        self.table_widget.setStyleSheet("QTableWidget { background-color: rgb(62, 62, 62); border:none}")

        df_layout.addWidget(self.table_widget)
        self.setLayout(df_layout)

    def display_error(self):
        
        # Clear the layout and add the Plotly chart
        output_Layout = self.ui.widget_4.layout()  # Get the layout of the Ohlcv_Chart_Group
        
        for i in reversed(range(output_Layout.count())):  # Clear existing widgets in the layout
            output_Layout.itemAt(i).widget().deleteLater()
        
        self.selection_label = QLabel(self.ui.widget_4)
        output_Layout.addWidget(self.selection_label)
        self.selection_label.setText("No Ohlcv data available")
        
        self.selection_label.setObjectName(u"selection_label")
        self.selection_label.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                    "color: rgb(130, 130, 130);")
        self.selection_label.setAlignment(Qt.AlignmentFlag.AlignCenter)


    # INDICATORS CONTENT END #

    def plot_results(self, strategiesList, intCapital):
        
        # Clear the layout and add the Plotly chart
        equity_Layout = self.ui.Equity_Chart_Groupbox.layout()  # Get the layout of the Ohlcv_Chart_Group
        equity_Layout.setContentsMargins(10, 10, 10, 10)  # Set margins (left, top, right, bottom) 
            
        for i in reversed(range(equity_Layout.count())):  # Clear existing widgets in the layout
            equity_Layout.itemAt(i).widget().deleteLater()
        
        # Create a new canvas to hold the plot if not already present
        canvas = FigureCanvas(Figure(figsize=(16, 9), facecolor='#2E2E2E'))  # New canvas with dark background
        equity_Layout.addWidget(canvas)  # Add the new canvas to the layout
        
        # Clear the previous figure
        canvas.figure.clear()
        
        # Set the dark background for the figure and axes
        plt.style.use('dark_background')  # Apply dark background style globally
        canvas.figure.patch.set_facecolor('#2E2E2E')  # Dark figure background

        # Create axes for plotting
        ax1 = canvas.figure.add_subplot(111)  # Equity curve
        
        # List of colors to be used for plotting different strategies
        colors = [
            '#88B04B', '#FF6F61', '#6B5B95', '#F7CAC9', '#92A8D1', '#955251',
            '#B565A7', '#009B77', '#DD4124', '#45B8AC', '#EFC050', '#5B5EA6'
        ]

        # Store drawdown results for each strategy
        drawdown_data = {}
        
        # Initialize an empty list to store the reformatted data
        formatted_data = []

        # Define a list of months to be used as headers
        month_headers = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

        # Loop through the list of equity data arrays and plot each one
        for i, strategy in enumerate(strategiesList):
            strategy_name = strategy['strategy_name']  # Access the strategy name
            equity_data = strategy['equity']  # Access the equity data
            equity_data = np.array(equity_data)
            df = strategy['ohlcv']  
            color = colors[i % len(colors)]  # Cycle colors if more strategies than colors
            
            ###########################################
            
            # Convert timestamps to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

            # Create a new column for year and month
            df['year'] = df['timestamp'].dt.year
            df['month'] = df['timestamp'].dt.month

            # Calculate monthly returns for each year
            monthly_returns = []
            
            for (year, month), group in df.groupby(['year', 'month']):
                
                start_equity = equity_data[group.index[0]]  # First day's equity
                
                # Find the last valid index in the equity data, constrained by the size of equity_data
                last_index = min(group.index[-1], len(equity_data) - 1)  # Safely access the last available index
                end_equity = equity_data[last_index]  # Use last available equity in the current group
                
                monthly_return = ((end_equity - start_equity) / start_equity) * 100  # Percentage return
                monthly_return = round(monthly_return, 2)  # Round to 2 decimal places
                monthly_returns.append({'year': year, 'month': month, 'return': monthly_return})

            # Pivot the data to have months as columns and years as rows
            return_df = pd.DataFrame(monthly_returns).pivot(index='year', columns='month', values='return')

            # Ensure the month headers are consistent and in the correct order
            return_df.columns = [month_headers[m-1] for m in return_df.columns]

            # Reindex the DataFrame to include all months, even if some are missing
            return_df = return_df.reindex(columns=month_headers)

            # Add the strategy name to the first column
            return_df.insert(0, 'Strategy', strategy_name)

            # Append this strategy's returns to the final data list
            formatted_data.append(return_df)
            
            ###########################################
            
            # Plot the equity curve
            ax1.plot(df['timestamp'], (equity_data - intCapital), label=f"{strategy_name}", color=color, zorder=3)
            
            # Calculate drawdown for this strategy
            peaks = np.maximum.accumulate(equity_data)
            drawdowns = (equity_data - peaks) / peaks * 100  # Drawdowns in percentage
            drawdown_data[strategy_name] = {'timestamp': df['timestamp'], 'drawdown': drawdowns}
            
        ##########################################################
        # Concatenate the results for all strategies
        final_df = pd.concat(formatted_data)
        
        # Reset the index to turn the year into a column
        final_df.reset_index(inplace=True)
        
        # Export the final DataFrame to Excel
        final_df.to_excel('output/formatted_monthly_returns.xlsx', sheet_name='Returns', index=False)
        
        # Optionally, print the final DataFrame to the console
        # print(final_df)
        ##########################################################
        # Plot horizontal line at y=0
        ax1.axhline(y=0, color='white', linestyle='--', linewidth=1, alpha=0.1, zorder=-2)

        ax1.legend(loc='upper left')
        ax1.set_facecolor('#2E2E2E')  # Dark axes background
        ax1.tick_params(axis='x', colors='white')  # X-axis ticks color
        ax1.tick_params(axis='y', colors='white')  # Y-axis ticks color

        # Clear the layout and add the Plotly chart
        drawdown_Layout = self.ui.Drawdown_Chart_Groupbox.layout()  # Get the layout of the Ohlcv_Chart_Group
        drawdown_Layout.setContentsMargins(10, 10, 10, 10)  # Set margins (left, top, right, bottom)

        for i in reversed(range(drawdown_Layout.count())):  # Clear existing widgets in the layout
            drawdown_Layout.itemAt(i).widget().deleteLater()
        
        # Create a new canvas to hold the plot
        self.dd_canvas = FigureCanvas(Figure(figsize=(20, 5), facecolor='#2E2E2E'))  # New canvas with dark background
        drawdown_Layout.addWidget(self.dd_canvas)  # Add the new canvas to the layout
        
        # Clear the previous figure
        self.dd_canvas.figure.clear()
        
        # Set the dark background for the figure and axes
        plt.style.use('dark_background')  # Apply dark background style globally
        self.dd_canvas.figure.patch.set_facecolor('#2E2E2E')  # Dark figure background

        # Create axes for plotting
        ax2 = self.dd_canvas.figure.add_subplot(111)  # Drawdown curve

        # Plot drawdown curve for each strategy (or specific strategy if desired)
        for i, (strategy_name, dd_data) in enumerate(drawdown_data.items()):
            ax2.clear()            
            
            decimation_factor = 10 # ADJUST DECIMATION BASED ON THE SAMPLE SIZE
            
            ax2.plot(dd_data['timestamp'][::decimation_factor], dd_data['drawdown'][::decimation_factor], label=f"{strategy_name}", color=colors[i % len(colors)])
            ax2.fill_between(dd_data['timestamp'][::decimation_factor], dd_data['drawdown'][::decimation_factor], color=colors[i % len(colors)], alpha=0.3)

        ax2.legend(loc='lower left')
        ax2.set_facecolor('#2E2E2E')  # Dark axes background
        ax2.tick_params(axis='x', colors='white')  # X-axis ticks color
        ax2.tick_params(axis='y', colors='white')  # Y-axis ticks color

        # # Adjust the margins of the plot within the figure
        canvas.figure.tight_layout(pad=2.0)
        self.dd_canvas.figure.tight_layout(pad=2.0)

        # Refresh canvas
        canvas.draw()
        self.dd_canvas.draw()

        self.ui.Trade_Results_Button.setEnabled(True)
        
    def metrics(self, strategiesList, intCapital, type, threshold, row, above_thresholds):
        
        self.strategiesList = strategiesList
        self.intCapital = intCapital
        
        combined_df = pd.DataFrame()
        combined_dfSignals = pd.DataFrame()
        
        for i, strategy in enumerate(strategiesList):
            
            equity = strategy['equity']
            dfSignals = strategy['signals'].copy()
            
            df = strategy['ohlcv'].copy()
            
            if i == 0:
                
                combined_dfSignals = dfSignals
            
            else:
                
                suffix_1 = f'_df{i}'
                suffix_2 = f'_df{i+1}'
                
                combined_dfSignals = pd.merge(
                    combined_dfSignals, dfSignals, 
                    how='outer', 
                    on='timestamp', 
                    suffixes=(suffix_1, suffix_2)
                    )
                
                # Fill missing values with 0 for 'Open Trades' from the two merged columns
                combined_dfSignals[f'Open_Trades{suffix_1}'] = combined_dfSignals[f'Open_Trades{suffix_1}'].fillna(0)
                combined_dfSignals[f'Open_Trades{suffix_2}'] = combined_dfSignals[f'Open_Trades{suffix_2}'].fillna(0)
                
                # Combine 'Open Trades' from the two merged columns
                combined_dfSignals['Open_Trades'] = combined_dfSignals[f'Open_Trades{suffix_1}'] + combined_dfSignals[f'Open_Trades{suffix_2}']
                
                # Drop the old 'Open Trades' columns with suffixes
                combined_dfSignals = combined_dfSignals.drop(columns=[f'Open_Trades{suffix_1}', f'Open_Trades{suffix_2}'])
                
                combined_dfSignals['Open_Trades'] = combined_dfSignals['Open_Trades'].fillna(0)
            
            def max_drawdown(equity):
                peaks = np.maximum.accumulate(equity)  # Track peaks
                drawdowns = (equity - peaks) / peaks  # Calculate drawdowns
                return np.min(drawdowns)*100, drawdowns*100  # Return the largest (worst) drawdown

            maxDrawdown, drawdowns = max_drawdown(equity)
            
            if type == 'backtest':
                
                netProfit = equity[-1] - equity[0]
                grossProfit = equity[-1]
                profitPercentage = (netProfit / equity[0]) * 100
                totalTrades = len(dfSignals)
                openTrades = len(dfSignals[dfSignals['Trade_Closed'] == 0])
                closedTrades = len(dfSignals[dfSignals['Trade_Closed'] == 1])
                maxDrawdown = maxDrawdown
                avgDrawdown = np.mean(drawdowns)
                profitFactor = 0
                sharpeRatio = 0
                totalWins = len(dfSignals[dfSignals['Result'] == 1])
                totalLosses = len(dfSignals[dfSignals['Result'] == -1])
                consecutiveWins = 0
                consecutiveLosses = 0
                largestWin = 0
                largestLoss = 0
                avgWin = 0
                avgLoss = 0
                avgTrade = 0
                avgTradeTime = 0
                avgWinTime = 0
                avgLossTime = 0
                maxRunup = 0
                avgRunup = 0
                winrate = (totalWins/totalTrades) * 100 if totalTrades > 0 else 0
                rr = 0
                maxOpenTrades = round(combined_dfSignals['Open_Trades'].max())
                avgOpenTrades = 1 if combined_dfSignals['Open_Trades'].mean() < 1 else round(combined_dfSignals['Open_Trades'].mean())
                
                # Profit Factor Calculation
                def calculate_profit_factor(equity):
                    gains = np.diff(equity)[np.diff(equity) > 0]  # Positive returns (gains)
                    losses = np.abs(np.diff(equity)[np.diff(equity) < 0])  # Negative returns (losses)
                    gross_profit = np.sum(gains)
                    gross_loss = np.sum(losses)
                    return gross_profit / gross_loss if gross_loss > 0 else float('inf')

                profitFactor = calculate_profit_factor(equity)

                # Sharpe Ratio Calculation
                def calculate_sharpe_ratio(equity):
                    
                    minute_returns = np.diff(equity) / equity[:-1]
                    avg_minute_return = np.mean(minute_returns)
                    minute_std_dev = np.std(minute_returns)
                    
                    annual_return = (1 + avg_minute_return) ** 525600 - 1
                    
                    annual_std_dev = minute_std_dev * np.sqrt(525600)
                    
                    risk_free_rate_annual = 0.02 # 2%
                    
                    return (annual_return - risk_free_rate_annual) / annual_std_dev if annual_std_dev > 0 else 0
                
                sharpeRatio = calculate_sharpe_ratio(equity)
                
                @njit
                def calculate_consecutive_wins_losses(results):
                    consecutiveWins = 0
                    consecutiveLosses = 0
                    current_consecutive_wins = 0
                    current_consecutive_losses = 0
                    
                    for i in range(len(results)):
                        if results[i] == 1:
                            current_consecutive_wins += 1
                            current_consecutive_losses = 0  # Reset losses if there's a win
                            consecutiveWins = max(consecutiveWins, current_consecutive_wins)
                        elif results[i] == -1:
                            current_consecutive_losses += 1
                            current_consecutive_wins = 0  # Reset wins if there's a loss
                            consecutiveLosses = max(consecutiveLosses, current_consecutive_losses)
                        else:
                            current_consecutive_wins = 0
                            current_consecutive_losses = 0  # Reset both if result is neither win nor loss

                    return consecutiveWins, consecutiveLosses

                @njit
                def calculate_trade_stats(equity):
                    largestWin = -np.inf
                    largestLoss = np.inf
                    
                    winning_trades = []
                    losing_trades = []
                    total_trades = []
                    
                    for i in range(1, len(equity)):
                        diff = equity[i] - equity[i - 1]
                        
                        # Update largest win and largest loss
                        largestWin = max(largestWin, diff)
                        largestLoss = min(largestLoss, diff)
                        
                        if diff > 0:
                            winning_trades.append(diff)
                        elif diff < 0:
                            losing_trades.append(diff)
                        
                        total_trades.append(diff)

                    # Convert lists to numpy arrays for mean calculation
                    winning_trades = np.array(winning_trades)
                    losing_trades = np.array(losing_trades)
                    total_trades = np.array(total_trades)
                    
                    # Use Numba-supported operations on arrays
                    avgWin = np.mean(winning_trades) if winning_trades.size > 0 else 0
                    avgLoss = np.mean(losing_trades) if losing_trades.size > 0 else 0
                    avgTrade = np.mean(total_trades) if total_trades.size > 0 else 0
                    
                    return largestWin, largestLoss, avgWin, avgLoss, avgTrade
                
                # Max Run-up Calculation
                troughs = np.minimum.accumulate(equity)  # Track troughs
                runups = np.where(troughs != 0, (equity - troughs) / troughs, 0)  # Avoid division by zero
                maxRunup = np.max(runups) * 100
                avgRunup = np.mean(runups * 100)

                # Step 1: Calculate consecutive wins/losses
                consecutiveWins, consecutiveLosses = calculate_consecutive_wins_losses(dfSignals['Result'].to_numpy())

                # Step 2: Calculate largest win, loss, and average trade statistics
                equity_np = np.array(equity)
                largestWin, largestLoss, avgWin, avgLoss, avgTrade = calculate_trade_stats(equity_np)
                
                # Calculate Risk to Reward Ratio
                def calculate_RR(avg_profit_per_win, avg_loss_per_loss):
                    
                    RR_solution = abs(avg_profit_per_win) / abs(avg_loss_per_loss) if abs(avg_loss_per_loss) > 0 else 0
                    
                    return RR_solution
                
                def format_RR_as_ratio(RR):
                    
                    if RR > 0:
                        risk = 1
                        reward = round(RR, 1)
                    else:        
                        risk = round(RR, 1)
                        reward = 1
                    
                    return f"{risk} : {reward}"
                
                rr_decimal = calculate_RR(avgWin, avgLoss)
                rr = format_RR_as_ratio(rr_decimal)
                
                dfSignals.loc[:, 'Trade_Duration'] = pd.NaT
                
                # Convert columns to datetime (if not already in datetime format)
                dfSignals.loc[:, 'timestamp'] = pd.to_datetime(dfSignals['timestamp'])
                dfSignals.loc[:, 'Exit_Time'] = pd.to_datetime(dfSignals['Exit_Time'])

                dfSignals['Trade_Duration'] = dfSignals[dfSignals['Result'] != 0]['Exit_Time'] - dfSignals[dfSignals['Result'] != 0]['timestamp']

                avgTradeTime = dfSignals[dfSignals['Result'] != 0]['Trade_Duration'].mean()
                
                avgWinTime = dfSignals[dfSignals['Result'] == 1]['Trade_Duration'].mean()
                avgLossTime = dfSignals[dfSignals['Result'] == -1]['Trade_Duration'].mean()
                
                start_date = dfSignals['timestamp'].iloc[0]
                end_date = dfSignals['timestamp'].iloc[-1]
                
                time_period_years = round((end_date - start_date).days / 365.25)  # Convert days to years
                
                total_return = round(((grossProfit - intCapital) / intCapital), 2)
                
                annualized_return = (1 + total_return) ** (1 / time_period_years) - 1 if time_period_years > 0 else 0
                
                calmar_ratio = round(annualized_return, 4) / round(abs(maxDrawdown / 100), 4) if abs(maxDrawdown) != 0 else 0
                
                peaks = np.maximum.accumulate(equity)  # Track peaks
                df['Peak'] = peaks
                df['Drawdown Phase'] = (equity < df['Peak']).astype(int)
                df['Drawdown Group'] = (df['Drawdown Phase'].diff() == 1).cumsum()
                drawdown_durations = df.groupby('Drawdown Group')['timestamp'].agg(['first', 'last'])
                drawdown_durations['duration'] = (drawdown_durations['last'] - drawdown_durations['first']).dt.days
                max_drawdown_duration = drawdown_durations['duration'].max() if not drawdown_durations.empty else 0
                
                trade_strength = np.log(totalTrades + 1) if totalTrades > 0 else 0
                profit_target = 100
                if profitPercentage > 0:
                    profit_component = (profitPercentage / profit_target) * trade_strength
                    risk_penalty = (1 / (1 + abs(maxDrawdown))) * (1 / (1 + max_drawdown_duration))
                    eer = profit_component * risk_penalty
                else:
                    loss_component = (abs(profitPercentage) / profit_target) * trade_strength
                    eer = -loss_component
                eer = eer * 1000 # For readbility
                
                ## END CALCULATIONS
                
                ## CREATE
                
                rowNumber = i+1
                
                output_labels = {
                    '' : (1, rowNumber),
                    'Initial_Capital' : (2, rowNumber),
                    'Net_Profit' : (3, rowNumber),
                    'Gross_Profit' : (4, rowNumber),
                    'Profit_Percentage' : (5, rowNumber),
                    'Total_Trades_Output' : (6, rowNumber),
                }
                
                ## UPDATE
            
                if netProfit < 0:
                    self.ui.Net_Profit_Output.setStyleSheet("color: red;")  # Set text color to red
                    self.ui.Net_Profit_Output.setText(f'-${abs(netProfit):,.0f}')
                else:
                    self.ui.Net_Profit_Output.setStyleSheet("color: lime;")  # Set text color to green
                    self.ui.Net_Profit_Output.setText(f'${netProfit:,.0f}')
                
                self.ui.Gross_Profit_Output.setText(f'${grossProfit:,.0f}')
                self.ui.Profit_Percentage_Output.setText(f'{round(profitPercentage, 2)}%')
                self.ui.Annual_Return_Output.setText(f'{round((annualized_return * 100), 2)}%')
                self.ui.Total_Trades_Output.setText(f'{round(totalTrades)}')
                self.ui.Open_Trades_Output.setText(f'{round(openTrades)}')
                self.ui.Closed_Trades_Output.setText(f'{round(closedTrades)}')
                self.ui.Max_Drawdown_Output.setText(f'{round(abs(maxDrawdown), 2)}%')
                self.ui.Avg_Drawdown_Output.setText(f'{round(abs(avgDrawdown), 2)}%')
                self.ui.Profit_Factor_Output.setText(f'{round(profitFactor, 2)}')
                self.ui.Sharpe_Ratio_Output.setText(f'{round(sharpeRatio, 2)}')
                                
                self.ui.Calmar_Ratio_Output.setText(f'{calmar_ratio:.2f}')                
                
                # Function to determine the color based on Calmar Ratio
                def get_eer_color(eer):
                    if eer < 0.1:
                        return "red", 'Poor'  # Poor
                    elif 0.1 <= eer < 0.5:
                        return "orange", 'Bad'  # Bad
                    elif 0.5 <= eer < 1:
                        return "yellow", 'Okay'  # Okayish
                    elif 1 <= eer < 2:
                        return "lightgreen", 'Good'  # Good
                    else:
                        return "lime", 'Excellent'  # Excellent
                
                eer_color, quality = get_eer_color(round(eer, 2))
                
                self.ui.Equity_Efficiency_Rate_Output.setText(f'<span style="color:{eer_color};">{eer:.2f}</span>')
                self.ui.Strategy_Quality_Output.setText(f'<span style="color:{eer_color};">{quality}</span>')
                self.ui.Max_Drawdown_Duration_Output.setText(f'{max_drawdown_duration} days')
                self.ui.Total_Wins_Output.setText(f'{round(totalWins)}')
                self.ui.Total_Losses_Output.setText(f'{round(totalLosses)}')
                self.ui.Consecutive_Wins_Output.setText(f'{round(consecutiveWins)}')
                self.ui.Consecutive_Losses_Output.setText(f'{round(consecutiveLosses)}')
                self.ui.Largest_Win_Output.setText(f'${largestWin:,.0f}')
                self.ui.Largest_Loss_Output.setText(f'-${abs(largestLoss):,.0f}')
                self.ui.Avg_Win_Output.setText(f'${avgWin:,.0f}')
                self.ui.Avg_Loss_Output.setText(f'-${abs(avgLoss):,.0f}')
                self.ui.Avg_Trade_Output.setText(f'${avgTrade:,.0f}')
                self.ui.Avg_Trade_Time_Output.setText(str(avgTradeTime).split('.')[0])
                self.ui.Avg_Win_Time_Output.setText(str(avgWinTime).split('.')[0])
                self.ui.Avg_Loss_Time_Output.setText(str(avgLossTime).split('.')[0])
                self.ui.Max_Runup_Output.setText(f'{round(abs(maxRunup), 2)}%')
                self.ui.Avg_Runup_Output.setText(f'{round(abs(avgRunup), 2)}%')
                self.ui.Winrate_Output.setText(f'{round(winrate, 2)}%')
                self.ui.RR_Output.setText(f'{rr}')
                self.ui.Max_Open_Trades_Output.setText(str(maxOpenTrades))
                self.ui.Avg_Open_Trades_Output.setText(str(avgOpenTrades))
                
            elif type == 'optimization':
                
                totalTrades = len(dfSignals)
                totalWins = len(dfSignals[dfSignals['Result'] == 1])
                winrate = (totalWins/totalTrades) * 100 if totalTrades > 0 else 0
                
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem('INCREMENT'))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(threshold)))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem('TRADES'))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(totalTrades)))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem('WIN RATE'))
                self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(f'{round(winrate, 2)}%'))
                self.ui.tableWidget.setItem(row, 6, QTableWidgetItem('MAX DRAWDOWN'))
                self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(f'{round(abs(maxDrawdown), 2)}%'))
                self.ui.tableWidget.setItem(row, 8, QTableWidgetItem('NET PROFIT'))
                value = equity[-1] - equity[0]
                formatted_value = f'${abs(value):,.0f}' if value >= 0 else f'-${abs(value):,.0f}'
                self.ui.tableWidget.setItem(row, 9, QTableWidgetItem(formatted_value))
                
                if winrate <= 15:
                    above_thresholds.append(str(threshold))
                    
                threshold_string = ', '.join(above_thresholds)
                self.ui.tableWidget.setItem(row, 10, QTableWidgetItem(threshold_string))
                
                return above_thresholds
                
    def on_Import_Button_Click(self):
        
        # Open file dialog to select location to open the strategy
        file_dialog = QFileDialog(self)
        self.strategy_file_path, _ = file_dialog.getOpenFileName(self, "Select Strategy File", "", "Python Files (*.py)")
        
        # If no file is selected, return early
        if not self.strategy_file_path:
            return

        try:
            
            # self.strategies_filepaths.append(self.strategy_file_path)
            # Show a success message
            # QMessageBox.information(self, "Success", f"Data imported successfully from {self.strategy_file_path}")
            pass
        except Exception as e:
            # Handle any errors that occur during file reading
            QMessageBox.critical(self, "Error", f"Failed to import the data. Error: {str(e)}")
        
        return self.strategy_file_path
        
    def on_edit_button_click(self):
        
        if self.strategy_file_path:

            # try:
            #     # Open the file with Notepad
            #     subprocess.Popen(["notepad.exe", self.strategy_file_path])
                
            # except Exception as e:
            #     print(f"Error opening Notepad: {e}")

            self.strategy_editor()

    def strategy_editor(self):
        
        self.editor_window = QWidget()
        self.editor_window.setWindowTitle('File Editor')
        self.editor_window.setGeometry(100, 100, 800, 600)
        
        # Create the main layout (vertical layout)
        textEditor_Layout = QVBoxLayout(self.editor_window)
        
        # Create a layout for the buttons (horizontal layout)
        button_layout = QHBoxLayout()
        
        # Create the "Save" and "Save As" buttons
        self.save_button = QPushButton('Save', self.editor_window)
        self.save_button.setMinimumSize(QSize(200, 30))
        self.save_button.setMouseTracking(True)
        self.save_button.setStyleSheet(u"QPushButton {\n"
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
        
        self.save_as_button = QPushButton('Save As', self.editor_window)
        self.save_as_button.setMinimumSize(QSize(200, 30))
        self.save_as_button.setMouseTracking(True)
        self.save_as_button.setStyleSheet(u"QPushButton {\n"
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

        # Add buttons to the button layout
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.save_as_button)

        # Connect buttons to their respective functions
        self.save_button.clicked.connect(self.save_file)
        self.save_as_button.clicked.connect(self.save_file_as)

        # Create the QTextEdit widget for editing the file content
        self.text_edit = QTextEdit(self.editor_window)

        # Add button layout and text edit to the main layout
        textEditor_Layout.addLayout(button_layout)  # Add the buttons at the top
        textEditor_Layout.addWidget(self.text_edit)  # Add the text editor below the buttons

        # Set the layout for the widget
        self.editor_window.setLayout(textEditor_Layout)

        # Load file content into the text editor
        self.load_file()
        
        self.editor_window.showMaximized()  # This line will make the window open maximized()

    def load_file(self):
        """Load the selected file into the text editor"""
        with open(self.strategy_file_path, 'r') as file:
            code = file.read()
            self.text_edit.setPlainText(code)

    def save_file(self):
        """Save the file after editing"""
        with open(self.strategy_file_path, 'w') as file:
            file.write(self.text_edit.toPlainText())

        self.editor_window.close()  # Close the editor window after saving

    def save_file_as(self):
        """Save the content to a new file chosen by the user"""
        new_file_path, _ = QFileDialog.getSaveFileName(self, "Save As", "", "Python Files (*.py)")
        if new_file_path:
            self.strategy_file_path = new_file_path
            with open(self.strategy_file_path, 'w') as file:
                file.write(self.text_edit.toPlainText())
            print(f"File saved as: {self.strategy_file_path}")
            
        self.editor_window.close()  # Close the editor window after saving

    def checkInputs(self):
        
        if self.ui.Entry_Text.text() and self.ui.TP_Text.text() and self.ui.SL_Text.text():
            self.ui.Backtest_Button.setEnabled(True)
        else:
            self.ui.Backtest_Button.setEnabled(False)

    def trade_results(self, strategiesList, intCapital):
        
        for i, strategy in enumerate(strategiesList):
            
            dfSignals = strategy['signals'].copy()
        
        # Open a new window and display the dataframe
        self.df_window = QWidget()
        self.df_window.setWindowTitle("Trade Results")
        
        # Create a table widget
        self.table = QTableWidget()
        self.set_table_data(dfSignals)
        
        # Set layout
        layout = QVBoxLayout(self.df_window)
        layout.addWidget(self.table)
        
        self.df_window.setLayout(layout)
            
        # Maximize the window
        self.df_window.showMaximized()  # This line will make the window open maximized
        
        self.df_window.show()

    def set_table_data(self, df):
        # Set table rows and columns based on DataFrame shape
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        
        # Set the column headers
        self.table.setHorizontalHeaderLabels(df.columns)
        
        # Fill the table with data from the DataFrame
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[row, col]))
                self.table.setItem(row, col, item)
        
        # Make the columns sortable
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setSortingEnabled(True)
        
        # Make the columns resizable by the user
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        
        # Automatically resize columns to fit content
        self.table.resizeColumnsToContents()
        
        # Now double the size of each column
        for col in range(self.table.columnCount()):
            new_width = self.table.columnWidth(col) * 1.5  # Double the width
            self.table.setColumnWidth(col, new_width)
        
    def create_strategy_widget(self, filePath):
        
        if os.path.splitext(filePath)[1]:
            strategyName = os.path.splitext(os.path.basename(filePath))[0]  # Get file name without extension
        else:
            strategyName = filePath
        
        manager_Layout = self.ui.Manager_Widget.layout()
        manager_Layout.setAlignment(Qt.AlignTop)  # Apply top vertical alignment to the layout

        self.strategy_Widget = QWidget(self.ui.Manager_Widget)
        self.strategy_Widget.setObjectName(u"strategy_Widget")
        self.strategy_Widget.setMinimumSize(QSize(0, 40))
        self.strategy_Widget.setStyleSheet(u'background-color: rgb(61,61,61);')
        
        self.strategyWidget_Layout = QHBoxLayout(self.strategy_Widget)
        self.strategyWidget_Layout.setObjectName(u"strategyWidget_Layout")
        self.strategyWidget_Layout.setContentsMargins(20, 0, 11, 0)

        self.strategy_Name_Label = QLabel(self.strategy_Widget)
        self.strategy_Name_Label.setObjectName(u'strategy_Name_Label')
        self.strategy_Name_Label.setMinimumSize(QSize(0, 30))
        self.strategy_Name_Label.setMaximumSize(QSize(16777215, 30))
        self.strategy_Name_Label.setText(strategyName)
        
        self.strategyWidget_Layout.addWidget(self.strategy_Name_Label)
        
        self.strategy_Selection_Button = QCheckBox(self.strategy_Widget)
        self.strategy_Selection_Button.setObjectName(u"strategy_Selection_Button")
        self.strategy_Selection_Button.setMinimumSize(QSize(20, 20))
        self.strategy_Selection_Button.setMaximumSize(QSize(20, 20))
        self.strategy_Selection_Button.setIconSize(QSize(20, 20))
        self.strategy_Selection_Button.setChecked(True)

        self.strategyWidget_Layout.addWidget(self.strategy_Selection_Button)

        self.strategy_Visibility_Button = QPushButton(self.strategy_Widget)
        self.strategy_Visibility_Button.setObjectName(u"strategy_Visibility_Button")
        self.strategy_Visibility_Button.setMinimumSize(QSize(20, 20))
        self.strategy_Visibility_Button.setMaximumSize(QSize(20, 20))
        self.strategy_Visibility_Button.setCheckable(True)  # Allow it to be checkable (toggle button)
        
        self.strategy_Visibility_Button.clicked.connect(lambda checked, currentWidget=self.strategy_Widget: self.change_Visibility_Icon(currentWidget))
        
        self.strategy_Visibility_Button.setIcon(QIcon("view.png"))
        self.strategy_Visibility_Button.setIconSize(QSize(15, 15))
        
        self.strategyWidget_Layout.addWidget(self.strategy_Visibility_Button)
        
        self.strategy_Edit_Button = QPushButton(self.strategy_Widget)
        self.strategy_Edit_Button.setObjectName(u"strategy_Edit_Button")
        self.strategy_Edit_Button.setMinimumSize(QSize(20, 20))
        self.strategy_Edit_Button.setMaximumSize(QSize(20, 20))
        
        self.strategy_Edit_Button.clicked.connect(lambda checked, currentWidget=self.strategy_Widget: self.edit_strategy(currentWidget))
        
        iconE = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.strategy_Edit_Button.setIcon(iconE)
        self.strategy_Edit_Button.setIconSize(QSize(14, 14))
        
        self.strategyWidget_Layout.addWidget(self.strategy_Edit_Button)
        
        self.strategy_Delete_Button = QPushButton(self.strategy_Widget)
        self.strategy_Delete_Button.setObjectName(u"strategy_Delete_Button")
        self.strategy_Delete_Button.setMinimumSize(QSize(20, 20))
        self.strategy_Delete_Button.setMaximumSize(QSize(20, 20))
        
        iconD = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.strategy_Delete_Button.setIcon(iconD)
        self.strategy_Delete_Button.setIconSize(QSize(15, 15))
        
        self.strategyWidget_Layout.addWidget(self.strategy_Delete_Button)
        
        self.strategy_Delete_Button.clicked.connect(lambda checked, currentWidget=self.strategy_Widget: self.remove_strategy_widget(currentWidget, filePath))

        # manager_Layout.addWidget(self.strategy_Widget)
        
        return self.strategy_Widget, self.strategy_Name_Label, self.strategy_Selection_Button, self.strategy_Visibility_Button, self.strategy_Edit_Button, self.strategy_Delete_Button

    def add_strategy_widget(self, filePath, ohlcv_data):
        
        stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete = self.create_strategy_widget(filePath)

        self.strategiesWidgetList.append((stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete))
        
        self.strategies_filepaths.append((filePath, ohlcv_data))

        self.ui.Manager_Widget.layout().insertWidget(self.ui.Manager_Widget.layout().count(), stratagyWidget)

    def change_Visibility_Icon(self, currentWidget):
        
        # Safely remove and delete the widget
        for stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete in self.strategiesWidgetList:
            
            if stratagyWidget == currentWidget:
                
                if strategyVisibility.isChecked():
                    
                    print(strategy['strategy_name'] for strategy in self.strategiesList)
                    strategiesList = self.strategiesList
                    
                    self.plot_results(strategiesList, self.intCapital)
                    strategyVisibility.setIcon(QIcon("view.png"))  # Change icon to "eye open"
                    
                else:
                    
                    strategiesList = self.strategiesList
                    
                    for strategy in strategiesList:
                        if strategy['strategy_name'] == strategyLabel.text():
                            strategiesList.remove(strategy)
                            
                    self.plot_results(strategiesList, self.intCapital)
                    strategyVisibility.setIcon(QIcon("hide.png"))  # Change icon to "eye closed"
    
    def edit_strategy(self, currentWidget):
        
        self.strategy_popup = strategy_window.StrategyWindow(self)
        self.strategy_popup.exec()
        
        self.strategy_popup.get_indicators_data()
    
    def remove_strategy_widget(self, currentWidget, filePath):
        
        # Safely remove and delete the widget
        for stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete in self.strategiesWidgetList:
            
            if stratagyWidget == currentWidget:
                
                # Remove the widget from the layout and delete it
                self.ui.Manager_Widget.layout().removeWidget(stratagyWidget)
                stratagyWidget.deleteLater()
                self.strategiesWidgetList.remove((stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete))  # Remove it from our tracking list
                self.strategies_filepaths.remove(filePath)
                
    def clear_strategies(self):
        
        for stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete in self.strategiesWidgetList:
            
            # Remove the widget from the layout and delete it
            self.ui.Manager_Widget.layout().removeWidget(stratagyWidget)
            stratagyWidget.deleteLater()
            
        self.strategiesWidgetList.clear()
        self.strategies_filepaths.clear()
        
        self.ui.Run_Backtest_Button.setEnabled(False)
        self.ui.Trade_Results_Button.setEnabled(False)