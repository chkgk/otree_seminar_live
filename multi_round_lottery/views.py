from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Investment(Page):
    form_model = models.Player
    form_fields = ['investment']

    def before_next_page(self):
        self.player.play_lottery()

class LotteryResult(Page):
    def vars_for_template(self):
        return {
            'outcome': "won" if self.player.lottery_won else "lost"
        }

    def before_next_page(self):
        if self.round_number == Constants.num_rounds:
            self.player.pick_round()

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        relevant_player = self.player.in_round(self.player.selected_round)

        return {
            'investment': relevant_player.investment,
            'outcome': "won" if relevant_player.lottery_won else "lost"
        }

page_sequence = [
    Investment,
    LotteryResult,
    Results
]
