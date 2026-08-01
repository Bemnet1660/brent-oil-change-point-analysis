"""
Data models for API responses (simplified as dicts)
"""
class PricePoint:
    def init(self, date, price):
        self.date = date
        self.price = price
    
    def to_dict(self):
        return {'date': self.date.isoformat(), 'price': self.price}

class Event:
    def init(self, event_id, event_date, event_name, event_type, region, description, impact_estimate):
        self.event_id = event_id
        self.event_date = event_date
        self.event_name = event_name
        self.event_type = event_type
        self.region = region
        self.description = description
        self.impact_estimate = impact_estimate
    
    def to_dict(self):
        return {
            'event_id': self.event_id,
            'event_date': self.event_date.isoformat(),
            'event_name': self.event_name,
            'event_type': self.event_type,
            'region': self.region,
            'description': self.description,
            'impact_estimate': self.impact_estimate
        }

class ChangePoint:
    def init(self, date, before_mean, after_mean, percent_change):
        self.date = date
        self.before_mean = before_mean
        self.after_mean = after_mean
        self.percent_change = percent_change
    
    def to_dict(self):
        return {
            'date': self.date.isoformat(),
            'before_mean': self.before_mean,
            'after_mean': self.after_mean,
            'percent_change': self.percent_change
        }
