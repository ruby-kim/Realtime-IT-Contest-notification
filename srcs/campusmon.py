from bs4 import BeautifulSoup
import requests


class Campusmon:
    def __init__(self):
        self.titles = dict()
        self.nbrPage = 1
        self.category = 'A011'
        self.contestStatus = ['state_sch', 'state_ing','state_poi']
        self.rootpath = "https://campusmon.jobkorea.co.kr"
        self.pagepath = "/Contest/List?_Page={}&_Tot_Cnt=814&_Field_Code={}&_Sort_Order=1".format(
            self.nbrPage, self.category)
        self.req = requests.get(self.rootpath + self.pagepath)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')
        self.data = self.soup.find('tbody').find_all('tr')

    def crawling(self, status='state_ing'):
        nextPage = self.nbrPage
        print("======== Start Crawling ========\n")
        while True:
            self.reget(status, nextPage)
            if not self.data:
                print("======== Done Crawling ========\n")
                break
            print("======== page {} ========".format(nextPage))
            for i in self.data:
                tmp = i.find('a')
                tmpstate = i.find_all('span')[-1].get('class')
                if tmpstate[0] not in self.contestStatus:
                    print("======== Done Crawling ========\n")
                    return
                self.titles[tmp.contents[0]] = self.rootpath + tmp.get('href')
            nextPage += 1

    def check_result(self):
        for key, value in self.titles.items():
            print("{}\t:\t{}".format(key, value))

    def reget(self, status="ing", curPage=1):
        """ re-requets to site"""
        if self.nbrPage != curPage:
            self.pagepath = "/Contest/List?_Page={curpg}&_Tot_Cnt=814&_Field_Code={c}&_Sort_Order=1".format(
                curpg=curPage, c=self.category)
            self.req = requests.get(self.rootpath + self.pagepath)
            self.soup = BeautifulSoup(self.req.content, 'html.parser')
            self.data = self.soup.find('tbody').find_all('tr')
