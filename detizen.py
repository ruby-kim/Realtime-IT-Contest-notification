import requests
from bs4 import BeautifulSoup
import os


class Detizen:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.req = requests.get('http://www.detizen.com/contest/?Category=19')
        self.html = self.req.content
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.data = self.soup.select(
            '#Body > #Wrapper > #Contents > #Main > section > div > ul > li > div > h4 > a'
        )
        self.titles = dict()

    def crawling(self):
        print("===== [Detizen] Start  Crawling data... =====")
        for i in range(0, len(self.data), 2):
            self.titles[self.data[i].get_text()] = 'http://www.detizen.com/contest/' + self.data[i].get('href')
        print("===== [Detizen] Finish Crawling data... =====\n")

    def check_result(self):
        for key, value in self.titles.items():
            print(key, value)
