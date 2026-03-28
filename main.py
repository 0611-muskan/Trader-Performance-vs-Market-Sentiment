# main.py
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.analysis import compute_metrics, sentiment_analysis, segmentation
from src.visualization import plot_bar, plot_heatmap

def main():
    # Load data
    sentiment, trades = load_data()

    # Preprocess
    df = preprocess(sentiment, trades)
    print("\nData after merge:", df.shape)

    # Part A: Key Metrics
    metrics = compute_metrics(df)
    print("\nLong/Short ratio:\n", metrics['long_short_ratio'])

    # Part B: Sentiment Analysis
    sentiment_res = sentiment_analysis(df)
    print("\nPnL by Sentiment:\n", sentiment_res['pnl_by_sentiment'])
    print("\nWin Rate by Sentiment:\n", sentiment_res['win_by_sentiment'])

    # Plots
    plot_bar(sentiment_res['pnl_by_sentiment'], "PnL by Sentiment", "pnl")
    plot_bar(sentiment_res['win_by_sentiment'], "Win Rate by Sentiment", "winrate")
    plot_bar(sentiment_res['trades_by_sentiment'], "Trades by Sentiment", "trade_freq")
    plot_heatmap(sentiment_res['long_short_by_sentiment'], "Long/Short Ratio by Sentiment", "longshort_heatmap")

    # Part B: Segmentation
    df, freq_map, consistency_map = segmentation(df)
    print("\nSegmentation examples:")
    print("\nFrequent vs Infrequent:\n", freq_map.value_counts())
    print("\nConsistent vs Inconsistent:\n", consistency_map.value_counts())

    # Part C: Actionable Rules
    print("\nSuggested Rules:")
    print("1. During Fear/Extreme Fear days, reduce leverage and trade cautiously.")
    print("2. During Greed/Extreme Greed days, high-leverage traders can increase exposure but monitor stop-loss.")
    print("3. Frequent, consistent traders perform better with moderate leverage; infrequent traders should reduce risk.")

    print("\nCharts saved in output/charts/")

if __name__ == "__main__":
    main()