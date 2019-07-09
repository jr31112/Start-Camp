# 0. requests, bs4 패키지를 불러온다.
# pip install requests : 요청을 보내주는 패키지
# pip install bs4 : 문서를 찾기 편하게 바꾸어주는 패키지(파싱)
import requests
from bs4 import BeautifulSoup
# 1. url로 요청(request.get)을 보내고, response에 저장한다.
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
response = requests.get(url).text
# 2. 요청보내기
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response,'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
table = soup.select('body > div > table > tbody')
# print(table)
print(type(table))
print(len(table))
for tr in table:
    print(tr.select_one('td.sale').text)