import os

from bs4 import BeautifulSoup
from selenium import webdriver


class Browser:
    def __init__(self):
        chrome_driver = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'chromedriver', 'chromedriver.exe'))
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
        self.browser.get('https://www.toernooi.nl')
        self.browser.add_cookie({'name': 'st', 'value': 'l=1043&exp=43612.6845210069&c=1&s=2'})

    def get_club(self, tournament, club_id):
        return self.get_content('sport/club.aspx?id={}&club={}'.format(tournament, club_id))

    def get_player_ranking(self, player_id):
        return self.get_content('player-profile/{}/ranking'.format(player_id))

    def get_clubs(self, tournament):
        return self.get_content('sport/clubs.aspx?id={}'.format(tournament))

    def get_tournaments(self, year, q):
        url = 'league?StartDate={0}-01-01&EndDate={0}-01-01&StatusFilterID=false&CountryCode=BEL&Q={1}'.format(year, q)
        return self.get_content_search(url)

    def get_players(self, tournament, club_id):
        return self.get_content('sport/clubplayers.aspx?id={}&cid={}'.format(tournament, club_id))

    def get_matches(self, tournament, club_id):
        return self.get_content('sport/clubplayers.aspx?id={}&cid={}'.format(tournament, club_id))

    def get_content(self, url):
        parsed_url = self.get_url(url)
        # self.browser.implicitly_wait(3)
        self.browser.get(parsed_url)

        soup = BeautifulSoup(self.browser.page_source, "html5lib")
        main_content = soup.find('div', attrs={'id': 'content'})

        # New layout is using class
        if main_content is None:
            main_content = soup.find('div', attrs={'class': 'page-content'})

        return main_content

    def get_content_search(self, url):
        parsed_url = self.get_url('/find/{}'.format(url))
        self.browser.implicitly_wait(10)
        self.browser.get(parsed_url)
        self.browser.save_screenshot('testing.png')
        soup = BeautifulSoup(self.browser.page_source, "html5lib")
        main_content = soup.find('div', attrs={'class': 'wrapper wrapper--padding'})
        return main_content

    @staticmethod
    def get_url(route):
        return 'https://www.toernooi.nl/{}'.format(route)
