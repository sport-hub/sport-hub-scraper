from models.club import Club
from models.player import Gender, Player
from models.ranking import Ranking
from models.tournament import Tournament
from services.web_processor import WebProcessor
import re


class ClubProcessor(WebProcessor):
    pass

    def get_players(self, tournament: Tournament, club: Club):
        main_content = self.browser.get_players(tournament.tournament_id, club.club_id)
        columns = main_content.table.tbody.tr.find_all("td", recursive=False)
        return self.get_player_from_html(columns)

    def get_matches(self, tournament: Tournament, club: Club):
        main_content = self.browser.get_players(tournament.tournament_id, club.club_id)
        columns = main_content.table.tbody.tr.find_all("td", recursive=False)
        return self.get_player_from_html(columns)

    def get_club(self, tournament: Tournament, club: Club):
        self.browser.get_club(tournament, club)

    def get_player_from_html(self, columns):
        gentlemen = columns[0]
        ladies = columns[1]
        players = []

        players += self.get_player_by_gender_html(gentlemen, Gender.MALE)
        players += self.get_player_by_gender_html(ladies, Gender.FEMALE)

        return players

    @staticmethod
    def get_player_by_gender_html(column, gender: Gender):
        players = []

        if not column.table:
            return players

        for link in column.table.tbody.find_all('tr', recursive=False):
            elements = link.find_all("td", recursive=False)

            player_id = re.search(r'player=(\d)', elements[1].a.get('href')).group(1)
            name = elements[1].text
            # flags = elements[2].text
            number = elements[3].text
            # played = elements[4].text
            single = elements[5].text
            double = elements[6].text
            mix = elements[7].text

            players.append(
                Player(
                    player_id,
                    name,
                    gender,
                    number,
                    Ranking(single, double, mix)
                )
            )

        return players
