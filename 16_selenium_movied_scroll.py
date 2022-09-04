# 동적페이지를 requests가 아닌 셀리니움을 통해 가져오기
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
browser = webdriver.Chrome(
    "/Users/jeongju/Desktop/git/python_project/web_scraping/chromedriver")
browser.maximize_window()
# 최대화

# 페이지 이동
url = "https://play.google.com/store/movies"
browser.get(url)


# 페이지 접속하고나서 스크롤 밑으로 내리기
# 자바스크립트 코드 실행하기
# browser.execute_script("window.scrollTo(0,1080)")  # pc의 해상도 높이, 한페이지 스크롤 다운

# 맨 밑으로 스크롤
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# 현재 문서의 총 높이만큼 스크롤을 내린다.

# 높이가 변하지 않을때까지 내리기
interval = 2  # 2초에 한번씩 스크롤 내리기
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복 수행
while True:
    # 스크롤 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)  # 페이지 로딩 대기

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

# 동적 페이지(사용자가 동작을 했을때 작동하는것.)에 대한 웹 스크래핑

# 할인중인 영화정보만 빼오기

# 복붙


soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class": "ULeU3b neq64b"})
print(len(movies))


for movie in movies:
    title = movie.find("div", attrs={"class": "Epkrse"})
    if title:
        title = title.get_text()
        print(title)
    else:
        continue

# 스크롤 내리면 영화의 테크가 달라진다.
# 여러개 찾기
# attrs={"class": ["ULeU3b neq64b","  " ]} 클래스가 이 리스트안에있는것들과 일치하는것들을 가져온다


# 세일하는 영화 정보 찾기
# 할인 전 가격
# for movie in movies:
#     title = movie.find("div", attrs={"class": "Epkrse"})

#     original_price = movie.find("span",attrs = {"class":"sale"})
#     if original_price:
#         original_price = original_price.get_text()
#     else:
#         continue
# # 할인된 가격
#     price = movie.find("span",attrs = {"class":"sdfasfdfa"})
#     # 링크
#     link = movie.find("a", attrs={})["href"]
#     # 올바른 링크: https://play.google.com + link

#     # 이후 print 문으로 출력

browser.quit()

# 굳이 브라우저를 띄우지 않고 사용하는것. 크롬이 없는 크롬. 크롬을 띄우지않고 크롬을 쓰는것.
