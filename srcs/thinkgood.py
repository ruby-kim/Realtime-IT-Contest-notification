# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


class Thinkgood:
    """thinkgood site에서 소프트웨어 분야의 현재 신청가능한 공모전 크롤링"""
    def __init__(self):
        '''
        :param
            infos : 실제 공모전 핵심 정보를 갖고 있는 dict(후에 pandas로 변경 가능)
            startPage : 크롤링할 테이블의 시작페이지
            category : 소프트웨어 분야(12)
            contestStatus : 공모 예정, 진행중(12, 마감 임박 포함), 마감 임박, 공모 종료
            rootpath : 고정 URL
            pagepath : 유동 URL 부분
            req : 해당 주소에서 request한 결과물을 저장(object)
            soup : html.parser방식으로 req를 읽음
            catelist : 카테고리 리스트
            data : 크롤링에 필요한 정보들이 있는 table만 필터링한 결과물(object)
        '''
        self.infos = dict()
        self.startPage = 1
        self.category = 12
        self.contestStatus = 'ing'
        self.rootpath = "https://thinkcontest.com"
        self.pagepath = "/Contest/CateField.html?page={}&c={}&s={}".format(
            self.startPage, self.category, self.contestStatus)
        self.req = requests.get(self.rootpath + self.pagepath)
        self.soup = BeautifulSoup(self.req.content, 'html.parser')
        self.catelist = self.soup.find(
            attrs={"class": "cate-list"}).find_all('a')
        self.data = self.soup.find(
            attrs={"class": "contest-table"}).find('tbody').find_all('tr')

    def crawling(self, status='ing'):
        nextPage = self.startPage
        gongmoInfo = []
        print("======== Start Crawling ========\n")
        while True:
            # BS4에서 셀레니움처럼 여러 페이지로 접근하기 위해 다음 페이지를 request함
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
                self.infos[i.find('a').contents[0]] = gongmoInfo
            nextPage += 1

    def check_result(self):
        for key, value in self.infos.items():
            print("{}\t:\t{}".format(key, value))

    def reget(self, status="ing", curPage=1):
        """ re-requets to site"""
        # 시작 페이지와 현재 작업할 페이지 번호가 다르면 re-get 진행
        if self.startPage != curPage:
            self.pagepath = "/Contest/CateField.html?page={curpg}&c={c}&s={status}".format(
                            curpg=curPage, c=self.category, status=status)
            self.req = requests.get(self.rootpath + self.pagepath)
            self.soup = BeautifulSoup(self.req.content, 'html.parser')
            self.data = self.soup.find(
                attrs={"class": "contest-table"}).find('tbody').find_all('tr')
