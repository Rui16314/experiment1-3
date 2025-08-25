from otree.api import *

doc = """
Auction experiments for ECON 3310.
"""

class C(BaseConstants):
    NAME_IN_URL = 'auction_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    valuation_p1 = models.FloatField()
    valuation_p2 = models.FloatField()
    bid_p1 = models.FloatField()
    bid_p2 = models.FloatField()
    winner = models.IntegerField()
    price_paid = models.FloatField()
    payoff_p1 = models.FloatField()
    payoff_p2 = models.FloatField()

class Player(BasePlayer):
    pass
