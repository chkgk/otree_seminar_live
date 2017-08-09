from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König'

doc = """
Ultimatum Game
"""


class Constants(BaseConstants):
    name_in_url = 'ultimatum_game'
    players_per_group = 2
    num_rounds = 1

    pot_size = c(100)

class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.group_randomly()


class Group(BaseGroup):
    proposer_share = models.CurrencyField(
        min=0, max=Constants.pot_size, 
        verbose_name="How much would you like to keep for yourself?"
    )

    accepted = models.BooleanField(
        choices=[(True, 'Yes'), (False, 'No')], 
        verbose_name="Accept the proposal?"
    )

    def calculate_payoffs(self):
        proposer = self.get_player_by_role('proposer')
        responder = self.get_player_by_role('responder')

        
        if self.accepted:
            proposer.payoff = self.proposer_share
            responder.payoff = Constants.pot_size - self.proposer_share
        else:
            proposer.payoff = c(0)
            responder.payoff = c(0)


class Player(BasePlayer):
    payoff = models.CurrencyField(min=0, max=Constants.pot_size)

    def role(self):
        if self.id_in_group == 1:
            return 'proposer'
        
        if self.id_in_group == 2:
            return 'responder'

