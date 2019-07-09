import os
# window - cp949 (encoding)
# mac/web - utf-8 (encoding)
with open('ssafy_with.txt','r') as f:
    # readlines는 라인을 각각 리스트의 원소로 가지고 온다.
    lines = f.readlines()
# print(lines)
# print(type(lines))

for line in lines:
    # strip 개행문자, 앞뒤 공백 제거
    print(line.strip())

with open('ssafy_with.txt','r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt)
# print(type(txt))