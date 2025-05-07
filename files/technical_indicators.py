import pandas as pd
import numpy as np
from numba import njit
import pandas_ta as pta
import ta

class TechnicalIndicators:
    
    """
    A comprehensive class for calculating various technical indicators
    """
    
    def __init__(self):
        """Initialize the TechnicalIndicators class"""
        self._validate_columns = ['open', 'high', 'low', 'close', 'volume']
    
    def _validate_dataframe(self, df: pd.DataFrame) -> None:
        
        """
        Validate that the DataFrame has the required columns
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Raises:
            ValueError: If required columns are missing
        """
        
        missing_cols = [col for col in self._validate_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"DataFrame missing required columns: {missing_cols}")
    
    def _ensure_numeric(self, df: pd.DataFrame) -> pd.DataFrame:
        
        """
        Ensure all OHLCV columns are numeric
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            pd.DataFrame: DataFrame with numeric OHLCV columns
        """
        
        df_copy = df.copy()
        
        for col in self._validate_columns:
            df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce')
        
        return df_copy

    def calculate_moving_averages(self, df: pd.DataFrame, length = 100) -> pd.DataFrame:
        
        """Calculate various moving averages"""
        df = self._ensure_numeric(df)
        
        # Hull Moving Average
        half_length = int(length / 2)
        sqrt_length = int(np.sqrt(length))
        wma1 = df['close'].rolling(window=half_length).mean()
        wma2 = df['close'].rolling(window=length).mean()
        df[f'HMA_{length}'] = (2 * wma1 - wma2).rolling(window=sqrt_length).mean()
        
        # EMA
        df[f'EMA_{length}'] = ta.trend.ema_indicator(
            df['close'], length)
        
        # SMA
        df[f'SMA_{length}'] = ta.trend.sma_indicator(
            df['close'], length)
        
        # WMA
        df[f'WMA_{length}'] = ta.trend.wma_indicator(
            df['close'], length)
            
        return df

    def calculate_momentum_indicators(self, df: pd.DataFrame, length = 14, short_window = 12 , long_window = 26, signal_window = 9) -> pd.DataFrame:
        
        """Calculate momentum-based indicators"""
        df = self._ensure_numeric(df)
        
        # RSI
        df[f'RSI_{length}'] = ta.momentum.RSIIndicator(
            close=df['close'], window=length).rsi()
        
        # MACD
        macd = ta.trend.MACD(
            close=df['close'],
            window_slow=long_window,
            window_fast=short_window,
            window_sign=signal_window
        )
        df[f'MACD_LINE_{short_window}_{long_window}_{signal_window}'] = macd.macd()
        df[f'SIGNAL_LINE_{short_window}_{long_window}_{signal_window}'] = macd.macd_signal()
        df[f'MACD_HIST_{short_window}_{long_window}_{signal_window}'] = macd.macd_diff()
        
        # Stochastic
        stoch = pta.stoch(df['high'], df['low'], df['close'], k=length, d=3)
        df['Stochastic_%K'] = stoch.iloc[:, 0]
        df['Stochastic_%D'] = stoch.iloc[:, 1]
        
        return df

    def calculate_volatility_indicators(self, df: pd.DataFrame, length = 14, deviation = 2) -> pd.DataFrame:
        """Calculate volatility-based indicators"""
        df = self._ensure_numeric(df)
        
        # Bollinger Bands
        bb = ta.volatility.BollingerBands(
            close=df['close'],
            window=length,
            window_dev=deviation
        )
        df['BB_Upper'] = bb.bollinger_hband()
        df['BB_Middle'] = bb.bollinger_mavg()
        df['BB_Lower'] = bb.bollinger_lband()
        
        # ATR
        df['TR'] = ta.volatility.average_true_range(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            window=length
        )
        
        return df

    def calculate_trend_indicators(self, df: pd.DataFrame, length = 14, multiplier = 3) -> pd.DataFrame:
        """Calculate trend-based indicators"""
        df = self._ensure_numeric(df)
        
        # ADX
        adx = ta.trend.ADXIndicator(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            window=length
        )
        df['ADX'] = adx.adx()
        df['DI_plus'] = adx.adx_pos()
        df['DI_minus'] = adx.adx_neg()
        
        # Supertrend
        df = self._calculate_supertrend(df, length, multiplier)
        
        # Ichimoku Cloud
        ichimoku = ta.trend.IchimokuIndicator(
            high=df['high'],
            low=df['low'],
            window1=9,
            window2=26,
            window3=52
        )
        df['Ichimoku_Conversion_Line'] = ichimoku.ichimoku_conversion_line()
        df['Ichimoku_Base_Line'] = ichimoku.ichimoku_base_line()
        df['Ichimoku_A'] = ichimoku.ichimoku_a()
        df['Ichimoku_B'] = ichimoku.ichimoku_b()
        
        return df

    def calculate_volume_indicators(self, df: pd.DataFrame, length = 14) -> pd.DataFrame:
        """Calculate volume-based indicators"""
        df = self._ensure_numeric(df)
        
        # OBV
        df['OBV'] = ta.volume.on_balance_volume(df['close'], df['volume'])
        
        # VWAP
        df['typical_price'] = (df['high'] + df['low'] + df['close']) / 3
        df['VWAP'] = (df['typical_price'] * df['volume']).cumsum() / df['volume'].cumsum()
        
        # Chaikin Money Flow
        df['CMF'] = ta.volume.chaikin_money_flow(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            volume=df['volume'],
            window=length
        )
        
        # Money Flow Index
        df['MFI'] = ta.volume.money_flow_index(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            volume=df['volume'],
            window=length
        )
        
        return df

    def _calculate_supertrend(self, df: pd.DataFrame, period = 10, multiplier = 3) -> pd.DataFrame:
        """Helper method for Supertrend calculation"""
        atr = ta.volatility.AverageTrueRange(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            window=period
        ).average_true_range()
        
        # Basic bands
        basic_upper = ((df['high'] + df['low']) / 2) + (multiplier * atr)
        basic_lower = ((df['high'] + df['low']) / 2) - (multiplier * atr)
        
        # Initialize Supertrend
        supertrend = pd.Series(index=df.index, dtype='float64')
        direction = pd.Series(index=df.index, dtype='float64')
        
        # Calculate Supertrend
        for i in range(1, len(df)):
            if df['close'][i] > basic_upper[i-1]:
                supertrend[i] = basic_lower[i]
                direction[i] = 1
            elif df['close'][i] < basic_lower[i-1]:
                supertrend[i] = basic_upper[i]
                direction[i] = -1
            else:
                supertrend[i] = supertrend[i-1]
                direction[i] = direction[i-1]
        
        df['Supertrend'] = supertrend
        df['Supertrend_Direction'] = direction
        
        return df

    def calculate_candlestick_patterns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate various candlestick patterns"""
        df = self._ensure_numeric(df)
        
        # Basic patterns
        df['Doji'] = ta.candlestick.doji(
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )
        
        df['Hammer'] = ta.candlestick.hammer(
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )
        
        df['Shooting_Star'] = ta.candlestick.shooting_star(
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )
        
        # Advanced patterns
        df['Morning_Star'] = ta.candlestick.morning_star(
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )
        
        df['Evening_Star'] = ta.candlestick.evening_star(
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )
        
        return df

    def calculate_stop_loss(self, df: pd.DataFrame, length = 14, multiplier = 8) -> pd.DataFrame:
        """Calculate stop loss levels based on ATR"""
        df = self._ensure_numeric(df)
        
        atr = ta.volatility.AverageTrueRange(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            window=length
        ).average_true_range()
        
        df['Stop_Loss_Long'] = df['low'] - (atr * multiplier)
        df['Stop_Loss_Short'] = df['high'] + (atr * multiplier)
        
        return df

    @staticmethod
    def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
        
        """Add time-based features to the DataFrame"""
        if 'timestamp' not in df.columns:
            raise ValueError("DataFrame must have a 'timestamp' column")
            
        df['day_of_week'] = df['timestamp'].dt.day_name()
        df['day_of_week_num'] = df['timestamp'].dt.weekday
        df['hour_of_day'] = df['timestamp'].dt.hour
        df['is_weekend'] = df['day_of_week_num'].isin([5, 6])
        
        return df