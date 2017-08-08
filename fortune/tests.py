from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.MyPage, {'investment': 50})
        
        if self.player.lottery_outcome == 'heads':
            assert self.player.payoff == c(150)
        else:
            assert self.player.payoff == c(50)

        yield (views.Results)
