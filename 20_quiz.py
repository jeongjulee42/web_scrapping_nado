import requests
from bs4 import BeautifulSoup
url = "https://new.land.naver.com/complexes/25935?ms=37.205186,127.06836,17&a=APT:ABYG:JGC&b=A1&e=RETAIL"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

houses = soup.find_all(
    "div", attrs={"class": "css-1dbjc4n r-13awgt0 r-eqz5dr r-1777fci"})
print(houses)

with open("house.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
