import talib
import pandas as pd

def add_trend_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)
    return df

def add_momentum_indicators(df):
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
    macd, signal, _ = talib.MACD(df['Close'])
    df['MACD'] = macd
    df['MACD_Signal'] = signal
    return df

def add_volatility_indicators(df):
    df['ATR'] = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
    upper, middle, lower = talib.BBANDS(df['Close'], timeperiod=20)
    df['Upper_Band'] = upper
    df['Middle_Band'] = middle
    df['Lower_Band'] = lower
    return df

def add_volume_indicators(df):
    df['OBV'] = talib.OBV(df['Close'], df['Volume'])
    return df
