# from selenium import webdriver
# from bs4 import BeautifulSoup
# from lxml import html
# import pprint
# import re


# chrome_driver = '..\\chromedriver\\chromedriver.exe'
 
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
 
# browser = webdriver.Chrome(executable_path=chrome_driver, chrome_options=chrome_options)
# url = 'https://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html'
# browser.implicitly_wait(3)
# browser.get(url)


# # browser.find_element_by_css_selector('a.btn.btn--secondary.margin-bottom--small')
# soup = BeautifulSoup(browser.page_source, "html5lib")
# main_content = soup.find('div', attrs = {'class': 'entry-content'})
# content = main_content.find('ul').text

# name_pattern = re.compile(r'^([A-Z]{1}.+?)(?:,)', flags = re.M)
# names = name_pattern.findall(content)

# pprint.pprint(names)