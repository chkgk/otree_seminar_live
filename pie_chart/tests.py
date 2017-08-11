from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.AllocationDecision, {'p1_share': 20})
        assert self.group.p1_share == 20
        assert self.group.p2_share == 80

        yield (views.Results)
