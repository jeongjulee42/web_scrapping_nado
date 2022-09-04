# headless 쓸때 주의점
# useragent
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=640x480")
# 밑에 설명
options.add_argument(
    "user-agent=Mozilla/5.0 (MacintoshIntel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36")

browser = webdriver.Chrome(
    "/Users/jeongju/Desktop/git/python_project/web_scraping/chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatsmyua.info/"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/101.0.0.0 Safari/537.36
det_var = browser.find_element_by_id("custom-ua-string")
print(det_var.text)
browser.close()
# headless chrome 일때 따로 유저에이전트를 설정 안해주면 다음과 같이 뜬다.
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
# AppleWebKit/537.36 (KHTML, like Gecko)
# HeadlessChrome/101.0.4951.64 Safari/537.36
# headlesschrome 라고 변해서 뜬다.
# 따라서 다음 문구를 추가
# options.add_argument("user-agent=원래 유저 에이전트값")

# 구글에서 selenium with python 검색
