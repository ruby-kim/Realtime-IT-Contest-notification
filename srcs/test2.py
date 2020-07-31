from bs4 import BeautifulSoup
import requests

path = "https://campusmon.jobkorea.co.kr/Contest/List"
contestTitles = []

req = requests.get(path)
objs = BeautifulSoup(req.content, "html.parser").select(".cTb.rank .ti >  a")

for i in objs:
	contestTitles += i.contents

print(contestTitles)
