"""
Load Brent oil price data from CSV
"""
import pandas as pd
import os

def load_brent_prices(file_path='data/raw/brent_oil_prices.csv'):
    """
    Load Brent oil price dataset.
    Expected columns: Date, Price
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")
    
    df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    df = df.sort_values('Date').reset_index(drop=True)
    return df

def load_events(file_path='data/processed/events.csv'):
    """Load events dataset"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Events file not found: {file_path}")
    df = pd.read_csv(file_path, parse_dates=['event_date'])
    return df

if name == "main":
    df = load_brent_prices()
    print(df.head())
    print(f"Total records: {len(df)}")
