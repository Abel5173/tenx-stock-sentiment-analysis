import talib
import pandas as pd


def add_trend_indicators(df):
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)
    df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)
    weights = list(range(1, 21))
    df['WMA_20'] = df['Close'].rolling(20).apply(lambda prices: (prices * weights).sum() / sum(weights), raw=True)
    return df

def add_momentum_indicators(df):
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)
    macd, macd_signal, _ = talib.MACD(df['Close'])
    df['MACD'] = macd
    df['MACD_Signal'] = macd_signal
    # Stochastic Oscillator
    slowk, slowd = talib.STOCH(df['High'], df['Low'], df['Close'])
    df['Stoch_K'] = slowk
    df['Stoch_D'] = slowd
    return df

def add_volatility_indicators(df):
    df['ATR_14'] = talib.ATR(df['High'], df['Low'], df['Close'], timeperiod=14)
    upper, middle, lower = talib.BBANDS(df['Close'], timeperiod=20)
    df['Upper_Band'] = upper
    df['Middle_Band'] = middle
    df['Lower_Band'] = lower
    return df

def add_volume_indicators(df):
    df['OBV'] = talib.OBV(df['Close'], df['Volume'])
    df['MFI'] = talib.MFI(df['High'], df['Low'], df['Close'], df['Volume'], timeperiod=14)
    return df
