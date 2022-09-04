# 네이버 로그인
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(
    "/Users/jeongju/Desktop/git/python_project/web_scraping/chromedriver")
browser.get("https://www.naver.com/")

# 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# id, password 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

# time.sleep(3)

# id 를 새로 입력
# browser.find_element_by_id("id").send_keys("my_id")
# 이 경우 이전의 데이터가 남아 지워줘야한다.
# browser.find_element_bt_id("id").clear()
# browser.find_element_by_id("id").send_keys("my_id")


# html 정보 출력
print(browser.page_source)  # 지금 페이지의 모든 html 문서를 그대로 출력
browser.close()  # 브라우저 종료


# https://jaeseokim.dev/Python/python-Selenium%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-Naver-login-%ED%9B%84-%EA%B5%AC%EB%8F%85-Feed-%ED%81%AC%EB%A1%A4%EB%A7%81/
# 참고
