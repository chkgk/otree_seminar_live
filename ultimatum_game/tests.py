from otree.api import Currency as c, currency_range
from otree.api import SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    cases = ['accept', 'reject']

    def play_round(self):

        # check role assignment
        if self.player.id_in_group == 1:
            assert self.player.role() == 'proposer'
        
        if self.player.id_in_group == 2:
            assert self.player.role() == 'responder'

        # page 1
        yield (views.RoleAssignment)

        # page 2
        if self.player.role() == 'proposer':
            # proposer page
            yield SubmissionMustFail(views.Proposal, {'proposer_share': -5 }) # negative
            yield SubmissionMustFail(views.Proposal, {'proposer_share': 120 }) # larger than pot

            yield (views.Proposal, {'proposer_share': 60 })
            
            assert self.group.proposer_share == c(60)

        # page 3
        responder_decision = { 'accept': True, 'reject': False }
        payoffs = { 
            'proposer': {
                'accept': 60,
                'reject': 0
            },
            'responder': {
                'accept': 40,
                'reject': 0
            }
        }

        if self.player.role() == 'responder':
            yield (views.Response, { 'accepted': responder_decision[self.case]})
            if self.case == 'accept':
                assert self.group.accepted == True
            else:
                assert self.group.accepted == False

        # check if payoffs are correctly set:
        assert self.player.payoff == payoffs[self.player.role()][self.case]

        # page 4
        yield (views.Results)