from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.player.treatment == "low":
            assert self.player.endowment == c(100)
        else:
            assert self.player.endowment == c(1000)



        yield (views.Investment, {'investment': 50})

        if self.player.lottery_won:
            assert self.player.payoff == self.player.endowment + 3.5 * 50
        else:
            assert self.player.payoff == self.player.endowment - 50

        yield (views.Results)
