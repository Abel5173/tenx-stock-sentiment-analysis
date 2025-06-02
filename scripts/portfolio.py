import matplotlib.pyplot as plt


def calculate_returns(price_df):
    return price_df.pct_change().dropna()


def calculate_portfolio_metrics(portfolio_returns, trading_days=252):
    annual_return = portfolio_returns.mean() * trading_days
    volatility = portfolio_returns.std() * (trading_days**0.5)
    sharpe_ratio = annual_return / volatility
    return annual_return, volatility, sharpe_ratio


def plot_portfolio_performance(portfolio_returns):
    """
    Plot the cumulative returns of a portfolio.

    Args:
        portfolio_returns (pd.Series): Daily returns of the portfolio.

    Returns:
        None. Displays the plot.
    """
    cumulative_returns = (1 + portfolio_returns).cumprod()

    plt.figure(figsize=(12, 6))
    plt.plot(cumulative_returns, label="Cumulative Return", color="navy")
    plt.title("📈 Cumulative Return of Equal-Weighted Portfolio")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1 Investment")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
