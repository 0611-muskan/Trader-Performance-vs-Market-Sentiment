# src/analysis.py
import pandas as pd

def compute_metrics(df):
    metrics = {}

    # Daily PnL per trader
    metrics['daily_pnl'] = df.groupby(['Account', 'date'])['Closed PnL'].sum()

    # Win rate per trader
    metrics['win_rate'] = df.groupby('Account')['win'].mean()

    # Average trade size per trader
    metrics['avg_trade_size'] = df.groupby('Account')['Size USD'].mean()

    # Trades per day
    metrics['trades_per_day'] = df.groupby('date').size()

    # Long/Short ratio overall
    metrics['long_short_ratio'] = df['Side'].value_counts(normalize=True)

    return metrics

def sentiment_analysis(df):
    analysis = {}

    # PnL and Win rate by sentiment
    analysis['pnl_by_sentiment'] = df.groupby('Classification')['Closed PnL'].mean()
    analysis['win_by_sentiment'] = df.groupby('Classification')['win'].mean()

    # Trade frequency per sentiment
    analysis['trades_by_sentiment'] = df.groupby('Classification').size()

    # Long/short ratio per sentiment
    analysis['long_short_by_sentiment'] = pd.crosstab(
        df['Classification'], df['Side'], normalize='index'
    )

    return analysis

def segmentation(df):
    # Frequent vs Infrequent traders
    trade_counts = df.groupby('Account').size()
    median_trades = trade_counts.median()
    freq_map = trade_counts.apply(lambda x: 'Frequent' if x > median_trades else 'Infrequent')

    # Consistent winners vs inconsistent
    consistency = df.groupby('Account')['win'].mean()
    consistency_map = consistency.apply(lambda x: 'Consistent' if x > 0.6 else 'Inconsistent')

    return df, freq_map, consistency_map