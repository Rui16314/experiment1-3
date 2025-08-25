from otree.api import *
from .models import C, Subsession, Group, Player

class Instructions(Page):
    def is_displayed(player):
        return player.round_number == 1

class Bidding(Page):
    form_model = 'group'
    form_fields = ['player_bid']

    def before_next_page(player, timeout_happened):
        group = player.group
        group.set_valuations()
        group.set_bot_bid(player.experiment)
        group.resolve_auction(player.experiment)

class Results(Page):
    def vars_for_template(player):
        group = player.group
        return dict(
            valuation=group.valuation,
            bot_valuation=group.bot_valuation,
            player_bid=group.player_bid,
            bot_bid=group.bot_bid,
            winner=group.winner,
            price_paid=group.price_paid,
            payoff=group.payoff,
            experiment=player.experiment,
            round_in_exp=((player.round_number - 1) % C.ROUNDS_PER_EXPERIMENT) + 1
        )

page_sequence = [Instructions, Bidding, Results]

