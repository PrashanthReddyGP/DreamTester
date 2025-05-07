from classes.basestrategy import BaseStrategy
from numba import jit
import numpy as np
from numba import objmode
import matplotlib.pyplot as plt
import pandas as pd

class BTC_SMA_CROSSOVER_LONG_STRATEGY(BaseStrategy):
    
    def __init__(self, df=None, capital=1000, cash=10, risk_percent=1, optim_number=1,\
        symbol='BTCUSDT', timeframe='1h', start_date='2000-01-01', end_date='2100-12-31'):
        
        super().__init__(df, capital, cash, risk_percent, optim_number, symbol, timeframe, start_date, end_date)
        
        self.symbol = 'BTCUSDT'
        self.timeframe = '1h'
        
        self.rr = 1
        
        self.indicators = [
            ('SMA', '1m', (100,)),
            ('SMA', '1m', (200,)),
            ('ATR', '1m', (14, 4)),
            ]
    
    def optimized_run(self):
        super().optimized_run() # Call the parent class's optimized_run
        
        # Run the optimized backtest
        (commission, no_fee, self.trade_closed, self.result, self.exit_time, self.open_trades, self.signals, self.equity, timestamp1, wins, timestamp2, losses, \
            self.returns, self.commissioned_returns, self.entry, self.takeprofit, self.stoploss, \
                self.max_drawdown, self.drawdown_duration, self.max_pull_up, self.pull_up_duration, self.avg_volatility) = self.optimizer_CLOSE(
            self.open, self.high, self.low, self.close, self.timestamp, self.initial_capital, self.risk_percent, self.rr,
            
            # ADD THE INDICATORS AS VALUES BELOW
            self.df['sma_100'].values,
            self.df['sma_200'].values,
            self.df['stoploss_long'].values,
            self.df['atr_pct'].values
        )
        
        print(f"Commission: {commission}%, Net without fee: {round(no_fee[-1] - no_fee[0])}, Net with fee: {round(self.equity[-1] - self.equity[0])}")
        
        timestamp1 = pd.to_datetime(np.where(timestamp1 == 0.0, pd.NaT, timestamp1), unit='s')
        timestamp2 = pd.to_datetime(np.where(timestamp2 == 0.0, pd.NaT, timestamp2), unit='s')
        
        # print(np.sum(wins==1), np.sum(losses==1)) # (round(np.sum(wins==1) / np.sum(losses==1) * 100))
        
        # self.plot_results(timestamp1, wins, timestamp2, losses)

    @staticmethod
    @jit(nopython=True)
    def optimizer_CLOSE(open, high, low, close, timestamp, initial_capital, risk_percent, rr, short_sma, long_sma, stop_loss, atr): # Make sure to define indicator variables here
        
        n = len(close)
        
        capital = initial_capital
        no_fee_capital = initial_capital
        
        cash = (capital * risk_percent) / 100
                
        entry = np.zeros(n)
        takeprofit = np.zeros(n)
        stoploss = np.zeros(n)
        
        trade_closed = np.zeros(n)
        result = np.zeros(n)
        exit_time = np.zeros(n)
        open_trades = np.zeros(n)
        signals = np.zeros(n)
        
        # Pre-allocate NumPy array
        equity = np.zeros(n)
        equity[0] = initial_capital
        
        no_fee_equity = np.zeros(n)
        no_fee_equity[0] = initial_capital
        
        returns = np.zeros(n)
        commissioned_returns = np.zeros(n)
        
        max_drawdown = np.zeros(n)
        drawdown_duration = np.zeros(n)
        max_pull_up = np.zeros(n)
        pull_up_duration = np.zeros(n)
        avg_volatility = np.zeros(n)
        
        trade_number = 0
        last_trade = 0
        
        timestamp1 = np.zeros(n)
        wins = np.zeros(n)
        timestamp2 = np.zeros(n)
        losses = np.zeros(n)
        
        sorted_atr = np.sort(atr)
        index = int(0.75 * len(atr))
        if index >= len(atr):
            index = len(atr) - 1
        volatility_cap = sorted_atr[index]
        
        firstTime = 1
        
        number = 0
        
        for i in range(1, n):
            
            # Entry condition: Short SMA crosses below Long SMA
            if short_sma[i-1] < long_sma[i-1] and short_sma[i] > long_sma[i] and open_trades[i] < 1: # Replace the ENTRY CONDITION
            
                distance = high[i] - low[i] / atr[i]
                
                signals[i] = 1
                trade_number += 1
                
                entry_price = close[i]
                initial_tp = entry_price + ((entry_price - stop_loss[i]) * rr)
                entry[i] = entry_price
                takeprofit[i] = initial_tp
                stoploss[i] = stop_loss[i]
                
                current_position_size = cash / (close[i] - stop_loss[i])
                
                max_price = entry_price
                min_price = entry_price
                stop_loss_hit = False
                atr_values_during_trade = []
                
                if last_trade == 1:
                    remaining_position_size = (current_position_size)
                elif last_trade == -1:
                    remaining_position_size = (current_position_size)
                else:
                    remaining_position_size = current_position_size
                
                fee = 0.001 * (entry_price * remaining_position_size) # Adjust based on the fee structure
                
                for j in range(i+1, n):
                    
                    max_price = max(max_price, high[j])
                    min_price = min(min_price, low[j])
                    atr_values_during_trade.append(atr[j])
                    
                    open_trades[j] += 1
                    
                    if high[j] >= initial_tp:
                        trade_closed[i] = 1
                        trade_return = (initial_tp - entry_price) * remaining_position_size
                        net_trade_return = trade_return - fee
                        
                        capital += net_trade_return
                        no_fee_capital += trade_return
                        
                        result[i] = 1
                        last_trade = 1
                        
                        cash = (capital * risk_percent) / 100
                                                
                        exit_time[i] = timestamp[j]
                        
                        timestamp1[i] = timestamp[i]
                        wins[i] = distance
                        
                        returns[i] = round(trade_return, 2)
                        commissioned_returns[i] = round(net_trade_return, 2)
                        
                        break
                    
                    # Exit condition: Trailing stop hit
                    elif low[j] <= stop_loss[i]:
                        
                        stop_loss_hit = True
                        
                        trade_closed[i] = 1
                        exit_time[i] = timestamp[j]
                        
                        result[i] = -1
                        last_trade = -1
                        trade_return = (stop_loss[i] - entry_price) * remaining_position_size
                        net_trade_return = trade_return - fee  # Fee for half position
                        
                        capital += net_trade_return
                        no_fee_capital += trade_return
                        
                        cash = (capital * risk_percent) / 100
                                                
                        if firstTime == 0:
                            timestamp2[i] = timestamp[i]
                            losses[i] = distance
                        
                        firstTime = 0
                        
                        returns[i] = round(trade_return, 2)
                        commissioned_returns[i] = round(net_trade_return, 2)
                        
                        break
                
                if stop_loss_hit:
                    max_pull_up[i] = round(((entry_price - min_price) / (entry_price - initial_tp)) * 100) if min_price < entry_price else 0
                    pull_up_duration[i] = timestamp[j] - timestamp[i]
                else:
                    max_drawdown[i] = round(((max_price - entry_price) / (stop_loss[i] - entry_price)) * 100) if max_price > entry_price else 0
                    drawdown_duration[i] = timestamp[j] - timestamp[i]
                
                if len(atr_values_during_trade) > 0:
                    atr_array = np.array(atr_values_during_trade)
                    atr_avg = np.mean(atr_array)
                    avg_volatility[i] = round((atr_avg / entry_price) * 100, 2)        
            
            no_fee_equity[i] = no_fee_capital
            equity[i] = capital
        
        commission = round(
            (((no_fee_equity[-1] - no_fee_equity[0]) - (equity[-1] - equity[0])) * 100) /
            (no_fee_equity[-1] - no_fee_equity[0]),
            2
        )
        
        return commission, no_fee_equity, trade_closed, result, exit_time, open_trades, signals, equity, timestamp1, wins, timestamp2, losses, returns, \
            commissioned_returns, entry, takeprofit, stoploss, max_drawdown, drawdown_duration, max_pull_up, pull_up_duration, avg_volatility

    def optimized_exit(self):
        super().optimized_exit() # Call the parent class's optimized_exit
        
        # Run the optimized backtest
        (self.trade_closed, self.result, self.exit_time, self.open_trades, self.signals, self.equity, \
            self.returns, self.commissioned_returns, self.entry, self.takeprofit, self.stoploss, \
                self.max_drawdown, self.drawdown_duration, self.max_pull_up, self.pull_up_duration, self.avg_volatility) = self.optimizer_OPEN(
            self.open, self.high, self.low, self.close, self.timestamp, self.initial_capital, self.risk_percent, self.rr,
            
            # ADD THE INDICATORS AS VALUES BELOW
            self.df['hl_oscillator'].values,
            self.df['hh'].values,
            self.df['hc'].values,
            self.df['sma_9'].values,
            self.df['sma_50'].values,
            self.df['sma_100'].values,
            self.df['stoploss_short'].values,
            self.df['atr'].values,
            self.optim_number
        )
    
    @staticmethod
    @jit(nopython=True)
    def optimizer_OPEN(open, high, low, close, timestamp, initial_capital, risk_percent, rr, hl_oscillator, hh, hc, signal_sma, short_sma, long_sma, stop_loss, atr, optim_number): # Make sure to define indicator variables here
        
        n = len(close)
        capital = initial_capital
        cash = (capital * risk_percent) / 100
        trade_closed = np.zeros(n)
        result = np.zeros(n)
        exit_time = np.zeros(n)
        open_trades = np.zeros(n)
        signals = np.zeros(n)
        
        entry = np.zeros(n)
        takeprofit = np.zeros(n)
        stoploss = np.zeros(n)
        
        returns = np.zeros(n)
        commissioned_returns = np.zeros(n)
        
        max_drawdown = np.zeros(n)
        drawdown_duration = np.zeros(n)
        max_pull_up = np.zeros(n)
        pull_up_duration = np.zeros(n)
        avg_volatility = np.zeros(n)
        
        # Pre-allocate NumPy array
        equity = np.zeros(n)
        equity[0] = initial_capital
        
        position_size = 0
        
        trade_number = 0
        last_trade = 0
        
        for i in range(1, n):
            
            if short_sma[i] > long_sma[i] and signal_sma[i-1] > long_sma[i-1] and signal_sma[i] < long_sma[i]: # Replace the ENTRY CONDITION
                
                signals[i] = 1
                
                entry_price = close[i]
                entry[i] = entry_price
                
                # position_size = cash / entry_price
                
                if last_trade == 1:    
                    position_size = (cash / entry_price)
                else:
                    position_size = (cash / entry_price)
                
                for j in range(i+1, n):
                    
                    open_trades[j] += 1
                    
                    if close[j] > hc[i-1]: # Replace the EXIT CONDITION
                        
                        trade_closed[i] = 1
                        exit_price = close[j]
                        
                        trade_return = (exit_price - entry_price) * position_size
                        
                        fee = 0.001 * (entry_price * position_size) # 0.1% fee on total position
                        net_trade_return = trade_return - fee
                        
                        if trade_return > 0:
                            result[i] = 1
                            last_trade = 1
                        else:
                            result[i] = -1
                            last_trade = -1
                        
                        exit_time[i] = timestamp[j]
                        
                        capital += net_trade_return
                        cash = ((capital * risk_percent) / 100)
                        
                        trade_number += 1
                        
                        # with objmode:
                        #     print(f'Trade : {trade_number}, Return : {trade_return}')
                        
                        break
            
            equity[i] = capital
        
        return trade_closed, result, exit_time, open_trades, signals, equity, returns, \
            commissioned_returns, entry, takeprofit, stoploss, max_drawdown, drawdown_duration, max_pull_up, pull_up_duration, avg_volatility
        
    def plot_results(self, timestamp1, wins, timestamp2, losses):
        # Plotting the scatter plot
        plt.figure(figsize=(10, 5))
        plt.gca().set_facecolor('black')
        plt.scatter(timestamp1, wins, color='g', label='Win')
        plt.scatter(timestamp2, losses, color='r', label='Loss')
        plt.title('Scatter Plot of Large Set of Numbers')
        plt.xlabel('TIMESTAMP')
        plt.ylabel('Values')
        plt.grid(True, color='gray', linestyle='-', linewidth=0.5)
        plt.legend()
        plt.show()