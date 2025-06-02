import matplotlib.pyplot as plt

def plot_price_and_sma(df, ticker='TICKER', sma_column='SMA_20'):
    """
    Plots the stock's closing price and a simple moving average (SMA).

    Parameters:
    - df: pandas DataFrame with a 'Close' column and SMA column (e.g., 'SMA_20')
    - ticker: string, the stock ticker (for the title)
    - sma_column: string, column name of the moving average to plot
    """
    if 'Close' not in df.columns or sma_column not in df.columns:
        print(f"Missing required columns in data for {ticker}")
        return

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price', linewidth=1.5)
    plt.plot(df.index, df[sma_column], label=sma_column, linestyle='--', alpha=0.8)

    plt.title(f"{ticker} - Price and {sma_column}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_cumulative_returns(returns_dict, title="Cumulative Returns by Stock"):
    """
    Plots cumulative returns for multiple stocks.

    Parameters:
    - returns_dict: dict of {ticker: pd.Series of daily returns}
    - title: str, title of the chart
    """
    plt.figure(figsize=(14, 6))

    for ticker, daily_returns in returns_dict.items():
        cumulative_returns = (1 + daily_returns).cumprod()
        plt.plot(cumulative_returns, label=ticker)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
