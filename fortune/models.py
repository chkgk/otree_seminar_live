from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'fortune'
    players_per_group = None
    num_rounds = 1

    endowment = c(100)

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    investment = models.CurrencyField(verbose_name="How much to invest?")
    lottery_outcome = models.CharField(choices=['heads', 'tails'])

    def flip_and_calculate(self):
        self.lottery_outcome = random.choice(['heads', 'tails'])
        if self.lottery_outcome == "heads":
            self.payoff = Constants.endowment + self.investment
        else:
            self.payoff = Constants.endowment - self.investment