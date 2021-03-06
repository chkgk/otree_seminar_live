import os
from os import environ

import dj_database_url
#from boto.mturk import qualification

import otree.settings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


ADMIN_USERNAME = 'admin'

# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# don't share this with anybody.
SECRET_KEY = '3gg8no281h7zihe-0a==0lwj6)vf(o45b*ani$c$0k8g8oe70u'

DATABASES = {
    'default': dj_database_url.config(
        # Rather than hardcoding the DB parameters here,
        # it's recommended to set the DATABASE_URL environment variable.
        # This will allow you to use SQLite locally, and postgres/mysql
        # on the server
        # Examples:
        # export DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
        # export DATABASE_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

        # fall back to SQLite if the DATABASE_URL env var is missing
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}

# AUTH_LEVEL:
# If you are launching a study and want visitors to only be able to
# play your app if you provided them with a start link, set the
# environment variable OTREE_AUTH_LEVEL to STUDY.
# If you would like to put your site online in public demo mode where
# anybody can play a demo version of your game, set OTREE_AUTH_LEVEL
# to DEMO. This will allow people to play in demo mode, but not access
# the full admin interface.

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree', 'otreechat']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
oTree games
"""

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    # to use qualification requirements, you need to uncomment the 'qualification' import
    # at the top of this file.
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.000,
    'participation_fee': 0.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

ROOMS = [
    {
        'name': 'awi_lab',
        'display_name': 'AWI Experimentallabor',
        'participant_label_file': 'participant_labels.txt'
    }
]


SESSION_CONFIGS = [
    {
        'name': 'survey',
        'display_name': '1: Survey & BMI',
        'num_demo_participants': 1,
        'app_sequence': ['survey'],
        'participation_fee': 3.00
    },
    {
        'name': 'fortune',
        'display_name': '2: Fortune',
        'num_demo_participants': 1,
        'app_sequence': ['fortune'],
    },
    {
        'name': 'prisoners_dilemma',
        'display_name': "3: Prisoners' Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['prisoners_dilemma'],
    },
    {
        'name': 'ultimatum_game',
        'display_name': '4: Ultimatum game',
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum_game'],
    },
    {
        'name': 'treatment_demo',
        'display_name': '5: Treatment manipulation demo',
        'num_demo_participants': 2,
        'app_sequence': ['treatment_demo'],
        #'treatment': "high"
    },
    {
        'name': 'quiz',
        'display_name': '6: Quiz',
        'num_demo_participants': 1,
        'app_sequence': ['quiz'],
    },
    {
        'name': 'chat_example',
        'display_name': '7: A chat example',
        'num_demo_participants': 2,
        'app_sequence': ['chat_example']
    },
    {
        'name': 'pie_chart',
        'display_name': '8: A pie chart example using highcharts',
        'num_demo_participants': 1,
        'app_sequence': ['pie_chart']
    },
    {
        'name': 'multi_round_lottery',
        'display_name': 'Extra 1: Multi-round lottery',
        'num_demo_participants': 1,
        'app_sequence': ['multi_round_lottery']
    }
]



# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
