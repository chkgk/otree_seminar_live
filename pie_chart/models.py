from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian König'

doc = """
An example app to demonstrate both highcharts as well as dynamic form validation
"""


class Constants(BaseConstants):
    name_in_url = 'pie_chart'
    players_per_group = None
    num_rounds = 1

    pie_size = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    p1_share = models.PositiveIntegerField(max=Constants.pie_size, widget=widgets.SliderInput(attrs={'step': '1'}))
    p2_share = models.PositiveIntegerField(max=Constants.pie_size)

    def set_p2_share(self):
        self.p2_share = Constants.pie_size - self.p1_share


class Player(BasePlayer):
    pass

