from otree.api import *
from .models import C, Subsession, Group, Player

class Instructions(Page):
    def is_displayed(player):
        return player.round_number == 1

class Bidding(Page):
    form_model = 'group'
    form_fields = ['bid_p1', 'bid_p2']

    def before_next_page(player, timeout_happened):
        group = player.group
        group.set_valuations()
        group.resolve_auction()

class Results(Page):
    def vars_for_template(player):
        group = player.group
        return dict(
            valuation=group.valuation_p1 if player.id_in_group == 1 else group.valuation_p2,
            bid=group.bid_p1 if player.id_in_group == 1 else group.bid_p2,
            opponent_bid=group.bid_p2 if player.id_in_group == 1 else group.bid_p1,
            payoff=group.payoff_p1 if player.id_in_group == 1 else group.payoff_p2,
            winner=group.winner,
            price_paid=group.price_paid,
        )

page_sequence = [Instructions, Bidding, Results]
