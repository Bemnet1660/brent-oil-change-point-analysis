"""
Map change points to events
"""
import pandas as pd
import numpy as np

def map_change_points_to_events(cp_dates, events_df, window_days=30):
    """
    For each change point, find events within a time window.
    Returns a DataFrame with associations.
    """
    results = []
    for cp_date in cp_dates:
        # Filter events within window
        mask = (events_df['event_date'] >= cp_date - pd.Timedelta(days=window_days)) & \
               (events_df['event_date'] <= cp_date + pd.Timedelta(days=window_days))
        matched = events_df[mask].copy()
        if len(matched) > 0:
            matched['change_point_date'] = cp_date
            matched['days_offset'] = (matched['event_date'] - cp_date).dt.days
            results.append(matched)
    if results:
        return pd.concat(results, ignore_index=True)
    else:
        return pd.DataFrame()
