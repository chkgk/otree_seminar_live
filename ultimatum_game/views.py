from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class RoleAssignment(Page):
    pass


class Proposal(Page):
    form_model = models.Group
    form_fields = ['proposer_share']

    timeout_seconds = 60
    timeout_submission = { 'proposer_share': 0 }


    def is_displayed(self):
        return self.player.role() == 'proposer'


class ResponderWaits(WaitPage):
    pass


class Response(Page):
    form_model = models.Group
    form_fields = ['accepted']

    def is_displayed(self):
        return self.player.role() == 'responder'

    def vars_for_template(self):
        return {'remainder': Constants.pot_size - self.group.proposer_share }


class ProposerWaits(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_payoffs()


class Results(Page):
    pass


page_sequence = [
    RoleAssignment,
    Proposal,
    ResponderWaits,
    Response,
    ProposerWaits,
    Results
]
