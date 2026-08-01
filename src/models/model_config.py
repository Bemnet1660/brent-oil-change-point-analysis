"""
Configuration for Bayesian change point models
"""
MODEL_CONFIG = {
    'default': {
        'draws': 2000,
        'tune': 1000,
        'chains': 4,
        'cores': 4,
        'target_accept': 0.95,
        'log_transform': True
    },
    'fast': {
        'draws': 500,
        'tune': 500,
        'chains': 2,
        'cores': 2,
        'target_accept': 0.90,
        'log_transform': False
    },
    'high_accuracy': {
        'draws': 4000,
        'tune': 2000,
        'chains': 4,
        'cores': 4,
        'target_accept': 0.99,
        'log_transform': True
    }
}
