from enum import IntEnum

from models.points import RankingPoint


class PlayerRanking:
    def __init__(self):
        self.single = Ranking(RankingType.SINGLE)
        self.double = Ranking(RankingType.DOUBLE)
        self.mix = Ranking(RankingType.MIX)

    def add_ranking(self, ranking_type, points: RankingPoint):
        if ranking_type == RankingType.SINGLE:
            self.single.points.append(points)

        if ranking_type == RankingType.DOUBLE:
            self.double.points.append(points)

        if ranking_type == RankingType.MIX:
            self.mix.points.append(points)


class Ranking:
    def __init__(self, ranking_type):
        self.ranking_type = ranking_type
        self.points = []


class RankingType(IntEnum):
    SINGLE = 0
    DOUBLE = 1
    MIX = 2
