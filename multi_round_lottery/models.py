from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from random import random, randint

author = 'Christian König'

doc = """
Multi-Round lottery demo
"""


class Constants(BaseConstants):
    name_in_url = 'multi_round_lottery'
    players_per_group = None
    num_rounds = 3

    endowment = c(100)
    winning_probability = 1/3
    winning_return = 2.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    investment = models.CurrencyField(verbose_name="How much do you want to invest?")
    lottery_payoff = models.CurrencyField()
    lottery_won = models.BooleanField()
    selected_round = models.PositiveIntegerField()

    def play_lottery(self):
        if random() >= Constants.winning_probability:
            self.lottery_won = False
            self.lottery_payoff = Constants.endowment - self.investment
        else:
            self.lottery_won = True
            self.lottery_payoff = Constants.endowment + self.investment * (1 + Constants.winning_return)

    def pick_round(self):
        self.selected_round = randint(1, Constants.num_rounds)
        correct_player = self.in_round(self.selected_round)
        self.payoff = correct_player.lottery_payoff