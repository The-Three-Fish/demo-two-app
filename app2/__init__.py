from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'app2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sorted_number = models.IntegerField()

    def get_number_from_first_app(self):
        return self.in_round(1).participant.vars.get('chosen_number', None)


def grouping_players(subsession):
    players = subsession.get_players()
    # 根据第一个app中选择的数字排序
    sorted_players = sorted(players, key=lambda x: x.get_number_from_first_app())
    # 分成每组3人
    group_size = 3
    group_matrix = []

    # 创建小组
    for i in range(0, len(sorted_players), group_size):
        group_matrix.append(sorted_players[i:i + group_size])

    # 设置小组
    subsession.set_group_matrix(group_matrix)

    # 将排序后的数字赋值给每个玩家的sorted_number属性
    for group in subsession.get_groups():
        for player in group.get_players():
            player.sorted_number = player.get_number_from_first_app()


# PAGES
class MyWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'grouping_players'


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyWaitPage, MyPage, Results]


