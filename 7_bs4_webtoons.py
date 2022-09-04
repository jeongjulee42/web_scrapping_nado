# 요일별 웹툰 정보 모두 긁어오기
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 전체중 class가 title이고, 태그명이 a인 모든 항목 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
# find는 첫 엘리먼트만, find_all은 전부

# 리스트로 반환되므로
for cartoon in cartoons:
    print(cartoon.get_text())
