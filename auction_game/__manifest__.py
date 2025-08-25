from otree.api import *

doc = """
Auction experiment with 6 treatments and bot opponents.
"""

class C(BaseConstants):
    NAME_IN_URL = 'auction_game'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 60  # 6 experiments × 10 rounds
    EXPERIMENTS = [1, 2, 3, 4, 5, 6]
    ROUNDS_PER_EXPERIMENT = 10
    VALUATION_RANGE = [i / 100 for i in range(101)]  # 0 to 100

class Subsession(BaseSubsession):
    def creating_session(subsession):
        for player in subsession.get_players():
            player.experiment = ((player.round_number - 1) // C.ROUNDS_PER_EXPERIMENT) + 1

class Group(BaseGroup):
    valuation = models.FloatField()
    bot_valuation = models.FloatField()
    player_bid = models.FloatField()
    bot_bid = models.FloatField()
    winner = models.StringField()
    price_paid = models.FloatField()
    payoff = models.FloatField()

class Player(BasePlayer):
    experiment = models.IntegerField()

