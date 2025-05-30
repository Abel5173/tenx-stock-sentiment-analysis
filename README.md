# Stock Market Sentiment Analysis and Technical Analysis

This project combines sentiment analysis of stock-related news with technical analysis of historical stock data to provide comprehensive market insights.

## Project Structure

```
tenx-stock-sentiment-analysis/
├── data/
│   ├── yfinance_data/           # Historical stock data
│   │   ├── AAPL_historical_data.csv
│   │   ├── AMZN_historical_data.csv
│   │   ├── GOOG_historical_data.csv
│   │   ├── META_historical_data.csv
│   │   ├── MSFT_historical_data.csv
│   │   ├── NVDA_historical_data.csv
│   │   └── TSLA_historical_data.csv
│   └── raw_analyst_ratings.csv  # Analyst ratings data
├── notebooks/
│   ├── stock_data_eda.ipynb     # Exploratory Data Analysis
│   └── technical_analysis.ipynb  # Technical Analysis
├── scripts/
│   ├── indicators.py            # Technical indicators implementation
│   ├── signals.py              # Trading signals generation
│   ├── plot_utils.py           # Visualization utilities
│   └── portfolio.py            # Portfolio analysis
├── tests/                      # Unit tests
└── requirements.txt            # Python dependencies
```

## Features

### 1. Technical Analysis
- Moving Averages (SMA, EMA, WMA)
- Momentum Indicators (RSI, MACD, Stochastic Oscillator)
- Volatility Indicators (Bollinger Bands, ATR)
- Volume Indicators (OBV, MFI)

### 2. Data Analysis
- Historical price analysis
- Volume analysis
- Trend identification
- Support and resistance levels
- Market sentiment correlation

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start Jupyter Notebook:
```bash
jupyter notebook
```

## Usage

### Technical Analysis
1. Navigate to `notebooks/technical_analysis.ipynb`
2. Run the cells to:
   - Load historical stock data
   - Calculate technical indicators
   - Generate visualizations
   - Identify trading signals

### Exploratory Data Analysis
1. Navigate to `notebooks/stock_data_eda.ipynb`
2. Run the cells to:
   - Analyze price trends
   - Check data quality
   - Visualize market patterns
   - Identify correlations

## Technical Indicators

### Trend Indicators
- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Weighted Moving Average (WMA)

### Momentum Indicators
- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Stochastic Oscillator

### Volatility Indicators
- Bollinger Bands
- Average True Range (ATR)

### Volume Indicators
- On-Balance Volume (OBV)
- Money Flow Index (MFI)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Acknowledgments

- Data provided by Yahoo Finance
- Technical analysis indicators implemented using TA-Lib
- Visualization tools: Matplotlib and Seaborn
- Tenx Academy tutors
