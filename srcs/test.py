from bs4 import BeautifulSoup
import requests

path = "https://thinkcontest.com"
contestTitles = []

req = requests.get(path)
objs = BeautifulSoup(req.content, "html.parser").select(".contest-title a")

for i in objs:
	contestTitles += i.contents

print(contestTitles)
