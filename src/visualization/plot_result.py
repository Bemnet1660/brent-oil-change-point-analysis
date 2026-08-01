"""
Visualization functions for change point analysis
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_time_series(df, title='Brent Oil Prices', save_path=None):
    """Plot price time series with optional rolling mean"""
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Price'], 'b-', alpha=0.6, label='Daily Price')
    if 'rolling_mean_30' in df.columns:
        plt.plot(df['Date'], df['rolling_mean_30'], 'r-', label='30-day MA')
    plt.xlabel('Date')
    plt.ylabel('Price (USD/barrel)')
    plt.title(title)
    plt.legend()
    plt.grid(alpha=0.3)
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def plot_change_point_summary(model, events_df, save_path=None):
    """Comprehensive summary plot with events overlaid"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    # (Implementation similar to the method in change_point.py)
    # Here we assume model has trace and data
    # We'll call model.plot_results internally
    model.plot_results(save_path=save_path)
