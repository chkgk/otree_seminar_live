from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Christian König'

doc = """
A demonstration of how to implement different treatments
"""


class Constants(BaseConstants):
    name_in_url = 'treatment_demo'
    players_per_group = None
    num_rounds = 1

    high_endowment = c(1000)
    low_endowment = c(100)

    winning_probability = 1/3
    winning_return = 2.5


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for player in self.get_players():
            # half split by even / odd:
            # player.treatment = "low" if player.id % 2 == 0 else "high"

            # random selection
            # player.treatment = random.choice(['low', 'high'])

            # determined by session config, if present:
            if 'treatment' in self.session.config:
                player.treatment = self.session.config['treatment']
            else:
                player.treatment = random.choice(['low', 'high'])

            player.endowment = Constants.high_endowment if player.treatment == "high" else Constants.low_endowment




class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.CharField()
    endowment = models.CurrencyField()
    investment = models.CurrencyField(min=0, verbose_name="How much do you want to invest?")
    lottery_won = models.BooleanField()

    def play_lottery(self):
        if random.random() >= Constants.winning_probability:
            self.lottery_won = False
            self.payoff = self.endowment - self.investment
        else:
            self.lottery_won = True
            self.payoff = self.endowment + self.investment * (1 + Constants.winning_return)