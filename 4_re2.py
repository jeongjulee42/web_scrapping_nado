# p.search
import re


p = re.compile("ca.e")


def print_match(m):
    if m:
        print("m.group():", m.group())
        # group: 일치하는 문자열 반환
        print("m.string:", m.string)
        # string: 입력받은 문자열 반환
        print("m.start():", m.start())
        # start: 일치하는 문자열의 시작 인덱스 반환
        print("m.end():", m.end())
        # end: 일치하는 문자열의 끝 인덱스 반환
        print("m.span():", m.span())
        # span: 일치하는 문자열의 시작과 끝 인덱스 반환
    else:
        print("매칭 x")


m = p.search("good care")
# search :  주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

m = p.search("careless")
print_match(m)

lst = p.findall("careless")
# findall : 일치하는 모든 것을 리스트 형태로 반환, 문장 내에서 일치하는것이 여러개이면 여러개를 리스트형태로 전부 반환
print(lst)

lst = p.findall("good care & careless & cafe")
print(lst)

# 정규식 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

# 원하는 형태 : 정규식
# . (ca.e)->하나의 문자를 의미
# ^ (^de)->문자열의 시작을 의미
# $ (se$)-> 문자열의 끝을 의미
# w3school -> learn python ->refex 에서 찾아서 공부
# python re -> docs를 찾아 공부
