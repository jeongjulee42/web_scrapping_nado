# 웹에서 원하는 정보를 추출하기 위해 html 문서 정보를 가져오기 위해 사용한다.
# pip으로 requests 설치
import requests
res = requests.get("http://google.com")  # 우리가 원하는 url 정보를 넘겨준다
# url에 접속해서 어떤 정보를 가져오는 명령어.

# 응답 코드 찍기 - 정보를 가져오는 과정에서 문제가 없었는지 확인
print(res.status_code)  # 200이면 정상, 403이면 접근 권한이 없다는것.

# 200 == requests.codes.ok
# if res.status_code == requests.codes.ok:
#     print("정상입니다.")

# else:
#     print("error:", res.status_code)

# 다른 방법
res.raise_for_status()  # 정상적으로 문서를 가져오면 문제가 없고, 그렇지 않은 경우 에러를 발생시킨다. 더욱 간단.

print(res.text)  # html 문서 확인

# 파일로 만들어서 확인
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

# requests를 통해 정보를 정상적으로 받아온다
