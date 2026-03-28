# src/visualization.py
import matplotlib.pyplot as plt
import os
import seaborn as sns

sns.set(style="whitegrid")

def plot_bar(series, title, filename):
    plt.figure(figsize=(7,5))
    series.plot(kind='bar')
    plt.title(title)
    plt.tight_layout()
    os.makedirs("output/charts", exist_ok=True)
    plt.savefig(f"output/charts/{filename}.png")
    plt.close()

def plot_heatmap(df, title, filename):
    plt.figure(figsize=(8,6))
    sns.heatmap(df, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title(title)
    os.makedirs("output/charts", exist_ok=True)
    plt.savefig(f"output/charts/{filename}.png")
    plt.close()