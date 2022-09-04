

import requests
from bs4 import BeautifulSoup
import re

# url 변경
for i in range(1, 6):
    url = "https://search.shopping.naver.com/search/all?frm=NVSCDIG&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex={}&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=rel&timestamp=&viewType=list".format(
        i)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all(
        "li", attrs={"class": re.compile("^basicList_item__2XT81")})

    print(items[0].find("a", attrs={
          "class": "basicList_link__1MaTN"}).get_text())
# 링크도 추가
