from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'auction_game'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 60
    EXPERIMENTS = [1, 2, 3, 4, 5, 6]
    ROUNDS_PER_EXPERIMENT = 10
    VALUATION_RANGE = [i / 100 for i in range(101)]

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

    def set_valuations(self):
        self.valuation = random.choice(C.VALUATION_RANGE)
        self.bot_valuation = random.choice(C.VALUATION_RANGE)

    def set_bot_bid(self, experiment):
        if experiment in [1, 2, 3]:  # First-price
            self.bot_bid = round(self.bot_valuation / 2, 2)
        else:  # Second-price
            self.bot_bid = self.bot_valuation

    def resolve_auction(self, experiment):
        if self.player_bid > self.bot_bid:
            self.winner = 'You'
            self.price_paid = self.player_bid if experiment in [1, 2, 3] else self.bot_bid
            self.payoff = round(self.valuation - self.price_paid, 2)
        elif self.bot_bid > self.player_bid:
            self.winner = 'Bot'
            self.price_paid = self.bot_bid if experiment in [1, 2, 3] else self.player_bid
            self.payoff = 0
        else:
            self.winner = 'Tie'
            self.price_paid = 0
            self.payoff = 0

class Player(BasePlayer):
    experiment = models.IntegerField()
