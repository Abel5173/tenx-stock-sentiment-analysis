from textblob import TextBlob


def compute_sentiment(text):
    return TextBlob(text).sentiment.polarity


def add_sentiment_scores(df):
    df["sentiment"] = df["headline"].apply(compute_sentiment)
    return df
