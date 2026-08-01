"""
Event data API routes
"""
from flask import Blueprint, jsonify, request
import pandas as pd
import os

event_bp = Blueprint('event', name, url_prefix='/api/events')

DATA_PATH = os.path.join(os.path.dirname(file), '../../../data/processed/')
events_df = pd.read_csv(os.path.join(DATA_PATH, 'events.csv'))
events_df['event_date'] = pd.to_datetime(events_df['event_date'])

@event_bp.route('/', methods=['GET'])
def get_events():
    return jsonify({
        'events': events_df.to_dict('records'),
        'count': len(events_df)
    })

@event_bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = events_df[events_df['event_id'] == event_id]
    if len(event) == 0:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify(event.to_dict('records')[0])
