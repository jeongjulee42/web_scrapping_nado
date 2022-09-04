# 웹 스크래핑한것을 csv 형태로 저장하기 (엑셀)
# 네이버 코스피 시가총액 순위 가져오기 1~200

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1, 2):
    res = requests.get(url+str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # 테이블을 가져와서 처리
    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")

    for row in data_rows:
        # td 가져오기
        # columns = row.find_all("td")
        # data = [column.get_text() for column in columns]
        # print(data)
        # 빈줄 , \t, \n 같은거 처리
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue   # 의미없는 데이터 스킵
        data = [column.get_text().strip() for column in columns]
        # strip를 통해 불필요한 공백 제거
        print(data)
