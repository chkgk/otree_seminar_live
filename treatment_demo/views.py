from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Investment(Page):
    form_model = models.Player
    form_fields = ['investment']

    def investment_max(self):
        return self.player.endowment

    def before_next_page(self):
        self.player.play_lottery()

class Results(Page):
    def vars_for_template(self):
        return {
            'outcome': "won" if self.player.lottery_won else "lost"
        }


page_sequence = [
    Investment,
    Results
]
