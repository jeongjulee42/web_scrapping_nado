# 웹에서는 사용자들의 정보를 알수 있다.
# pc, 스마트폰에따라 다른 화면을 볼 수 있다.
# 브라우저가 웹사이트에 접속할때 주는 헤더 정보에 따라서 사이트가 어떤 정보를줄지 선택할 수 있다.
# 웹크롤링과 스크래핑의 requests 같이 컴퓨터가 무단으로 접속하여 정보를 가져오는것을 웹사이트가 차단할수도있다. (사람이 크롬을 이용하여 접속할때는 보임)
# 유저에이전트로 이것을 해결
# 구글에 user agent string 검색
# https://www.whatsmyua.info/ 여기 접속하면
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36
# 와같이 뜨는데 이것이 접속하는 정보이다.
# 사파리같이 다른 브라우저로 접속하면 유저에이전트가 달라짐 -> 이것으로 웹페이지는 어떤 정보를 보여줄지 판단한다.
# headers = {"User-Agent":"정보"}
# res = requests.get(url, headers = headers)
# 이렇게 하면 이 페이지에 접속을 할 때 내가 정의한 유저 에이전트값을 넘겨주는것.

import requests
url = "http://nadocoding.tistory.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()


with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
