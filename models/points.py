class RankingPoint:
    def __init__(self, competition_points, tournament_points, date):
        self.competition_points = competition_points
        self.tournament_points = tournament_points
        self.date = date

    def total_points(self):
        return self.competition_points + self.tournament_points
