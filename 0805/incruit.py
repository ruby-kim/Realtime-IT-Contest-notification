import requests
from bs4 import BeautifulSoup
import os


class Incruit:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.base_url = 'http://gongmo.incruit.com/list/gongmolist.asp'
        self.categories = ['?ct=1&category=10', '?ct=1&category=11']
        self.contests = dict()

    def crawling(self):
        print("===== [Incruit]  Start Crawling data... =====")
        for category in self.categories:
            req = requests.get(self.base_url + category)
            soup = BeautifulSoup(req.content, "html.parser")
            data_list = soup.find(id='tbdyGmScrap').find_all('a')
            self.scraping(data_list)
        print("===== [Incruit] Finish Crawling data... =====\n")

    def scraping(self, data_list):
        """
        key: 공모전 이름
        value: [ 기간
                 분류(과학 / 공학, 소프트웨어 항목만)
                 주최자
                 사이트링크 크롤링
               ]
        중복 공모전 체크
        """
        for data in data_list:
            req = requests.get(data.get('href'))
            soup = BeautifulSoup(req.content, "html.parser")
            tmp = soup.find(class_='tBrd1Gray').find_all('td')

            title = soup.find(class_='job_new_top_title').get_text()
            values = [tmp[3].get_text(), tmp[0].get_text().replace("<br/>", ","), tmp[1].get_text(), tmp[4].find('a').get('href')]
            self.contests[title] = values

    def check_result(self):
        for key, value in self.contests.items():
            print(key, value)

    def check_dirname(self):
        print(self.BASE_DIR)
        print()
