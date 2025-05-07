from files import indicators # import indicators.py file from files folder
import numpy as np
import random
import re
import pandas as pd
import scipy.stats as stats
from scipy.stats import anderson
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout, QSizePolicy, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from numba import jit
from time import sleep
from itertools import combinations

class MachineLearning:
    
    def __init__(self, parent):
        
        self.parent = parent
        
        self.indicators_instance = indicators.Indicators()
        
        self.populate_ui()
        self.ui_interactions()
        self.variables()
    
    def ui_interactions(self):
        self.parent.ui.ml_datasplit_Slider.valueChanged.connect(self.update_datasplit_label)
        self.parent.ui.ml_fetchdata_Button.clicked.connect(self.fetch_data)
        self.parent.ui.ml_simulate_Button.clicked.connect(self.ml_simulation)
        self.parent.ui.ml_backtest_Button.clicked.connect(self.backtest_selection)
    
    def populate_ui(self):
        self.parent.populate_symbols(self.parent.ui.ml_symbol_selection_Combobox)
        self.parent.populate_timeframes(self.parent.ui.ml_timeframe_selection_Combobox)
        self.populate_ml_models()
        self.populate_fitness_function()
        self.populate_backtest_types()
    
    def variables(self):
        self.eer = 0
        self.efficiency = 0
    
    def get_selection_dropdowns(self):
        
        self.symbol = self.parent.ui.ml_symbol_selection_Combobox.currentText()
        self.timeframe = self.parent.ui.ml_timeframe_selection_Combobox.currentText()
    
    def update_datasplit_label(self):
        
        self.parent.ui.ml_datasplit_Label.setText(f'{self.parent.ui.ml_datasplit_Slider.value()}%')
    
    def populate_backtest_types(self):
        backtest_types = ['Default', 'Adaptive', 'K-Means', 'Randomize']
        
        self.parent.ui.ml_backtest_selection_Combobox.clear()
        self.parent.ui.ml_backtest_selection_Combobox.addItems(backtest_types)
    
    def backtest_selection(self):
        backtest_type = self.parent.ui.ml_backtest_selection_Combobox.currentText()
        if backtest_type == 'Default':
            self.default_backtest()
        elif backtest_type == 'Adaptive':
            self.adaptive_backtest()
        elif backtest_type == 'K-Means':
            self.kmeans_backtest()
        elif backtest_type == 'Randomize':
            self.randomize_backtest()
        else:
            return
    
    def fetch_data(self):
        
        self.get_selection_dropdowns()
        
        # symbols_list = ["ONTUSDT", "BATUSDT", "1INCHUSDT", "TRXUSDT", "BELUSDT"]
        
        # self.parent.ui.ml_debug_Textedit.setPlainText('Fetching OHLCV data...')
                
        # Fetch Ohlcv data
        self.df, self.df_3m, self.df_5m, self.df_15m, self.df_1H, self.df_1D  = self.parent.download_ohlcv_data(
            self.parent.ui.ml_symbol_selection_Combobox, self.parent.ui.ml_timeframe_selection_Combobox, self.parent.ui.ml_startdate_Dateedit, self.parent.ui.ml_enddate_Dateedit
            )
        
        # Calculate Indicator values
        self.df = self.calculate_indicators(self.df)
        
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 10000)
        
        self.parent.ui.ml_debug_Textedit.setPlainText(f'{self.df.head(5)}\n{self.df.tail(5)}')
        
        # self.df.head(5).to_csv("analysis_head.csv", index=False)
        # self.df.tail(5).to_csv("analysis_tail.csv", index=False)
        
    def default_backtest(self, lengths = [50, 100]):
        
        for length in lengths:
            self.df = self.indicators_instance.calculate_sma(self.df, length)
        
        self.df = self.signal_generation(self.df)
        
        # self.parent.ui.ml_debug_Textedit.setPlainText(f'{self.df.head(5)}\n{self.df.tail(5)}')
        
        self.df = self.result(self.df)
        
        self.parent.ui.ml_debug_Textedit.setPlainText(f'{self.df.head(5)}\n{self.df.tail(5)}')
        
        self.metrics(self.df)
        self.plot_equity_curve(self.df)
        
        QApplication.processEvents()  # Update the UI to plot in real-time
    
    def adaptive_backtest(self):
        self.default_backtest()
        
        QApplication.processEvents() # Update the UI if needed
        
        self.simulation()
        self.adaptive_loop()
        
    def kmeans_backtest(self):
        self.default_backtest()
        
        QApplication.processEvents() # Update the UI if needed
        
        self.simulation()
        self.kmeans_loop()
    
    def randomize_backtest(self):
        
        symbols = ['MKRUSDT']
        timeframes = ['15m']
        
        lengths = ['20', '50', '100', '200']
        
        # Generate all combinations of two distinct elements
        length_combinations = list(combinations(lengths, 2))
        
        atrs = ['1', '2', '3', '4', '5', '6', '7', '8', '10', '15', '20', '25', '30']
        atr15s = ['1', '2', '3', '4', '5', '6', '7', '8', '10']
        
        rrs = ['1', '2', '3', '4', '5']
        
        for symbol in symbols:
            for timeframe in timeframes:
                
                self.df = pd.DataFrame()
                
                self.reset_params(symbol, timeframe)
                QApplication.processEvents() # Update the UI if needed
                
                self.get_selection_dropdowns()
                
                # Fetch Ohlcv data
                self.df, self.df_3m, self.df_5m, self.df_15m, self.df_1H, self.df_1D  = self.parent.download_ohlcv_data(
                    self.parent.ui.ml_symbol_selection_Combobox, self.parent.ui.ml_timeframe_selection_Combobox, self.parent.ui.ml_startdate_Dateedit, self.parent.ui.ml_enddate_Dateedit)
                
                # Determine which list to iterate over based on the timeframe
                atr_list = atrs if timeframe != '15m' else atr15s
                
                for a,b in length_combinations:
                    
                    self.df = self.indicators_instance.calculate_sma(self.df, int(a))
                    self.df = self.indicators_instance.calculate_sma(self.df, int(b))
                    
                    self.df = self.signal_generation(self.df, a=a, b=b)
                    
                    for atr in atr_list:
                        
                        self.df = self.indicators_instance.calculate_stop_loss(self.df, 14, int(atr))
                        
                        for rr in rrs:
                            
                            self.df = self.result(self.df, rr=int(rr))
                            
                            # self.parent.ui.ml_debug_Textedit.setPlainText(f'{self.df.head(5)}\n{self.df.tail(5)}')
                            
                            self.metrics(self.df)
                            self.plot_equity_curve(self.df)
                            
                            print(f'{symbol}, {timeframe}, SMA: {a}&{b}, ATR: {atr}, RR: {rr}, EER: {round((self.efficiency), 2)}')
                            
                            QApplication.processEvents()  # Update the UI to plot in real-time
    
    def reset_params(self, symbol, timeframe):
        
        self.parent.ui.ml_symbol_selection_Combobox.setCurrentText(symbol)
        self.parent.ui.ml_timeframe_selection_Combobox.setCurrentText(timeframe)
    
    def simulation(self):
        
        self.split_dataframe()
        self.calculate_means()
        self.calculate_midpoint()
        self.store_conditions()
        
    def calculate_indicators(self, df):

        self.parent.ui.ml_debug_Textedit.setPlainText('Processing Indicators..')
        
        df = self.indicators_instance.calculate_hma(df)
        df = self.indicators_instance.calculate_ema(df)
        df = self.indicators_instance.calculate_sma(df)
        
        # df = self.indicators_instance.calculate_wma(df)
        df = self.indicators_instance.calculate_rsi(df)
        df = self.indicators_instance.calculate_macd(df)
        df = self.indicators_instance.calculate_stocastic(df)
        df = self.indicators_instance.ma_distance(df)
        df = self.indicators_instance.calculate_adx(df)
        df = self.indicators_instance.calculate_cci(df)
        df = self.indicators_instance.calculate_VWAP(df)
        df = self.indicators_instance.calculate_bollinger_bands(df)
        df = self.indicators_instance.calculate_momentum(df)
        df = self.indicators_instance.calculate_obv(df)
        df = self.indicators_instance.calculate_roc(df)
        # df = self.indicators_instance.calculate_ichimoku(df)
        df = self.indicators_instance.calculate_psar(df)
        df = self.indicators_instance.supertrend(df)
        df = self.indicators_instance.donchian_channels(df)
        # df = self.indicators_instance.heikin_ashi(df)
        df = self.indicators_instance.identify_candlestick_patterns(df)
        df = self.indicators_instance.calculate_stop_loss(df)
        df = self.indicators_instance.calculate_sma_slope(df)
        df = self.indicators_instance.hh_ll(df)
        df = self.indicators_instance.calculate_hl_oscillator(df)
        df = self.indicators_instance.calculate_vix(df)
        # df = self.indicators_instance.market_regime(df)
        df = self.indicators_instance.calculate_market_regime(df)
        df = self.indicators_instance.lag_ohlcv(df)
        df = self.indicators_instance.datetime_split(df)
        # df = self.indicators_instance.economic_data(df)
        df = self.indicators_instance.candle_lengths(df)
        df = self.indicators_instance.price_movement(df)
        
        return df
    
    def signal_generation(self, df, a=None, b=None, condition=None):
        
        df['Signal'] = np.zeros(len(df))
        
        if condition is None:
            
            if a is None:
                bullish_cross = (df['sma_50'].shift(1) < df['sma_100'].shift(1)) & (df['sma_50'] > df['sma_100'])
                bearish_cross = (df['sma_50'].shift(1) > df['sma_100'].shift(1)) & (df['sma_50'] < df['sma_100'])
            
            else:
                bullish_cross = (df[f'sma_{a}'].shift(1) < df[f'sma_{b}'].shift(1)) & (df[f'sma_{a}'] > df[f'sma_{b}'])
                bearish_cross = (df[f'sma_{a}'].shift(1) > df[f'sma_{b}'].shift(1)) & (df[f'sma_{a}'] < df[f'sma_{b}'])
        
        else:
            # Evaluate the condition string to create a boolean mask
            condition_mask = eval(condition)
            
            # Define the conditions with the additional condition mask
            bullish_cross = (df['sma_50'].shift(1) < df['sma_100'].shift(1)) & (df['sma_50'] > df['sma_100']) & condition_mask
            bearish_cross = (df['sma_50'].shift(1) > df['sma_100'].shift(1)) & (df['sma_50'] < df['sma_100']) & condition_mask
        
        # Define the conditions combining with the passed conditionnditions
        df['Signal'] = np.select([bullish_cross, bearish_cross], [1, -1], default=0)
        
        return df

    @staticmethod
    @jit(nopython=True)
    def result_np(signal, open, high, low, close, stoploss_long, stoploss_short, timestamp, starting_capital = 1000.0, rr=1):
        risk_percent = 1
        capital = starting_capital
        cash = (capital * risk_percent) / 100

        entry = np.full(len(signal), np.nan)
        stop_loss = np.full(len(signal), np.nan)
        take_profit = np.full(len(signal), np.nan)
        trade_closed = np.zeros(len(signal), dtype=np.bool_)
        result = np.zeros(len(signal), dtype=np.int32)
        trade_return = np.zeros(len(signal))
        commissioned_return = np.zeros(len(signal))
        exit_time = np.zeros(len(signal))
        equity = np.full(len(signal), capital)
        
        open_trades = np.zeros(len(close))

        for i in range(len(close)):
            if signal[i] == 1 and open_trades[i] < 1:
                # result[i] = 0
                entry[i] = entry_price = close[i]
                stop_loss[i] = stop_loss_price = stoploss_long[i]
                take_profit[i] = take_profit_price = entry_price + ((entry_price - stop_loss_price) * rr)
                current_position_size = cash / (entry_price - stop_loss_price)
                fee = 0.001 * (entry_price * current_position_size)
                for j in range(i + 1, len(signal)):
                    open_trades[j] += 1
                    if high[j] >= take_profit_price:
                        trade_closed[i] = True
                        trade_return[i] = (take_profit_price - entry_price) * current_position_size
                        net_trade_return = trade_return[i] - fee
                        capital += net_trade_return
                        result[i] = 1
                        cash = (capital * risk_percent) / 100
                        exit_time[i] = timestamp[j]
                        commissioned_return[i] = net_trade_return
                        break
                    elif low[j] <= stop_loss_price:
                        trade_closed[i] = True
                        trade_return[i] = (stop_loss_price - entry_price) * current_position_size
                        net_trade_return = trade_return[i] - fee
                        capital += net_trade_return
                        result[i] = -1
                        cash = (capital * risk_percent) / 100
                        exit_time[i] = timestamp[j]
                        commissioned_return[i] = net_trade_return
                        break
                    
            elif signal[i] == -1 and open_trades[i] < 1:
                result[i] = 0
                # entry[i] = entry_price = close[i]
                # stop_loss[i] = stop_loss_price = stoploss_short[i]
                # take_profit[i] = take_profit_price = entry_price - ((stop_loss_price - entry_price) * rr)
                # current_position_size = cash / (stop_loss_price - entry_price)
                # fee = 0.001 * (entry_price * current_position_size)
                # for j in range(i + 1, len(close)):
                #     open_trades[j] += 1
                #     if low[j] <= take_profit_price:
                #         trade_closed[i] = True
                #         trade_return[i] = (entry_price - take_profit_price) * current_position_size
                #         net_trade_return = trade_return[i] - fee
                #         capital += net_trade_return
                #         result[i] = 1
                #         cash = (capital * risk_percent) / 100
                #         exit_time[i] = timestamp[j]
                #         commissioned_return[i] = net_trade_return
                #         break
                #     elif high[j] >= stop_loss_price:
                #         trade_closed[i] = True
                #         trade_return[i] = (entry_price - stop_loss_price) * current_position_size
                #         net_trade_return = trade_return[i] - fee
                #         capital += net_trade_return
                #         result[i] = -1
                #         cash = (capital * risk_percent) / 100
                #         exit_time[i] = timestamp[j]
                #         commissioned_return[i] = net_trade_return
                #         break
            
            equity[i] = capital

        return entry, stop_loss, take_profit, trade_closed, result, trade_return, commissioned_return, exit_time, equity
    
    def result(self, df, starting_capital = 1000.0, rr=1):
        signal = df['Signal'].values
        open = df['open'].values
        high = df['high'].values
        low = df['low'].values
        close = df['close'].values
        stoploss_short = df['stoploss_short'].values
        stoploss_long = df['stoploss_long'].values
        
        df['timestamp'] = df['timestamp'].astype(np.int64) // 10**9  # Unix timestamp in seconds
        timestamp = df['timestamp'].values
        
        entry, stop_loss, take_profit, trade_closed, result, trade_return, commissioned_return, exit_time, equity = self.result_np(signal, open, high, low, close, stoploss_long, stoploss_short, timestamp, starting_capital, rr=rr)
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        df['Exit_Time'] = pd.to_datetime(np.where(exit_time == 0.0, pd.NaT, exit_time), unit='s')
        
        df['Entry'] = entry
        df['Stop Loss'] = stop_loss
        df['Take Profit'] = take_profit
        df['Trade Closed'] = trade_closed
        df['Result'] = result
        df['Return'] = trade_return
        df['Commissioned Return'] = commissioned_return
        df['Equity'] = equity

        return df
    
    def metrics(self, df):
        
        totalTrades = len(df[df['Trade Closed']])
        
        netProfit = round(df.iloc[-1]['Equity'] - df.iloc[0]['Equity'])
        
        profitPercentage = round((netProfit / df.iloc[0]['Equity']) * 100)
        
        winRate = round((len(df[df['Result'] == 1]) / totalTrades) * 100) if totalTrades > 0 else 0
        
        peaks = np.maximum.accumulate(df['Equity'])  # Track peaks
        drawdowns = (df['Equity'] - peaks) / peaks # Calculate drawdowns
        maxDrawdown = round(np.min(drawdowns)*100)  # Return the largest (worst) drawdown

        start_date = df.iloc[0]['timestamp']
        end_date = df.iloc[-1]['timestamp']
        time_period_years = round((end_date - start_date).days / 365.25)  # Convert days to years
        total_return = round((netProfit / df.iloc[0]['Equity']), 2)
        annualized_return = (1 + total_return) ** (1 / time_period_years) - 1 if time_period_years > 0 else 0
        cagr = ((df.iloc[-1]['Equity'] / df.iloc[0]['Equity']) ** (1 / time_period_years)) - 1 if time_period_years > 0 else 0
        
        calmerRatio = round(annualized_return, 4) / round(abs(maxDrawdown / 100), 4) if abs(maxDrawdown) != 0 else 0
        
        df_daily = df.resample('D', on='timestamp').last()  # Assumes 'timestamp' is a datetime type
        df_daily['Daily Return'] = df_daily['Equity'].pct_change().dropna()
        volatility = df_daily['Daily Return'].std()
        annualized_volatility = volatility * np.sqrt(365)
        
        confidence_level = 0.95
        var = -df_daily['Daily Return'].quantile(1 - confidence_level)  # Positive value for loss
        
        var_threshold = df_daily['Daily Return'].quantile(1 - confidence_level)
        tail_losses = df_daily['Daily Return'][df_daily['Daily Return'] <= var_threshold]
        cvar = -tail_losses.mean()  # Positive value for loss
        
        df['Peak'] = peaks
        df['Drawdown Phase'] = (df['Equity'] < df['Peak']).astype(int)
        df['Drawdown Group'] = (df['Drawdown Phase'].diff() == 1).cumsum()
        drawdown_durations = df.groupby('Drawdown Group')['timestamp'].agg(['first', 'last'])
        drawdown_durations['duration'] = (drawdown_durations['last'] - drawdown_durations['first']).dt.days
        max_drawdown_duration = drawdown_durations['duration'].max() if not drawdown_durations.empty else 0
        
        recovery_factor = netProfit / abs(maxDrawdown) if abs(maxDrawdown) != 0 else 0
        
        # Calculate risk-adjusted return with error handling
        if pd.isna(cagr) or pd.isna(volatility) or volatility == 0:
            riskAdjustedReturn = 0  # or 0, depending on your use case
        else:
            riskAdjustedReturn = round(cagr / volatility)  # Round to 2 decimal places
        
        trade_strength = np.log(totalTrades + 1) if totalTrades > 0 else 0
        profit_target = 100
        if profitPercentage > 0:
            profit_component = (profitPercentage / profit_target) * trade_strength
            risk_penalty = (1 / (1 + abs(maxDrawdown))) * (1 / (1 + max_drawdown_duration))
            eer = profit_component * risk_penalty
        else:
            loss_component = (abs(profitPercentage) / profit_target) * trade_strength
            eer = -loss_component
        eer = eer * 1000 # Just for more redability
        self.efficiency = eer
        # print(f'Equity Efficiency Rate (EER): {round((eer), 2)}')
        
        if eer > self.eer:
            
            print(f'Total Trades: {totalTrades}')
            print(f'Net Profit: {netProfit}')
            print(f'Profit Percentage: {profitPercentage}%')
            print(f'Win Rate: {winRate}%')
            print(f'Max Drawdown: {maxDrawdown}%')
            print(f'CAGR: {round(cagr * 100)}%')
            print(f'Calmer Ratio: {round(calmerRatio, 2)}')
            print(f'Volatility: {round(volatility * 100, 2)}%')
            print(f'Volatility (Annualized): {round(annualized_volatility * 100, 2)}%')
            print(f'VaR (95% Confidence): {round(var * 100, 2)}%')
            print(f'CVaR (95% Confidence): {round(cvar * 100, 2)}%')
            print(f'Max Drawdown Duration: {max_drawdown_duration} days')
            print(f'Recovery Factor: {round(recovery_factor, 2)}')
            print(f'Risk Adjusted Return: {riskAdjustedReturn}%')
            
            self.eer = eer
        
    def plot_equity_curve(self, df):
        
        colors = [
            '#A7D06A', '#FF8B7D', '#8977A7', '#F9D3D9', '#B0C5E3', '#A97D76',
            '#C78DC4', '#00B991', '#EE5F43', '#64D1BD', '#F4D47E', '#7A7FB9'
        ]
        
        color = random.choice(colors)
        
        label = self.parent.ui.chart_placeholder_Label
        
        # Check if the label already has a layout and a FigureCanvas widget.
        layout = label.layout()
        canvas = None
        
        if layout is not None:
            for i in range(layout.count()):
                widget = layout.itemAt(i).widget()
                if isinstance(widget, FigureCanvasQTAgg):
                    canvas = widget
                    break
        
        if canvas is None:
            # No existing canvas found; create a new one.
            fig = Figure(figsize=(16, 9), facecolor='none')
            ax = fig.add_subplot(111)
            ax.plot(df['timestamp'], df['Equity'] - df.iloc[0]['Equity'], label='Equity Curve', color=color)

            ax.axhline(y=0, color='grey', linestyle='--', linewidth=1, alpha=0.3, zorder=-2)
            
            ax.set_facecolor('none')
            ax.spines['top'].set_color('white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            
            fig.tight_layout(pad=2.0)
            
            canvas = FigureCanvas(fig)
            canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            canvas.updateGeometry()
            
            # Create a new layout if not already set.
            if layout is None:
                layout = QVBoxLayout(label)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)
                label.setLayout(layout)
            layout.addWidget(canvas)
        else:
            
            # Use the existing canvas.
            fig = canvas.figure
            if fig.get_axes():
                ax = fig.get_axes()[0]
            else:
                ax = fig.add_subplot(111)

            ax.plot(df['timestamp'], df['Equity'] - df.iloc[0]['Equity'], label='Equity Curve', color=color)
            ax.axhline(y=0, color='grey', linestyle='--', linewidth=1, alpha=0.3, zorder=-2)
            
            ax.set_facecolor('none')
            ax.spines['top'].set_color('white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            
            fig.tight_layout(pad=2.0)
            
            canvas.draw()
    
    def populate_fitness_function(self):
        
        self.parent.ui.ml_fitness_function_Combobox.clear()
        self.parent.ui.ml_fitness_function_Combobox.addItems(['Total Trades', 'Net Profit', 'Profit Percentage', 'Win Rate', 'Max Drawdown', 'CAGR', 'Calmer Ratio', 'Volatility', 'Annualized Volatility', 'VaR', 'CVaR', 'Max Drawdown Duration', 'Recovery Factor', 'Risk Adjusted Return'])
    
    def populate_ml_models(self):
        
        self.parent.ui.ml_models_Combobox.clear()
        self.parent.ui.ml_models_Combobox.addItems(['Linear Regression', 'Logistic Regression', 'XGBoost', 'K-Means', 'Genetic Algorithm', 'LSTM', 'Random Forest', 'Decision Tree', 'Neural Network'])
        
    def split_dataframe(self):
        
        df = self.df.copy()
        
        wins_df = df[df['Result'] == 1]
        loses_df = df[df['Result'] == -1]

        # Define columns to keep – adjust the list below as needed
        columns_to_keep = [
            'volume', 'rsi', 'macd_line', 'signal_line',
            'macd_histogram', 'stocastic_%k', 'stocastic_%d',
            'ema_200_distance', 'sma_200_distance', 'hma_200_distance', 'adx',
            '+dm', '-dm', 'cci', 'cum_price_vol', 'cum_vol', 'std', 'bb_width',
            'momentum', 'obv', 'roc', 'candle_length', 'pulldown_length',
            'pullup_length', 'tr_st', 'atr_st', 'supertrend', 'bullish_engulfing', 'bearish_engulfing', 'hammer',
            'shooting_star', 'doji', 'tr', 'atr', 'atr_multiplier', 'ma_df', 'ma_slope', 'ma_acceleration',
            'ma_highest_acceleration', 'ma_acceleration_normalized', 'ma_trend',
            'day', 'is_weekend', 'is_weekday', 'hour', 'year', 'month', 'day_of_year', 'day_of_week', 'minute', 
            'week_of_year', 'days_in_month', 'quarter', 'is_month_start', 'is_month_end', 'is_quarter_start', 'is_quarter_end',
            'is_year_start', 'is_year_end', 'is_leap_year', 'is_week_start', 'is_week_end', 'hl_oscillator', 'vix', 'ma_distance',
            'regime', 'relative_regime', 'regime_score', 'candle', 'is_bull', 'is_bear', 'candle_size_change_pct', 'candle_pct_open',
            'upper_wick_pct', 'lower_wick_pct', 'body_pct', 'body_upper_wick_pct', 'body_lower_wick_pct', 'wick_pct', 'gap',
            'prev_candle_pct_change', 'open_to_close_pct', 'open_to_high_pct', 'open_to_low_pct',
            'price_momentum', 'intracandle_range_pct', 'momentum_sma'
        ]

        self.wins_df = wins_df[columns_to_keep]
        self.loses_df = loses_df[columns_to_keep]
    
    def calculate_means(self):
        
        wins_df = self.wins_df.copy()
        loses_df = self.loses_df.copy()
        
        # Calculate the column means and store in new DataFrames for wins and losses respectively
        self.win_means = pd.DataFrame(wins_df.mean()).transpose()
        self.loss_means = pd.DataFrame(loses_df.mean()).transpose()
    
    def calculate_midpoint(self):
        
        win_means = self.win_means.copy()
        loss_means = self.loss_means.copy()
        
        # Create a new DataFrame with the same columns as win_means and loss_means
        combined_stats = pd.DataFrame(columns=win_means.columns, index=['win_means', 'loss_means', 'median'])
        
        # Store win_means and loss_means into the respective rows
        combined_stats.loc['win_means'] = win_means.iloc[0]
        combined_stats.loc['loss_means'] = loss_means.iloc[0]
        
        # For the median row, average the win_means and loss_means values column-wise
        combined_stats.loc['median'] = (win_means.iloc[0] + loss_means.iloc[0]) / 2
        
        # Optionally, store the new DataFrame as an attribute
        self.combined_stats = combined_stats
        
    def store_conditions(self):
        
        combined_stats = self.combined_stats.copy()
        
        conditions = []
        
        for stat in combined_stats.index:
            
            for col in combined_stats.columns:
                
                value = combined_stats.loc[stat, col]
                conditions.append(f"df['{col}'] >= {value}")
                conditions.append(f"df['{col}'] <= {value}")
        
        self.conditions = conditions
        
    def kmeans_loop(self):
        
        df = self.df.copy()
        
        for condition in self.conditions:
            
            print(condition)
            
            df = self.signal_generation(df, condition=condition)
            df = self.result(df)
            self.metrics(df)
            self.plot_equity_curve(df)
            
            QApplication.processEvents()  # Update the UI to plot in real-time

    def adaptive_loop(self):
        # Make sure the dataframe is sorted by timestamp
        df = self.df.copy()
        df.sort_values(by='timestamp', inplace=True)
        overall_results = pd.DataFrame()
        
        # Initialize current capital to 1000 (or whatever your base capital is)
        current_capital = 1000.0
        
        lookback = 180
        
        # Pointer for the current start position
        start_date = df.iloc[0]['timestamp']
        initial_training_end_date = start_date + pd.DateOffset(days=lookback)
        
        # Find the index of the first row with a timestamp >= initial_training_end_date
        end_index = df.index[df['timestamp'] >= initial_training_end_date][0]
        
        total_len = len(df)
        
        while end_index < total_len:
            # Define the training period (6 months window)
            training_end_date = df.iloc[end_index]['timestamp']
            training_start_date = training_end_date - pd.DateOffset(days=lookback)
            
            training_df = df[(df['timestamp'] >= training_start_date) & (df['timestamp'] < training_end_date)].copy()
            
            if training_df.empty:
                break
            
            # Evaluate candidate conditions on the training period
            best_condition = None
            best_eer = 0
            best_training_dd = None
            
            for condition in self.conditions:
                temp_df = training_df.copy()
                temp_df = self.signal_generation(temp_df, condition=condition)
                temp_df = self.result(temp_df)
                
                # Calculate net profit for the period
                netProfit = temp_df['Equity'].iloc[-1] - temp_df['Equity'].iloc[0]
                
                # Compute maximum drawdown for training period
                peaks = np.maximum.accumulate(temp_df['Equity'])
                drawdowns = (temp_df['Equity'] - peaks) / peaks
                maxDrawdown = drawdowns.min()  # most negative value
                
                temp_df['Peak'] = peaks
                temp_df['Drawdown Phase'] = (temp_df['Equity'] < temp_df['Peak']).astype(int)
                temp_df['Drawdown Group'] = (temp_df['Drawdown Phase'].diff() == 1).cumsum()
                drawdown_durations = temp_df.groupby('Drawdown Group')['timestamp'].agg(['first', 'last'])
                drawdown_durations['duration'] = (drawdown_durations['last'] - drawdown_durations['first']).dt.days
                max_drawdown_duration = drawdown_durations['duration'].max() if not drawdown_durations.empty else 0
                
                totalTrades = len(df[df['Trade Closed']])
                        
                profitPercentage = round((netProfit / df.iloc[0]['Equity']) * 100)
                
                trade_strength = np.log(totalTrades + 1) if totalTrades > 0 else 0
                profit_target = 100
                if profitPercentage > 0:
                    profit_component = (profitPercentage / profit_target) * trade_strength
                    risk_penalty = (1 / (1 + abs(maxDrawdown))) * (1 / (1 + max_drawdown_duration))
                    eer = profit_component * risk_penalty
                else:
                    loss_component = (abs(profitPercentage) / profit_target) * trade_strength
                    eer = -loss_component
                eer = eer * 1000 # Just for more redability
                
                if eer > best_eer:
                    best_eer = eer
                    best_condition = condition
                    best_training_dd = maxDrawdown
            
            if best_condition is None:
                print("No valid condition found in training period.")
                break
            
            print(f"Training period {training_start_date.date()} to {training_end_date.date()}:")
            print(f"  Best condition: {best_condition}")
            print(f"  EER: {best_eer:.2f}, Training Max Drawdown: {best_training_dd:.2%}")
            
            # Define the testing period: starting at training_end_date until 6 months later
            testing_start_date = training_end_date
            testing_end_date = testing_start_date + pd.DateOffset(days=180)
            testing_df = df[(df['timestamp'] >= testing_start_date) & (df['timestamp'] < testing_end_date)].copy()
            
            if testing_df.empty:
                print("No data for testing period. Ending backtest.")
                break
            
            testing_df = self.signal_generation(testing_df, condition=best_condition)
            testing_df = self.result(testing_df, starting_capital = current_capital)

            # Monitor drawdown during the testing period:
            peaks_test = np.maximum.accumulate(testing_df['Equity'])
            drawdowns_test = (testing_df['Equity'] - peaks_test) / peaks_test
            
            # Find if (and when) the testing period drawdown becomes worse than the training period’s drawdown
            breach_index = None
            for i, dd in enumerate(drawdowns_test):
                if dd < best_training_dd:  # if current drawdown is worse (more negative) than training's max drawdown
                    breach_index = i
                    break
            
            if breach_index is not None:
                # Truncate testing period at the point of drawdown breach
                testing_df = testing_df.iloc[:breach_index]
                print(f"Testing period ended early at index {breach_index} due to drawdown breach.")

            # Append testing results to the overall results
            overall_results = pd.concat([overall_results, testing_df])
            
            # Update the current capital based on the last equity from the testing period
            current_capital = testing_df['Equity'].iloc[-1]
            
            # Update start_index to continue from the end of the current testing period
            if not testing_df.empty:
                last_test_timestamp = testing_df.iloc[-1]['timestamp']
                new_end = df[df['timestamp'] > last_test_timestamp].index.min()
                if pd.isna(new_end):
                    break
                end_index = new_end
            else:
                break

        # After looping, you can plot the overall equity curve
        print("Adaptive backtest completed.")
        
        self.plot_equity_curve(overall_results)
        self.metrics(overall_results)
        
    def ml_simulation(self):
        
        # PREPARE CLEAN DATA
        df = self.df.copy()
        
        print(f'Original Features (including timestamp): {len(df.columns)}')
        
        # DROP NOT USEFUL COLUMNS
        columns_to_drop = ['regime_type']
        df = df.drop(columns=columns_to_drop)
        
        # CONVERT ALL COLUMNS TO NUMERIC
        df['supertrend'] = df['supertrend'].apply(lambda x: 0 if x == -1.0 else 1 if x == 1.0 else x) # Convert -1, 1 to 0, 1
        
        datetime_cols = ['timestamp']
        categorical_cols = ['year', 'month', 'day_of_week', 'hour', 'minute', 'ma_trend', 'hl_oscillator', 'regime', 'relative_regime']
        cat_ordinal_cols = ['year', 'month', 'day_of_week', 'hour', 'minute'] # Normalize
        cat_nominal_cols = ['ma_trend', 'hl_oscillator', 'regime', 'relative_regime'] # One Hot Encode
        
        df = pd.get_dummies(df, columns = cat_nominal_cols) # Convert the categorical cols to seprate cols using One Hot Decode
        
        binary_cols = ['is_weekend', 'supertrend', 'bullish_engulfing', 'bearish_engulfing', 'hammer', 'doji', 'shooting_star']
        
        int_cols = df.select_dtypes(include=['int32', 'int64']).columns.tolist()
        for col in int_cols:
            df[col] = df[col].astype('float64')
        
        for col in df.columns[1:]:
            df[col] = df[col].astype('float64') # Convert bools to float
        
        # TARGET COLUMN
        df = df.copy()  # Defragment the DataFrame before adding new columns
        df['target'] = np.where(df['close'].shift(-1) > df['close'], 1, -1)

        non_nan_df = df.dropna()
        
        if not non_nan_df.empty:
            first_valid = non_nan_df.index[0]
            last_valid = non_nan_df.index[-1]
            df = df.loc[first_valid:last_valid]
        else:
            # Option 2: Fallback - remove fixed number of rows if auto-detection doesn't work.
            df = df.iloc[212:-1]
        
        # Normalize Binary Features, Ordinal Categorical Features especially time related features,
        # All Ordinal Categorical Features + Evenly distributed features without Outliers
        normalization_cols = ['year', 'month', 'day_of_week', 'hour', 'minute', 
                              'bullish_engulfing', 'bearish_engulfing', 
                              'hammer', 'shooting_star', 'doji', 'is_weekend', 'ma_trend_-1', 'ma_trend_0', 
                              'ma_trend_1', 'hl_oscillator_-1', 'hl_oscillator_0', 'hl_oscillator_1', 
                              'regime_-1', 'regime_0', 'regime_1', 'relative_regime_-1.0', 'relative_regime_0.0', 
                              'relative_regime_1.0', 'supertrend']
        
        yeo_trans = ['macd_line', 'signal_line', 'macd_histogram', 'cci', 'roc',
                     'supertrend_lowerband', 'stoploss_long', 'ma_df', 'ma_slope',
                     'ma_acceleration', 'ma_highest_acceleration', 'ma_acceleration_normalized',
                     'pullup_length', 'pulldown_length', 'ma_distance', 'regime_score'] # +ve -ve and 0 features
        
        box_trans = ['open', 'high', 'low', 'close', 'volume', 
                     'hma_200', 'sma_200', 'ema_200', 'sma_9', 'sma_20',
                     'rsi', 'stocastic_%k', 'stocastic_%d', 'ema_200_distance', 'sma_200_distance',
                     'hma_200_distance', '+dm', '-dm', 'typical_price', 'cum_price_vol',
                     'cum_vol', 'vwap', 'std', 'upper_bollinger_band', 'lower_bollinger_band', 
                     'bb_width', 'momentum', 'obv', 'psar', 'candle_length',
                     'tr_st', 'atr_st', 'supertrend_upperband', 'donchain_upperband', 
                     'donchain_lowerband', 'donchain_midline', 'tr', 'atr','atr_multiplier', 'stoploss_short',
                     'hh', 'hl', 'hc', 'ho', 'lh', 'll', 'lc', 'lo', 'vix'] # +ve only features
        
        # Standardize all other features after transforming them
        # Features with Outliers or non-even distribution
        standardization_cols = ['open', 'high', 'low', 'close', 'volume', 
                                'hma_200', 'sma_200', 'ema_200', 'sma_9', 'sma_20',
                                'rsi', '+dm', '-dm', 'macd_line', 'signal_line', 'macd_histogram',
                                'stocastic_%k', 'stocastic_%d', 'ema_200_distance', 'sma_200_distance',
                                'hma_200_distance', 'adx', 'cci', 'typical_price', 'cum_price_vol',
                                'cum_vol', 'vwap', 'std', 'upper_bollinger_band', 'lower_bollinger_band', 
                                'bb_width', 'momentum', 'obv', 'roc', 'psar', 'candle_length', 'pulldown_length',
                                'pullup_length', 'tr_st', 'atr_st', 'supertrend_upperband', 'supertrend_lowerband',
                                'donchain_upperband', 'donchain_lowerband', 'donchain_midline', 'tr', 'atr',
                                'atr_multiplier', 'stoploss_long', 'stoploss_short', 'ma_df', 'ma_slope',
                                'ma_acceleration', 'ma_highest_acceleration', 'ma_acceleration_normalized',
                                'hh', 'hl', 'hc', 'ho', 'lh', 'll', 'lc', 'lo', 'vix', 'ma_distance', 'regime_score'] # Standardization was recommended for PCA

        # TRANSFORMATION
        from sklearn.preprocessing import PowerTransformer
        pt_box = PowerTransformer(method='box-cox') # Transformation might not be good for Random Forest (Test with and without)
        pt_yeo = PowerTransformer(method='yeo-johnson')
        
        for feature in box_trans:
            if df[feature].min() <= 0:
                print(f"Feature {feature} contains non-positive values; switching to yeo-johnson transformation.")
                df[feature] = pt_yeo.fit_transform(df[[feature]])
            else:
                df[feature] = pt_box.fit_transform(df[[feature]])
        
        for feature in yeo_trans:
            df[feature] = pt_yeo.fit_transform(df[[feature]])

        # # SCALING
        from sklearn.preprocessing import StandardScaler
        from sklearn.preprocessing import MinMaxScaler
        
        norm_scaler = StandardScaler()
        df[normalization_cols] = norm_scaler.fit_transform(df[normalization_cols])
        
        stand_scaler = MinMaxScaler()
        df[standardization_cols] = stand_scaler.fit_transform(df[standardization_cols])

        # FEATURE IMPORTANCE / FEATURE SELECTION / DIMENTIONALITY REDUCTION / PCA
        
        # import seaborn as sns
        
        # # Compute the correlation matrix
        # corr_matrix = df.corr()
        
        # # Plot the heatmap for visualization
        # plt.figure(figsize=(12, 8))
        # sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', square=True)
        # plt.title("Feature Correlation Heatmap")
        # plt.show()
        
        # threshold = 0.9
        
        # high_corr_pairs = [(i, j) for i in corr_matrix.columns for j in corr_matrix.columns 
        #                 if i != j and abs(corr_matrix.loc[i, j]) > threshold]
        
        # to_drop = set([pair[1] for pair in high_corr_pairs])
        
        # df_final = df.drop(columns=to_drop)
        
        # # df_final.tail().to_csv("non_correlated_features.csv", index=False)
        
        # print(f'Non-Correlated Features : {df_final.columns}')
        
        df.reset_index(drop=True, inplace=True)
        # print(df.tail(2))
        
        numerical_df = df.iloc[:, 1:].copy() # Includes target but not timestamp
        non_target_numerical_df = df.iloc[:, 1:-1].copy()  # Selects all rows and all columns except the first and the last        
        
        # print(non_target_numerical_df.info())
        
        ##################    
        
        print(f'Features Before PCA: {len(df.columns) - 1}')
        
        from sklearn.decomposition import PCA
        
        pca = PCA()
        X_pca = pca.fit_transform(non_target_numerical_df)
        # # # print("Explained Variance Ratio:", pca.explained_variance_ratio_)
        # # # print("Cumulative Explained Variance:", pca.explained_variance_ratio_.cumsum())

        n_components = sum(pca.explained_variance_ratio_.cumsum() <= 0.95) + 1
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(non_target_numerical_df)
        df_pca = pd.DataFrame(X_pca, columns=[f'PC{i+1}' for i in range(n_components)]) # Dataframe with only new features
        
        new_df = pd.concat([df, df_pca], axis=1) # Old Features dataframe with extra features
        
        final_df = pd.concat([df[['timestamp']], df_pca, df[['target']]], axis=1)
        
        print(f'Features Generated: {n_components}')
        
        # final_df.to_csv('new_features_dataframe.csv')

        # print(new_df.info())
        
        # new_df.tail(10).to_csv('pca_dataframe.csv')
        
        # loadings = pd.DataFrame(pca.components_.T, columns=[f'PC{i+1}' for i in range(n_components)], index=non_target_numerical_df.columns)
        # loadings.to_csv('pca_feature_contribution.csv')

        #######################

        # BACKTEST PREDICTIONS ON TEST DATA
        
        # REGULARIZATION
        
        # VISUALIZATION
        
        # final_df = df
        
        X = final_df.drop(columns=['timestamp', 'target'])  # Can only check numeric columns
        y = final_df['target']  # Replace 'target' with your actual target column
        t = final_df['timestamp']
        
        train_size = int(len(final_df) * 0.8)  # 80% for training, 20% for testing
        
        X_train, X_test = X[:train_size], X[train_size:]
        y_train, y_test = y[:train_size], y[train_size:]
        t_train, t_test = t[:train_size], t[train_size:]
        
        
        def manual_timeseries_bootstramp(data, block_length=30, n_samples=1):
            n = len(data)
            bootstrap_samples = []
            
            for _ in range(n_samples - 1):
                # Randomly select starting indices for blocks
                start = np.random.randint(0, n - block_length)
                end = start + block_length
                
                sample = data.iloc[start:end]
                
                bootstrap_samples.append(sample)
            
            # Default one sample of the most recent data
            recent_sample = data.iloc[-block_length:]
            bootstrap_samples.append(recent_sample)
            
            return bootstrap_samples
        
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report

        bootstrap_samples = manual_timeseries_bootstramp(final_df, block_length=500, n_samples=5)
        
        for sample in bootstrap_samples:
            
            X = sample.drop(columns=['timestamp', 'target'])
            y = sample['target']
            t = sample['timestamp']
                
            train_size = int(len(sample) * 0.8)  # 80% for training, 20% for testing
            
            X_train, X_test = X[:train_size], X[train_size:]
            y_train, y_test = y[:train_size], y[train_size:]
            t_train, t_test = t[:train_size], t[train_size:]
            
            model = RandomForestClassifier(n_estimators=50, max_depth=10, min_samples_split=10, bootstrap=False, random_state=42)
            
            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)
            
            print(classification_report(y_test, y_pred))