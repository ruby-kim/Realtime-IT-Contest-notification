import requests
from bs4 import BeautifulSoup
import os
import json


class Incruit:
    def __init__(self):
        self.base_url = 'http://gongmo.incruit.com/list/gongmolist.asp'
        self.categories = ['?ct=1&category=10', '?ct=1&category=11']
        self.contests = dict()

    def crawling(self):
        """ 카테고리별 공모전 리스트 크롤링 """
        print("===== [Incruit]  Start Crawling data... =====")
        for category in self.categories:
            page = 1
            while 42:
                req = requests.get(self.base_url + category+"&page="+str(page))
                soup = BeautifulSoup(req.content, "html.parser")
                data_list = soup.find(id='tbdyGmScrap').find_all('a')
                if len(data_list) == 0: 
                    break
                self.scraping(data_list)
                page += 1
        print("===== [Incruit] Finish Crawling data... =====")

    def scraping(self, data_list):
        """
        공모전 세부 정보 크롤링 & dict 형태로 데이터 저장
        공모전 이름(title): [기간(host),
                          분류(classify) - 과학/공학, 소프트웨어 항목만,
                          주최자(host),
                          사이트링크(link)]
        """
        for data in data_list:
            req = requests.get(data.get('href'))
            soup = BeautifulSoup(req.content, "html.parser")
            tmp = soup.find(class_='tBrd1Gray').find_all('td')

            title = soup.find(class_='job_new_top_title').get_text()
            term = tmp[3].get_text()
            classify = tmp[0].get_text().replace("<br/>", ",")
            host = tmp[1].get_text()
            link = tmp[4].find('a').get('href').replace('\t', '')
            self.contests[title] = [term, classify, host, link]

    def save(self):
#         base_dir = os.path.dirname(os.path.abspath(__file__))
#         with open(os.path.join(base_dir, 'incruit.json'), 'w+', encoding='utf-8') as json_file:
#             json.dump(self.contests, json_file, ensure_ascii=False, indent='\t')
        file_path = './incruit.json'
        with open(file_path, 'w', -1, "utf-8") as json_file:
            json.dump(self.contests, json_file, ensure_ascii=False, indent='\t')            
        print("===== [Incruit] Save data... =====\n")

    def check_result(self):
        for key, value in self.contests.items():
            print(key, ":", value)