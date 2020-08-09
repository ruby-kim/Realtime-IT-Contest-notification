import requests
from bs4 import BeautifulSoup
import os


class Thinkgood:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.base_url = 'https://www.thinkcontest.com/Contest'
        self.categories = ['/CateField.html?page=1&c=11', '/CateField.html?page=1&c=12']
        self.select = 'div#wrapper > div#trunk > div#main > div.container > div.body.contest-cate > div.all-contest > table.type-2.mg-t-5.contest-table > tbody > tr > td.txt-left > div.contest-title > a'
        self.contests = dict()

    def crawling(self):
        print("===== [Thinkgood] Start  Crawling data... =====")
        for category in self.categories:
            req = requests.get(self.base_url + category)
            soup = BeautifulSoup(req.content, "html.parser")
            data_list = soup.select(self.select)
            self.scraping(data_list)
        print("===== [Thinkgood] Finish Crawling data... =====\n")

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
            req = requests.get('https://www.thinkcontest.com' + data.get('href'))
            soup = BeautifulSoup(req.content, "html.parser")
            tmp = soup.find(class_='body contest-detail')
            val_tmp = tmp.select('div.contest-overview > table.type-5 > tbody > tr > td')
            title = tmp.find(class_='title').get_text()
            values = [val_tmp[-3].get_text(), tmp.find(class_='divided').get_text().replace("\n", ","), tmp.find(class_="linker").get_text(), tmp.find(class_="linker").get('href')]
            self.contests[title] = values

    def check_result(self):
        for key, value in self.contests.items():
            print(key, ":", value)
        print()

    def check_dirname(self):
        print(self.BASE_DIR)
        print()
