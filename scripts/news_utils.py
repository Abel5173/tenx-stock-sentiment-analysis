import pandas as pd

def load_and_prepare_news(filepath='../data/raw_analyst_ratings.csv'):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date']).dt.date  # normalize timestamp to date only
    df['headline'] = df['headline'].astype(str).str.strip()

    # Remove empty or bad headlines
    df = df[df['headline'].str.len() > 3]
    df.dropna(subset=['headline'], inplace=True)

    return df
