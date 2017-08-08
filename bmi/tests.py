from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


from otree.api import SubmissionMustFail



class PlayerBot(Bot):

    def play_round(self):
        # check invalid input handling

        for number in [1, 2, 3, 4]:
            yield SubmissionMustFail(views.MyPage, {'height': -number, 'weight': -5})

        yield (views.MyPage, { 'height': 1.00, 'weight': 100 })
        assert self.player.bmi == 100
        assert self.player.bmi_class == "overweight"

        yield(views.Results)
