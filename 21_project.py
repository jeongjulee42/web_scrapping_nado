import requests
from bs4 import BeautifulSoup


def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=0&acr=3&acq=%EB%82%A0%EC%94%A8&qdt=0&ie=utf8&query=%EB%82%A0%EC%94%A8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        "Accept-Language": "ko-KR,ko"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    print("[오늘의 날씨]")
    weather = soup.find("div", attrs={"class": "temperature_info"})
    print(weather.find("p", attrs={"class": "summary"}).get_text())
    rainfall = soup.find("li", attrs={"class": "week_item today"})
    print(soup.find("div", attrs={"class": "temperature_text"}).find(
        "strong").get_text(), end=" ")

    temps = rainfall.find_all("span", attrs={"class": "weather_left"})
    print("(최고 "+rainfall.find("span", attrs={"class": "highest"}).get_text(
    ).strip()+" / " + "최저 " + rainfall.find("span", attrs={"class": "lowest"}).get_text().strip()+")")

    print("강수확률 : ", end="")
    for temp in temps:
        print(temp.get_text().strip(), end=" ")
    print()
    dusts = soup.find(attrs={"class": "today_chart_list"}).find_all(
        attrs={"class": "item_today level2"})

    for dust in dusts:
        print(dust.get_text().strip(), end=" ")

    print()


if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 정보 가져오기
