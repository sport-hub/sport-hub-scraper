from datetime import datetime

from models.player import Player
from models.points import RankingPoint
from models.ranking import RankingType
from services.web_processor import WebProcessor


class PlayerProcessor(WebProcessor):
    pass

    def get_player_ranking(self, player: Player):
        main_content = self.browser.get_player_ranking(player.player_id)
        rows = main_content.table.tbody.find_all("tr", recursive=False)
        self.set_player_ranking_from_html(rows, player)

    @staticmethod
    def set_player_ranking_from_html(rows, player):
        for ranking_type in RankingType:
            columns = rows[int(ranking_type)].find_all("td", recursive=False)
            tournament_points = columns[3].div.text
            competition_points = columns[4].div.text

            points = RankingPoint(tournament_points, competition_points, datetime.utcnow())
            player.ranking.add_ranking(ranking_type, points)
