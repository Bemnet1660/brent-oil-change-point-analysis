"""
Helper functions
"""
import pandas as pd
import numpy as np

def compute_confidence_interval(samples, ci=0.95):
    """Compute highest density interval"""
    lower = (1 - ci) / 2
    upper = 1 - lower
    return np.percentile(samples, [lower*100, upper*100])

def format_currency(value):
    """Format price as USD with dollar sign"""
    return f"${value:,.2f}"

def date_to_index(df, date):
    """Get index of a specific date"""
    return df[df['Date'] == pd.Timestamp(date)].index[0] if date in df['Date'].values else None
