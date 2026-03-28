import pandas as pd

def load_data():
    sentiment = pd.read_csv("data/sentiment.csv")
    trades = pd.read_csv("data/trades.csv")

    print("Sentiment Shape:", sentiment.shape)
    print("Trades Shape:", trades.shape)

    return sentiment, trades