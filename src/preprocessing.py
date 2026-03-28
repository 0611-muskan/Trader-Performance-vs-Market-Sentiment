# src/preprocessing.py
import pandas as pd

def preprocess(sentiment, trades):
    # Strip spaces from column names
    sentiment.columns = sentiment.columns.str.strip()
    trades.columns = trades.columns.str.strip()

    # Convert sentiment date
    sentiment['Date'] = pd.to_datetime(sentiment['date'])
    sentiment['date'] = sentiment['Date'].dt.date

    # Convert trades timestamp
    trades['time'] = pd.to_datetime(trades['Timestamp IST'], format='mixed')
    trades['date'] = trades['time'].dt.date

    # Merge datasets on date
    merged = trades.merge(
        sentiment[['date', 'classification']],
        on='date',
        how='left'
    )

    # Rename column to match expected name
    merged = merged.rename(columns={'classification': 'Classification'})

    # Create win column
    merged['win'] = merged['Closed PnL'] > 0

    return merged