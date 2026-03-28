# Crypto Sentiment Analysis

## Overview
This project analyzes trader performance based on Fear vs Greed market sentiment indices. It correlates real trading data with sentiment indicators to identify performance patterns and trading opportunities.

## Objective
- Analyze trader performance across different sentiment periods
- Identify patterns in trading behavior during fear and greed cycles
- Generate actionable insights for sentiment-based trading strategies

## Project Structure
```
├── data/
│   ├── sentiment.csv          # Fear/Greed index data
│   └── trades.csv             # Historical trade data
├── src/
│   ├── data_loader.py         # Load CSV files
│   ├── preprocessing.py       # Data cleaning and merging
│   ├── analysis.py            # Metrics and sentiment analysis
│   └── visualization.py       # Chart generation
├── output/
│   └── charts/                # Generated visualizations
├── notebooks/
│   └── analysis.ipynb         # Interactive analysis notebook
├── main.py                    # Main execution script
└── requirements.txt           # Dependencies
```

## Methodology

### Data Collection & Preprocessing
- Collected historical trade data (`trades.csv`) and market sentiment data (`sentiment.csv`)
- Cleaned missing values and standardized timestamps for merging
- Categorized sentiment into 5 classes: Extreme Fear, Fear, Neutral, Greed, Extreme Greed

### Analysis Approach
1. Merged trade data with corresponding market sentiment
2. Calculated key metrics by sentiment category:
   - **PnL (Profit and Loss)** per trade
   - **Win Rate** by sentiment period
   - **Trade Frequency** distribution
   - **Long/Short Ratio** analysis
3. Segmented traders into:
   - Frequent vs Infrequent traders
   - Consistent vs Inconsistent performers

### Visualizations Generated
- PnL by sentiment class
- Win rate by sentiment class
- Trade frequency distribution
- Long/Short ratio heatmap by sentiment

## Key Findings

### Performance Insights
| Sentiment | Avg PnL | Win Rate | Trade Frequency |
|-----------|---------|----------|-----------------|
| Extreme Greed | $73.14 | 45.87% | ↑ Highest |
| Extreme Fear | $47.45 | 39.05% | Varies |
| Greed | $35.65 | 40.31% | High |
| Fear | $56.54 | 38.79% | Moderate |
| Neutral | $31.75 | 40.26% | Lower |

### Key Observations
1. **Highest PnL in Extreme Greed**: Traders made the most profit during bullish sentiment
2. **Strong Performance in Extreme Fear**: Contrarian strategies showed promise when others were risk-averse
3. **Lowest Performance During Neutral**: Stable markets offer fewer trading advantages
4. **Increased Activity During Greed**: Trade frequency peaks during positive sentiment periods

## Strategy Recommendations

1. **Sentiment-Based Position Sizing**
   - Increase exposure during Extreme Greed for momentum strategies
   - Reduce position size during Neutral periods

2. **Risk Management**
   - Implement hedging strategies during Neutral Market periods
   - Monitor stop-loss levels closely during Extreme Greed

3. **Contrarian Opportunities**
   - Consider contrarian plays in Extreme Fear markets
   - Accumulate assets when others are risk-averse

4. **Continuous Monitoring**
   - Adjust strategies dynamically based on sentiment changes
   - Maintain real-time sentiment analysis integration

## Installation & Setup

### Requirements
- Python 3.7+
- pandas, numpy, matplotlib, seaborn, scikit-learn

### Installation Steps
```bash
# Install dependencies
pip install -r requirements.txt

# Run the analysis
python main.py
```

## Output
Charts and results are saved in the `output/charts/` directory:
- `pnl.png` - PnL by sentiment
- `winrate.png` - Win rate by sentiment
- `trade_freq.png` - Trade frequency by sentiment
- `longshort_heatmap.png` - Long/Short ratio analysis

