from bs4 import BeautifulSoup
import requests


class Thinkgood:
    def __init__(self):
        self.titles = dict()
        self.nbrPage = 1
        self.category = 12
        self.contestStatus = 'ing'
        self.rootpath = "https://thinkcontest.com"
        self.pagepath = "/Contest/CateField.html?page={}&c={}&s={}".format(
            self.nbrPage, self.category, self.contestStatus)
        self.req = requests.get(self.rootpath + self.pagepath)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')
        self.catelist = self.soup.find(
            attrs={"class": "cate-list"}).find_all('a')
        self.data = self.soup.find(
            attrs={"class": "contest-table"}).find('tbody').find_all('tr')

    def crawling(self, status='ing'):
        nextPage = self.nbrPage
        gongmoInfo = []
        print("======== Start Crawling ========\n")
        while True:
            self.reget(status, nextPage)
            if not self.data:
                print("======== Done Crawling ========")
                break
            print("======== page {} ========".format(nextPage))
            for i in self.data:
                during = i.find_all('td')[3]
                gongmoInfo = [during.contents[0] + " ~ " + during.contents[-1],
                            self.catelist[self.category - 1].contents[0],
                            i.find_all('td')[1].contents[0],
                            self.rootpath + i.find('a').get('href')]
                self.titles[i.find('a').contents[0]] = gongmoInfo
            nextPage += 1

    def check_result(self):
        for key, value in self.titles.items():
            print("{}\t:\t{}".format(key, value))

    def reget(self, status="ing", curPage=1):
        """ re-requets to site"""
        if self.contestStatus != status:
            self.contestStatus = status
        if self.nbrPage != curPage:
            self.pagepath = "/Contest/CateField.html?page={curpg}&c={c}&s={status}".format(
                            curpg=curPage, c=self.category, status=status)
            self.req = requests.get(self.rootpath + self.pagepath)
            self.soup = BeautifulSoup(self.req.content, 'html.parser')
            self.data = self.soup.find(
                attrs={"class": "contest-table"}).find('tbody').find_all('tr')
