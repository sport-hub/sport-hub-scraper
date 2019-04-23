from models.club import Club
from models.tournament import Tournament
from models.player import Player
from services.web_processor import WebProcessor
import re


class TournamentProcessor(WebProcessor):
    pass

    def get_tournaments(self, year, query):
        main_content = self.browser.get_tournaments(year, query)
        content = main_content.find('ul', {'id': 'searchResultArea'})
        return self.get_tournaments_html(content)

    def get_clubs(self, tournament: Tournament):
        main_content = self.browser.get_clubs(tournament.tournament_id)
        content = main_content.find('tbody')
        return self.get_clubs_html(content)

    def get_user_id(self, player: Player):
        main_content = self.browser.get_player(player.competitions[0].comp_id, player.competitions[0].player_id)
        return self.get_player_html(main_content)

    @staticmethod
    def get_clubs_html(column):
        clubs = []
        for link in column.find_all('tr', recursive=False):
            elements = link.find_all("td", recursive=False)

            name = elements[0].text
            number = elements[1].text

            club = Club(name, number)

            comp_id = re.search(
                r'aspx\?id=(.+?)((?=\&)|$)', elements[0].a.get('href')).group(1)
            club_comp_id = re.search(
                r'club=(\d+)', elements[0].a.get('href')).group(1)

            club.add_competition(comp_id, club_comp_id)

            clubs.append(club)

        return clubs

    @staticmethod
    def get_tournaments_html(column):
        tournaments = []

        for link in column.find_all('li', recursive=False):
            item = link.find('a')
            if item:
                tournament_id = link.find('a').attrs.get(
                    'href').replace('/sport/tournament.aspx?id=', '')
                name = link.find('h4').a.span.text
                tournaments.append(Tournament(tournament_id, name))

        return tournaments

    @staticmethod
    def get_player_html(content):
        test = content.find(
            'div', {'class': 'playerphoto'}).a.img.attrs.get('src')

        return re.search(r'.*\/(.*)(?=\.jpg)', content.find('div', {'class': 'playerphoto'}).a.img.attrs.get('src')).group(1)
