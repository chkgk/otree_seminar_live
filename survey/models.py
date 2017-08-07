from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Christian'

doc = """
Our first survey app.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.PositiveIntegerField(
        max=120,
        verbose_name="How old are you?",
        doc="collect age data between 0 and 120"
    )

    field_of_studies = models.CharField(
        blank=True,
        verbose_name="What do you study if at all?",
        doc="free text input of field of studies"
    )

    likes_experiment = models.CharField(
        choices=["Yes of course!", "No and I don't have a witty comment", "maybe"],
        widget=widgets.RadioSelect(),
        verbose_name="Did you like the experiment?",
        doc="yes, no , maybe input as a string"
    )
