SESSION_CONFIGS = [
    dict(
        name='auction_game',
        app_sequence=['auction_game'],
        num_demo_participants=2,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0.00,
    doc=""
)

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
INSTALLED_APPS = ['otree']
