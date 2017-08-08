from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian'

doc = """
Our first survey app.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    weight = models.FloatField(min=0, verbose_name="Weight?")
    height = models.FloatField(min=0, verbose_name="Height?")

    bmi = models.FloatField()

    def calculate_bmi(self):
        self.bmi = round(self.weight / self.height**2, 2)
