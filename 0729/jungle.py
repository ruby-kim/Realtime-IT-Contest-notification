import requests
from bs4 import BeautifulSoup
import os


class Jungle:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.req = requests.get('https://www.jungle.co.kr/contest/filter?categoryCode=CTC001')
        self.html = self.req.content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.data = self.soup.select(
            'div > div > ul#contest-list.thumb_list05 > li > div > a.thumb_title05'
        )
        self.titles = dict()

    def crawling(self):
        print("===== [Jungle] Start  Crawling data... =====")
        for text in self.data:
            self.titles[text.get_text()] = 'https://www.jungle.co.kr' + text.get('href')
        print("===== [Jungle] Finish Crawling data... =====\n")

    def check_result(self):
        for key, value in self.titles.items():
            print(key, value)
        print()

    def check_dirname(self):
        print(self.BASE_DIR)
        print()
