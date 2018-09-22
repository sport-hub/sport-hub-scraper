from models.club import Club
from models.tournament import Tournament
from services.web_processor import WebProcessor
import re


class TournamentProcessor(WebProcessor):
    pass

    def get_tournaments(self, year, query):
        main_content = self.browser.get_tournaments(year, query)
        content = main_content.find('ul', {'id': 'searchResultArea'})
        return self.get_tournaments_html(content)

    def get_clubs(self, tournament: Tournament):
        main_content = self.browser.get_clubs(tournament)
        content = main_content.find('tbody')
        return self.get_clubs_html(content)

    @staticmethod
    def get_clubs_html(column):
        clubs = []
        for link in column.find_all('tr', recursive=False):
            elements = link.find_all("td", recursive=False)

            name = elements[0].text
            number = elements[1].text
            club_id = re.search(r'club=(\d+)', elements[0].a.get('href')).group(1)

            clubs.append(
                Club(club_id, name, number)
            )

        return clubs

    @staticmethod
    def get_tournaments_html(column):
        tournaments = []
        for link in column.find_all('li', recursive=False):
            tournament_id = link.attrs.get('data-anchor')

            if tournament_id:
                name = link.div.div.h4.a.text
                tournaments.append(Tournament(tournament_id, name))

        return tournaments
