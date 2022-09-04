# xpath 이용
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/jeongju/Desktop/chromedriver")
# 같은 경로에 있는 경우 Chrome()와 같이 사용 가능

browser.get("https://www.daum.net/")  # 객체를 생성해서 해당 url로 이동

elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")

elem = browser.find_element_by_xpath(
    "//*[@id='daumSearch']/fieldset/div/div/button[2]")
# "" 중복되므로 이거 '로 바꿔줌
elem.click()

# browser.close() # 현재 떠있는 창만 종료
# browser.quit() # 탭이 몇개이던 신경 안쓰고 모두 종료
