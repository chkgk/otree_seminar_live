from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Investment, {'investment': 50})
        if self.player.lottery_won:
            assert self.player.lottery_payoff == 275
        else:
            assert self.player.lottery_payoff == 50

        yield (views.LotteryResult)

        if self.round_number == Constants.num_rounds:
            yield (views.Results)
            assert self.player.payoff == self.player.in_round(self.player.selected_round).lottery_payoff
