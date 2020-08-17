import requests
from bs4 import BeautifulSoup
import os
import json

class Thinkgood:
    def __init__(self):
        self.base_url = 'https://www.thinkcontest.com/Contest'
        self.categories = ['/CateField.html?c=11', '/CateField.html?c=12']
        self.categories_state = ['&s=hurry', '&s=ing', '&s=soon']
        self.select = 'div#wrapper > div#trunk > div#main > div.container >' \
                      'div.body.contest-cate > div.all-contest > table.type-2.mg-t-5.contest-table >' \
                      'tbody > tr > td.txt-left > div.contest-title > a '
        self.contests = dict()

    def crawling(self):
        """ 카테고리별 공모전 리스트 크롤링 """
        print("===== [Thinkgood]  Start Crawling data... =====")
        for category in self.categories:
            for state in self.categories_state:
                page = 1
                while 42:
                    req = requests.get(self.base_url + category + state + '&page=' + str(page))
                    soup = BeautifulSoup(req.content, "html.parser")
                    data_list = soup.select(self.select)
                    self.scraping(data_list)
                    if len(data_list) == 0: 
                        break
                    page += 1
        print("===== [Thinkgood] Finish Crawling data... =====")

    def scraping(self, data_list):
        """
        공모전 세부 정보 크롤링 & dict 형태로 데이터 저장
        공모전 이름(title): [기간(host),
                          분류(classify) - 과학/공학, 소프트웨어 항목만,
                          주최자(host),
                          사이트링크(link)]
        """
        for data in data_list:
            req = requests.get('https://www.thinkcontest.com' + data.get('href'))
            soup = BeautifulSoup(req.content, "html.parser")
            tmp = soup.find(class_='body contest-detail')
            val_tmp = tmp.select('div.contest-overview > table.type-5 > tbody > tr > td')
            title = soup.find(class_='body contest-detail').find(class_='title').get_text()
            term = val_tmp[-3].get_text()
            classify = tmp.find(class_='divided').get_text().replace("\n", ", ")[2: -2]
            host = tmp.find(class_="linker").get_text().replace('\ue89e', '')
            link = tmp.find(class_="linker").get('href')
            self.contests[title] = [term, classify, host, link]

    def save(self):
#        base_dir = os.path.dirname(os.path.abspath(__file__))
#        with open(os.path.join(base_dir, 'thinkgood.json'), 'w+', encoding='utf-8') as json_file:
#            json.dump(self.contests, json_file, ensure_ascii=False, indent='\t')
        file_path = './thinkgood.json'
        with open(file_path, 'w', -1, "utf-8") as json_file:
            json.dump(self.contests, json_file, ensure_ascii=False, indent='\t')
        print("===== [Thinkgood] Save data... =====\n")

    def check_result(self):
        for key, value in self.contests.items():
            print(key, ":", value)