# 셀레니움 - 웹페이지 테스트 자동화를 할수있는 프레임 워크
# 이것을 통해 직접 웹브라우저를 컨트롤 하면서 html을 가져와 스크래핑한다.
# pip으로 셀레니움과 크롬 드라이버 설치
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/jeongju/Desktop/chromedriver")
# 같은 경로에 있는 경우 Chrome()와 같이 사용 가능

browser.get("http://naver.com")  # 객체를 생성해서 해당 url로 이동

# 엘리먼트 찾아가기 -로그인버튼
# elem = browser.find_element_by_class_name("link_login")
# elem.click()  # click

# browser.back()  # 이전페이지로 이동
# browser.forward()  # 다시 앞으로 이동
# browser.refresh()  # 새로고침
# browser.back()

# 검색창 찾기
elem = browser.find_element_by_id("query")
elem.send_keys("나도코딩")
# Keys.Enter 를 위해
# from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)

# 테그로 정보찾기
elem = browser.find_element_by_tag_name("a")
elem = browser.find_elements_by_tag_name("a")  # 모두 찾기
# print(elem)
for e in elem:
    e.get_attribute("href")
    # print(e.get_attribute("href"))

# elem = browser.find_element_by_name 도 가능
