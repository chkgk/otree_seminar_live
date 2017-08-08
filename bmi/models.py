from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
BMI calculation and classification 
"""


class Constants(BaseConstants):
    name_in_url = 'bmi'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    height = models.FloatField(verbose_name="Height?")
    weight = models.FloatField(verbose_name="Weight?")

    bmi = models.FloatField()
    bmi_class = models.CharField()

    def calculate_bmi(self):
        self.bmi = round(self.weight / self.height**2,2)

    def classify_bmi(self):
        if self.bmi < 18.5:
            self.bmi_class = "underweight"

        if self.bmi > 25:
            self.bmi_class = "overweight"

         if 18.5 <= self.bmi <= 25:
            self.bmi_class = "normal"  
