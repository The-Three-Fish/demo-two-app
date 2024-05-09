from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    number = models.IntegerField(
        label="Please choose a number between 0 and 500",
        min=0, max=500
    )


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['number']

    @staticmethod
    def before_next_page(player, timeout_happened):
        # 存储选择的数字到全局变量中
        player.participant.vars['chosen_number'] = player.number


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
