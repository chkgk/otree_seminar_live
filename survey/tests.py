from otree.api import Currency as c, currency_range
from otree.api import SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):

        # invalid age data should be rejected
        invalid_age_data = {
            'age': -1,             # age is negative
            'gender': 'male',
            'field_of_studies': 'Economics',
            'height': 2.00,
            'weight': 90.0
        }
        yield SubmissionMustFail(views.Demographics, invalid_age_data)


        # invalid gender inputs should also be rejected
        invalid_gender_data = {
            'age': 25,             
            'gender': 'monkey', # monkey is not an allowed input for the gender field
            'field_of_studies': 'Economics',
            'height': 2.00,
            'weight': 90.0
        }
        yield SubmissionMustFail(views.Demographics, invalid_gender_data)


        # valid data should pass
        valid_survey_data = {
            'age': 25,
            'gender': 'male',
            'field_of_studies': 'Economics',
            'height': 2.00,
            'weight': 90.0
        }
        yield (views.Demographics, valid_survey_data)

        # bmi should now be calculated for each player
        # formula: BMI = w / h^2
        # in our case: BMI = 90 / 2^2 = 90/4 = 22.5
        assert self.player.bmi == 22.5 
        assert self.player.bmi_classification == 'normal'

        # finally we should see the Results page. 
        yield (views.BMI_Result)