"""
Preprocessing utilities for oil price data
"""
import pandas as pd
import numpy as np

def clean_prices(df):
    """Handle missing values and ensure correct types"""
    df = df.copy()
    df['Price'] = df['Price'].astype(float)
    # Forward fill missing prices (if any)
    df['Price'] = df['Price'].fillna(method='ffill')
    return df

def compute_returns(df, log=True):
    """Compute returns (log or simple)"""
    df = df.copy()
    if log:
        df['log_return'] = np.log(df['Price'] / df['Price'].shift(1))
    else:
        df['simple_return'] = df['Price'].pct_change()
    return df

def add_rolling_features(df, windows=[30, 90, 180]):
    """Add rolling statistics"""
    df = df.copy()
    for w in windows:
        df[f'rolling_mean_{w}'] = df['Price'].rolling(w).mean()
        df[f'rolling_std_{w}'] = df['Price'].rolling(w).std()
    return df

if name == "main":
    from load_data import load_brent_prices
    df = load_brent_prices()
    df = clean_prices(df)
    df = compute_returns(df, log=True)
    df = add_rolling_features(df)
    df.to_csv('data/processed/cleaned_oil_prices.csv', index=False)
    print("Cleaned data saved to data/processed/cleaned_oil_prices.csv")
