from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König'

doc = """
My first Survey App
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
    age = models.PositiveIntegerField()
    gender = models.CharField(
        choices=['male', 'female', 'other', 'prefer not to tell'],
        widget=widgets.RadioSelectHorizontal
    )
    field_of_studies = models.CharField()
    height = models.FloatField()
    weight = models.FloatField()

    bmi = models.FloatField()
    bmi_classification = models.CharField()

    def calculate_bmi(self):
        self.bmi = round(self.weight / self.height**2, 2)

        if self.bmi  < 18.5:
            self.bmi_classification = 'underweight'
        elif self.bmi > 25:
            self.bmi_classification = 'overweight'
        else:
            self.bmi_classification = 'normal'