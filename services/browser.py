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
    
    def get_player(self, tournament, player_id):
        return self.get_content('sport/player.aspx?id={}&player={}'.format(tournament, player_id))

    def get_player_ranking(self, player_id):
        return self.get_content('player-profile/{}/ranking'.format(player_id))

    def get_clubs(self, tournament):
        return self.get_content('sport/clubs.aspx?id={}'.format(tournament))

    def get_tournaments(self, year, q):
        url = 'league?StartDate={0}-01-01&EndDate={0}-01-01&StatusFilterID=false&CountryCode=BEL&Q={1}'.format(year, q)
        return self.get_content_search(url)

    def get_players(self, competition):
        return self.get_content('sport/clubplayers.aspx?id={}&cid={}'.format(competition.comp_id, competition.club_id))

    def get_matches(self, competition):
        return self.get_content('sport/clubplayers.aspx?id={}&cid={}'.format(competition.comp_id, competition.club_id))

    def get_content(self, url):
        parsed_url = self.get_url(url)
        # self.browser.implicitly_wait(3)
        self.browser.implicitly_wait(20)
        self.browser.get(parsed_url)
        self.browser.set_window_size(1920, 1080)
        self.browser.save_screenshot('get_content.png')

        soup = BeautifulSoup(self.browser.page_source, "html5lib")
        main_content = soup.find('div', attrs={'class': 'content'})

        # New layout is using class
        if main_content is None:
            main_content = soup.find('div', attrs={'class': 'page-content'})

        return main_content

    def get_content_search(self, url):
        parsed_url = self.get_url('/find/{}'.format(url))
        self.browser.implicitly_wait(20)
        self.browser.get(parsed_url)
        self.browser.set_window_size(1920, 1080)
        self.browser.save_screenshot('get_content_search.png')
        soup = BeautifulSoup(self.browser.page_source, "html5lib")
        main_content = soup.find('div', attrs={'class': 'wrapper wrapper--padding'})
        return main_content

    @staticmethod
    def get_url(route):
        return 'https://www.toernooi.nl/{}'.format(route)
