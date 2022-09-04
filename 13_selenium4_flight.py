# 네이버 항공권 예매

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# python3 로 터미널에서 실행

browser = webdriver.Chrome(
    "/Users/jeongju/Desktop/git/python_project/web_scraping/chromedriver")
browser.get("https://flight.naver.com/")

# 가는날, 오는날
# from selenium.webdriver.common.by import By  -  xpath를 위해
begin_date = browser.find_element(By.XPATH, "//button[text() = '가는 날']")
# browser.find_element_by_link_text("가는날 선택").click 같이 할수도있음
# // -> html 문서 전체중에서 찾겠다는 뜻
# //button[text()= '가는 날'   -> 버튼 element인데 그것의 텍스트 값이 가는 날 인것을 찾음

# 가져온것을 클릭
begin_date.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//b[text() = "27"]')))
# 날짜 선택 5-27일
day27 = browser.find_elements(By.XPATH, "//b[text() = '27']")
# print(len(day27))
# 5,6,7,... 의 27일도 가져왔음
day27[0].click()


time.sleep(1)
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//b[text() = "도착"]')))
# 도착 버튼 클릭
arrival = browser.find_element(By.XPATH, '//b[text() = "도착"]')
arrival.click()

WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//button[text() = "국내"]')))
domestic = browser.find_element(By.XPATH, '//button[text() = "국내"]')
domestic.click()

# time.sleep(2)
# 제주 국제공항 클릭
# 일부 글자를 포함하는 경우로 계산
WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//i[contains(text(), "제주국제공항")]')))
jeju = browser.find_element(By.XPATH, '//i[contains(text(), "제주국제공항")]')
jeju.click()

# 항공권 검색
# time.sleep(2)
WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//span[contains(text(), "항공권 검색")]')))
search = browser.find_element(By.XPATH, '//span[contains(text(), "항공권 검색")]')
search.click()


# 이후 로딩이 되는데, 로딩이 완료되기 전까지는 데이터를 가져올수없다.
# 기다리기 위해 wait import - from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# 어떤 element가 나올때까지 기다리는데, 그 조건을 무엇으로 할지 결정하는것

elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
# 최대 30초까지 기다리는데 , 어떤 엘리먼트가 표시 될때까지 기다려달라는것.
# 클래스값 비교는 @를 사용
elem.click()

time.sleep(2)
browser.close()


def wait_until(xpath_str):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(
        (By.XPATH, xpath_str)))

# 같이 만들어 편하게 사용
