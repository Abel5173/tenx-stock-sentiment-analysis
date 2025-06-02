import os
import pandas as pd

def load_yfinance_data(data_dir='../data/yfinance_data'):
    stock_data = {}
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            stock_name = file.replace('_historical_data.csv', '')
            df = pd.read_csv(os.path.join(data_dir, file))
            df['Date'] = pd.to_datetime(df['Date'])
            df.sort_values('Date', inplace=True)
            df.set_index('Date', inplace=True)
            stock_data[stock_name] = df
    return stock_data
