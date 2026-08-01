"""
Price data API routes
"""
from flask import Blueprint, jsonify, request
import pandas as pd
import os

price_bp = Blueprint('price', name, url_prefix='/api/prices')

# Load data once (or use a global data loader)
DATA_PATH = os.path.join(os.path.dirname(file), '../../../data/processed/')
df = pd.read_csv(os.path.join(DATA_PATH, 'cleaned_oil_prices.csv'))
df['Date'] = pd.to_datetime(df['Date'])

@price_bp.route('/', methods=['GET'])
def get_prices():
    start = request.args.get('start_date')
    end = request.args.get('end_date')
    data = df.copy()
    if start:
        data = data[data['Date'] >= start]
    if end:
        data = data[data['Date'] <= end]
    return jsonify({
        'data': data.to_dict('records'),
        'count': len(data)
    })

@price_bp.route('/summary', methods=['GET'])
def get_summary():
    summary = {
        'min_price': float(df['Price'].min()),
        'max_price': float(df['Price'].max()),
        'mean_price': float(df['Price'].mean()),
        'std_price': float(df['Price'].std()),
        'start_date': df['Date'].min().strftime('%Y-%m-%d'),
        'end_date': df['Date'].max().strftime('%Y-%m-%d')
    }
    return jsonify(summary)
