def generate_combined_signals(df):
    buy = (
        (df['RSI_14'] < 30) &
        (df['MACD'] > df['MACD_Signal']) &
        (df['Close'] < df['Lower_Band'])
    )
    sell = (
        (df['RSI_14'] > 70) &
        (df['MACD'] < df['MACD_Signal']) &
        (df['Close'] > df['Upper_Band'])
    )
    df['Buy_Signal'] = buy
    df['Sell_Signal'] = sell
    return df


def generate_trading_signals(df):
    buy_conditions = (
        (df['RSI_14'] < 30) &
        (df['MACD'] > df['MACD_Signal']) &
        (df['Close'] < df['Lower_Band'])
        # Optionally: & (df['MFI'] < 20)
    )

    sell_conditions = (
        (df['RSI_14'] > 70) &
        (df['MACD'] < df['MACD_Signal']) &
        (df['Close'] > df['Upper_Band'])
        # Optionally: & (df['MFI'] > 80)
    )

    df['Buy_Signal'] = buy_conditions
    df['Sell_Signal'] = sell_conditions

    return df
