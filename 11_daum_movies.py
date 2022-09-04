# 웹에서 이미지 다운받기
from bs4 import BeautifulSoup
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}


for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(
        year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        # http 붙이기
        image_url = image["src"]
        if image_url.startswith("//"):
            # //으로 시작한다면
            image_url = "https:" + image_url

        print(image_url)
        # 접속해서 파일 저장
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie{}_{}.jpg".format(year, idx + 1), "wb") as f:
            # 이미지는 바이너리가 아니므로 wb를 사용
            f.write(image_res.content)  # 이미지가 가지고있는 컨텐트를 라일에 쓴다.

        # 상위 5개의 이미지만 가져오기 위함
        if idx >= 4:
            break
