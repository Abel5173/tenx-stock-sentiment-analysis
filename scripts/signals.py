def generate_buy_signals(df):
    return (df['RSI_14'] < 30) & (df['MACD'] > df['MACD_Signal']) & (df['Close'] < df['Lower_Band'])

def generate_sell_signals(df):
    return (df['RSI_14'] > 70) & (df['MACD'] < df['MACD_Signal']) & (df['Close'] > df['Upper_Band'])
