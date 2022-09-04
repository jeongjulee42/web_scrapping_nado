# 쿠팡 노트북 -> 1에서 2로 바뀌면 주소가 복잡해짐
# but 주소중 page=2 에서 숫자만 바뀌면 페이지가 변함

# http method
# 우리가 http 서버에 요청을 보내면 그 요청에 맞는 응답을 준다.
# 이때 요청에 포함되는것중 http method가 있다
# get 방식 - 어떤 내용을 누구나 볼수있도록 url에 넣어서 보내는것.
# https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1
# 물음표 뒤에있는것부터 변수=값 의 형태 -> 우리가 바꾸어 쉽게 요청할 수 있다.
# get은 한번 보낼때 보낼수있는 데이터의 양에 한계가 있다.

# post 방식 - url이 아닌 http message body에 숨겨서 보내는 방식
# 페이지는 변해도 url이 그대로이면 post방식, 보낼수있는 데이터의 양에 한계가 없다.

import requests
from bs4 import BeautifulSoup
import re

url = "https://search.shopping.naver.com/search/all?frm=NVSCDIG&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=rel&timestamp=&viewType=list"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all(
    "li", attrs={"class": re.compile("^basicList_item__2XT81")})

print(items[0].find("a", attrs={"class": "basicList_link__1MaTN"}).get_text())

# for item in items:
#     price = item.find("",attrs={})
#     if price:
#       price = price.get_text()
#     else:
#       print("none")
# 와 같은 방법으로 찾기
# 네이버로 다시 시도하기

# 쿠팡 광고제품 제거
# for item in items:
#     ad_badge = item.find("",attrs = {})
#     if ad_badge:
#       continue

#     price = item.find("",attrs={})
#     if price:
#       price = price.get_text()
#     else:
#       print("none")

# 리뷰 100개 이상, 평점 4.5 이상

# apple 같이 특정 회사 제외
# if "Apple" in name:


# 다른 페이지도 추가
