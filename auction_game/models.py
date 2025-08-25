from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'auction_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 10
    VALUATION_RANGE = [i / 100 for i in range(10001)]

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

    def set_valuations(self):
        import random
        self.valuation_p1 = random.choice(C.VALUATION_RANGE)
        self.valuation_p2 = random.choice(C.VALUATION_RANGE)

    def resolve_auction(self):
        if self.bid_p1 > self.bid_p2:
            self.winner = 1
            self.price_paid = self.bid_p1  # first-price
            self.payoff_p1 = self.valuation_p1 - self.price_paid
            self.payoff_p2 = 0
        elif self.bid_p2 > self.bid_p1:
            self.winner = 2
            self.price_paid = self.bid_p2
            self.payoff_p2 = self.valuation_p2 - self.price_paid
            self.payoff_p1 = 0
        else:
            self.winner = 0
            self.price_paid = 0
            self.payoff_p1 = self.payoff_p2 = 0

class Player(BasePlayer):
    pass
