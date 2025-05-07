import os
import importlib.util

import pandas as pd
import numpy as np
from queue import Queue

from PySide6.QtCore import QThread, Signal

class BacktestWorker(QThread):
    
    progress = Signal(int)
    finished = Signal(list, int)
    
    def __init__(self, backtester_class_instance):
        super().__init__()
        self.backtester_class = backtester_class_instance
    
    # Test dynamic loading and class identification
    def load_strategy_from_file(self, strategy_file_path):
        
        module_name = os.path.splitext(os.path.basename(strategy_file_path))[0]

        spec = importlib.util.spec_from_file_location(module_name, strategy_file_path)
        strategy_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(strategy_module)

        # Find subclass of BaseStrategy
        for attr_name in dir(strategy_module):
            attr = getattr(strategy_module, attr_name)
            if isinstance(attr, type) and attr_name != 'BaseStrategy':
                return attr

    def run_backtest(self, capital, strategy_filepaths_List, strategiesWidgetList, type, threshold, row, above_thresholds, result_queue):
        
        if not strategy_filepaths_List:
            print("No strategy files selected.")
            return
        
        strategies = []
        initial_capital = capital
        
        # Load each strategy from uploaded files
        for strategy_file_paths, strategy_widgets in zip(strategy_filepaths_List, strategiesWidgetList):
            
            # Unpack the widgets from the tuple
            stratagyWidget, strategyLabel, strategySelection, strategyVisibility, strategyEdit, strategyDelete = strategy_widgets
            
            # Unpack the elements from the tuple
            strategy_file_path, ohlcv_data = strategy_file_paths
            
            widget_list = ohlcv_data['widget']
            data = ohlcv_data['df']
            df_3m = ohlcv_data['df_3m']
            df_5m = ohlcv_data['df_5m']
            df_15m = ohlcv_data['df_15m']
            df_1H = ohlcv_data['df_1H']
            df_1D = ohlcv_data['df_1D']
            
            data = self.backtester_class.indicator_verification(widget_list, data, df_3m, df_5m, df_15m, df_1H, df_1D)
            
            # Check if the checkbox (strategySelection) is checked
            if strategySelection.isChecked():
                
                # If checked, load the strategy from the file
                StrategyClass = self.load_strategy_from_file(strategy_file_path)
                strategies.append((StrategyClass, data))
            
            else:
                print(f"Skipping strategy: {strategy_file_path} as its checkbox is unchecked.")
            
        initial_capital = capital
        risk_percent = 1
        cash = (capital * risk_percent) / 100
        
        strategiesList = []
        combined_df = pd.DataFrame()
        combined_dfSignals = pd.DataFrame()
        
        # Run each loaded strategy
        for StrategyClass, data in strategies:
            
            df = data.copy()
            
            strategy_instance = StrategyClass(df, capital, cash, risk_percent, threshold)
            print(f"Running strategy: {StrategyClass.__name__}")
            
            strategyName = StrategyClass.__name__
            
            try:
                equity, dfSignals, df = strategy_instance.run()
                
                # Store the equity and signals in a dictionary
                strategy_data = {
                    'strategy_name': strategyName,
                    'equity': equity,
                    'ohlcv':df,
                    'signals': dfSignals
                }        
                
                df = data.copy()
                
                strategiesList.append(strategy_data)
                
                self.finished.emit(strategiesList, initial_capital)
                
                combined_df = pd.concat([combined_df, df], ignore_index=True)
                combined_df = combined_df.drop_duplicates(subset=['timestamp'])
                
                combined_dfSignals = pd.concat([combined_dfSignals, dfSignals], ignore_index=True)
                
            except Exception as e:
                print(f"Error running strategy {StrategyClass.__name__}: {e}")
        
        if len(strategies) > 1:
            
            combined_dfSignals = combined_dfSignals.sort_values(by='timestamp')
            combined_df = combined_df.sort_values(by='timestamp')
            
            combined_dfSignals.reset_index(drop=True, inplace=True)
            combined_df.reset_index(drop=True, inplace=True)
            
            combined_dfSignals = combined_dfSignals.copy()
            combined_df = combined_df.copy()
            
            complete_df = pd.merge(combined_df, combined_dfSignals, on='timestamp', how='outer')
            
            complete_df = complete_df.sort_values(by='timestamp')
            
            timestamps = (complete_df['timestamp'].astype(np.int64) // 10**9).values
            results = complete_df['Result'].values
            rrs = complete_df['RR'].values
            reductions = complete_df['Reduction'].values
            commissioned_returns_combined = complete_df['Commissioned Returns'].values
            
            portfolio_equity = strategy_instance.portfolio(timestamps, results, rrs, reductions, commissioned_returns_combined)
            
            complete_df = complete_df.drop_duplicates(subset=['timestamp'])
            
            strategy_data = {
                'strategy_name': 'Portfolio',
                'equity': portfolio_equity,
                'ohlcv':complete_df,
                'signals': combined_dfSignals
            }
            
            strategiesList.append(strategy_data)
            
            self.backtester_class.add_strategy_widget('Portfolio', complete_df)
        
        if type == 'backtest':
            
            self.finished.emit(strategiesList, initial_capital)

            self.backtester_class.plot_results(strategiesList, initial_capital)
            
            self.backtester_class.metrics(strategiesList, initial_capital, type, threshold, row, above_thresholds)
            self.backtester_class.on_backtest_finished(strategiesList, initial_capital)
            
            result_queue.put(above_thresholds)

            print("BACKTEST FINISHED")
            
        elif type == 'optimization':
            
            self.finished.emit(strategiesList, initial_capital)
            
            above_thresholds = self.backtester_class.metrics(strategiesList, initial_capital, type, threshold, row, above_thresholds)
            
            result_queue.put(above_thresholds)