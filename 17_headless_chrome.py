# 굳이 브라우저를 띄우지 않고 사용하는것. 크롬이 없는 크롬. 크롬을 띄우지않고 크롬을 쓰는것.
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver

# 추가
options = webdriver.ChromeOptions()
options.headless = True
# 백그라운드에서 도는 브라우저의 크기
options.add_argument("window-size=640x480")


browser = webdriver.Chrome(
    "/Users/jeongju/Desktop/git/python_project/web_scraping/chromedriver", options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies"
browser.get(url)


interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

# 스크린샷 찍기
browser.get_screenshot_as_file("google_movie.png")

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


browser.quit()
