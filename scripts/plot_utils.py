import matplotlib.pyplot as plt

def plot_price_and_sma(df, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close')
    plt.plot(df['SMA_20'], label='SMA 20')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()
