import requests
from bs4 import BeautifulSoup
import os
import json


class Thinkgood:
    def __init__(self):
        self.base_url = 'https://www.thinkcontest.com/Contest'
        self.categories = ['/CateField.html?page=1&c=11', '/CateField.html?page=1&c=12']
        self.select = 'div#wrapper > div#trunk > div#main > div.container >' \
                      'div.body.contest-cate > div.all-contest > table.type-2.mg-t-5.contest-table >' \
                      'tbody > tr > td.txt-left > div.contest-title > a '
        self.contests = dict()

    def crawling(self):
        """ 카테고리별 공모전 리스트 크롤링 """
        print("===== [Thinkgood]  Start Crawling data... =====")
        for category in self.categories:
            req = requests.get(self.base_url + category)
            soup = BeautifulSoup(req.content, "html.parser")
            data_list = soup.select(self.select)
            self.scraping(data_list)
        print("===== [Thinkgood] Finish Crawling data... =====")

    def scraping(self, data_list):
        """
        공모전 세부 정보 크롤링 & dict 형태로 데이터 저장
        공모전 이름(title): [기간(term),
                          분류(classify) - 과학/공학, 소프트웨어 항목만,
                          주최자(host),
                          사이트링크(link)]
        """
        for data in data_list:
            req = requests.get('https://www.thinkcontest.com' + data.get('href'))
            soup = BeautifulSoup(req.content, "html.parser")
            tmp = soup.find(class_='body contest-detail')
            val_tmp = tmp.select('div.contest-overview > table.type-5 > tbody > tr')

            title = soup.find(class_='body contest-detail').find(class_='title').get_text()
            values = ['0'] * 4
            for elem in val_tmp:
                elem = str(elem.get_text())
                if "접수기간" in elem:          # term
                    values[0] = elem.replace("접수기간\n", "").replace("\n", "")
                elif "응모분야" in elem:        # classify
                    values[1] = elem.replace("응모분야\n", "").replace("\n", ", ")[6:-6]
                elif "주최" in elem:          # host
                    values[2] = elem.replace("주최\n", "").replace("\n", "")
                elif "주관" in elem:
                    values[2] += ": " + elem.replace("주관", "").replace("\n", "")
                    if values[2][0] == ":":
                        values[2].replace(": ", "")

            values[3] = tmp.find(class_="linker").get('href') if tmp.find(class_="linker") is not None \
                else "(링크 미지원)"   # link
            self.contests[title] = values

    def save_result(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(base_dir, 'thinkgood.json'), 'w+', encoding='utf-8') as json_file:
            json.dump(self.contests, json_file, ensure_ascii=False, indent='\t')
        assert "===== [Thinkgood] Save data... =====\n"

    def check_result(self):
        for key, value in self.contests.items():
            print(key, ":", value)
