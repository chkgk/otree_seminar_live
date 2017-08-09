from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age', 'gender', 'field_of_studies', 'height', 'weight']

    def before_next_page(self):
        self.player.calculate_bmi()

class BMI_Result(Page):
    pass


page_sequence = [
    Demographics,
    BMI_Result
]
