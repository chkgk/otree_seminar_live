from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'prisoners_dilemma'
    players_per_group = 2
    num_rounds = 1

    # first level of list is one player's action, second level the other player's action
    symmetric_payoffs = [ [1, 3], 
                          [0, 2] ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def calculate_years_in_prison(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        p1.years_in_prison = Constants.symmetric_payoffs[p1.decision][p2.decision]
        p2.years_in_prison = Constants.symmetric_payoffs[p2.decision][p1.decision]

        p1.others_decision = p2.decision
        p2.others_decision = p1.decision


class Player(BasePlayer):
    decision = models.SmallIntegerField(
                choices=[[0, 'stay silent'], [1, 'betray']],
                verbose_name="I choose to:",
                widget=widgets.RadioSelect()
            )
    years_in_prison = models.PositiveIntegerField()

    others_decision = models.SmallIntegerField(
                choices=[[0, 'stay silent'], [1, 'betray']])