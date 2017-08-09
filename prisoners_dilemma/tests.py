from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    cases = ['silent_silent', 'betray_silent', 'silent_betray', 'betray_betray']

    def play_round(self):

        if self.player.id_in_group == 1:
            player_name = 'p1'
        else:
            player_name = 'p2'

        # we define one case for each possible choice combination
        # 0 means 'stay slient', 1 means 'betray'
        actions = {
            'silent_silent': { 'p1': 0, 'p2': 0},
            'betray_silent': { 'p1': 1, 'p2': 0},
            'silent_betray': { 'p1': 0, 'p2': 1},
            'betray_betray': { 'p1': 1, 'p2': 1}
        }

        # we also store correct payoffs for each case and each player
        years = {
            'silent_silent': { 'p1': 1, 'p2': 1},
            'betray_silent': { 'p1': 0, 'p2': 3},
            'silent_betray': { 'p1': 3, 'p2': 0},
            'betray_betray': { 'p1': 2, 'p2': 2}
        }

        # players choose actions depending on cases and their "name"
        yield (views.Decision, { 'decision': actions[self.case][player_name] })


        # check payoffs
        assert self.player.years_in_prison == years[self.case][player_name]


        yield (views.Results)
