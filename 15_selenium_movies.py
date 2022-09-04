# 동적 페이지(사용자가 동작을 했을때 작동하는것.)에 대한 웹 스크래핑

# 할인중인 영화정보만 빼오기


import requests
from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies?hl=ko&gl=US"
# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class": "ULeU3b neq64b"})
# print(len(movies))
# # 0이라고 뜬다.

# with open("movie.html", "w", encoding="utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())  # html 문서 이쁘게 출력

# 여기서 영화를 검색해도 검색이 안된다.
# 따라서 html 파일을 직접 브라우저에서 열어보자.
# 화면이 다르다. 영어로 뜨고 다른 영화도 뜬다 ->  접속하는 사용자의 header 정보를 통해 구글 무비에서 서로 다른 페이지를 리턴해주므로.

# 이럴때 유저 에이전트를 사용하자.
url = "https://play.google.com/store/movies"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko"}
# "Accept-Language":"ko-KR,ko" : 한글 언어로 된 페이지를 달라고 요청하는것.
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ULeU3b neq64b"})
print(len(movies))


# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# 새로고침하면 10개정도밖에 안뜬다 -> 원래 페이지에서 10개먼저 뜨고 반응형으로 스크롤을 내리거나 하면 더 뜨기 때문 (동적페이지)
# 이럴때 셀레니움이 필요함
# 먼저 영화 제목 찍기

for movie in movies:
    title = movie.find("div", attrs={"class": "Epkrse"})
    if title:
        title = title.get_text()
        print(title)
    else:
        continue
