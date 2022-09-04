# 정해진 형태를 의미하는 식 ex> 주민등록번호,이메일주소,차량번호,...

import re

# 4자리중 하나를 모름 ca?e -> 검색하기

p = re.compile("ca.e")
# p는 패턴값을 받기위한 변수
# . (ca.e)->하나의 문자를 의미     care, cafe, case 는 가능 | caffe 이런것은 불가능
# ^ (^de)->문자열의 시작을 의미    de로 시작하는 모든것이 매칭된다.
# $ (se$)-> 문자열의 끝을 의미     case, ... 과 같이 se로 끝나는 모든것이 매칭이된다.

m = p.match("case")
# print(m.group())
# case가 정규식과 매칭이 되어서 출력을 해주는 코드
# m = p.match("caffe")
# print(m.group())
# 매치되지 않으면 에러가 발생

# if m:
#     print(m.group())
# else:
#     print("매칭 x")
# 이렇게 쓴다.


def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭 x")


m = p.match("cave")
print_match(m)
# 함수로 만들어서 사용

m = p.match("good care")
print_match(m)

m = p.match("acare")
print_match(m)

m = p.match("careless")
print_match(m)
# 매치 동작이 주어진 문자열의 처음부터 일치하는지 확인하므로 뒤에 다른 값이 있어도 일치하는것.
# match : 주어진 문자열의 처음부터 일치하는지 확인
