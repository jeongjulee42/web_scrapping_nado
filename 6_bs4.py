# bs4 & lxml 설치(구문 분석)
from cgitb import text
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 우리가 가져온 html 문서를 lxml을 통해 bs객체로 만든것. soup가 모든 정보를 가지고 있다. 이것을 통해 element에 접근할수 있다.


# print(soup.title)
# # url의 title정보 가져옴.
# print(soup.title.get_text())
# # title에서 글자만 빼옴

# print(soup.a)
# # 첫번째로 발견된 a 엘리먼트 반환

# print(soup.a.attrs)
# # a태그의 속성 정보 출력

# print(soup.a["href"])
# # href 속성 값 정보 출력

# # 페이지에 대해 잘 모를때
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# # soup 객채내의 a태그에 해당하며, class가 Nbtn_upload인 것에 대해서만 찾는것.

# print(soup.find(attrs={"class": "Nbtn_upload"}))
# # a 태그 없어도 가능

# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)  # 링크정보만 찾기

# soup에서 부모, 자식, 형제 관계 사용하기

# 형제
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)   # 다음 엘리먼트로 넘어가기
# print(rank1.next_sibling.next_sibling)
# 위에서는 아무것도 출력 x, 2번했더니 출력 -> 태그사이에 줄바꿈같은것이 있는것. 따라서 2번하면됨

# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# 부모
# print(rank1.parent)

# 자식은 밑에 있는 테크를 적으면 된다.
# rank1.a.get_text() 같이

# 태그 사이에 줄바꿈때문에 next_sibling 몇번써야할지 모르겠을때
# rank2 = rank1.find_next_sibling("li")  # 조건에 해당하는것만 찾는것
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# rank2 = rank3.find_previous("li")
# print(rank2.a.get_text())


# 랭킹 1~10 까지 한번에 찾아서 처리하기
# rank = rank1.find_next_siblings("li")  # 형제들 전부 가져오기
# print(rank)


# find의 다른 기능
webtoon = soup.find("a", text="정글쥬스-72화")
# 텍스트값 비교, 텍스트가 정글쥬스-72화 에 해당하는것 찾기
print(webtoon)
