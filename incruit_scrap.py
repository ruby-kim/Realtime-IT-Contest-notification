import requests
from bs4 import BeautifulSoup

base_url = "http://gongmo.incruit.com/list/gongmolist.asp"



page=[ 0, "?sortfield=4&sortorder=0&page=1"]

def scrap(page):
    # 페이스 url을 기준으로 page단위로 파싱한다.
    web = requests.get(base_url + page[1])
    soup = BeautifulSoup(web.content, "html.parser")

    # 공모전 리스트 바
    wrap_page = soup.find_all(attrs={"class":"listWrap"})
    print(wrap_page)

    # 다음페이지 파싱
    page_list = soup.find(attrs={"class":"listWrap", "class":"paginate pgMedium"}).find_all("a")

    # 비교해서 페이지 갱신해주기
    for pg in page_list:
        temp = pg.attrs["href"]
        if page[1] < temp:
            page[1] = temp
            break

    # page[0]은 현재페이지, page[1]은 다음페이지다. 같으면 멈춘다.
    return page[0] != page[1]

def is_next(page):
    if page[0] != page[1]:
        page[0] = page[1]
        return True
    return False


def run_app():
    # fasle가 아닐대까지 돌아보자.
    while is_next(page) != False :
            print("====================================" + page[1] + "====================================")
            scrap(page)

run_app()











