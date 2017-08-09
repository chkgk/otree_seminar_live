from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_years_in_prison()


class Results(Page):
    def vars_for_template(self):
        return {
            'decision': 'stay silent' if self.player.decision == 0 else 'betray',
            'others_decision': 'stay silent' if self.player.others_decision == 0 else 'betray'
        }


page_sequence = [
    Decision,
    ResultsWaitPage,
    Results
]
