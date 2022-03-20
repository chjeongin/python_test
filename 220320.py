# F12 --> 인터넷 사이트 인터페이스의 코드 확인
# 클라이언트가 서버에 요청 -->URL
# 서버가 클라이언트에 응답 --> httl
#  https://docs.python-requests.org/en/master/user/quickstart/
#  https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# 터미널을 깔끔하게 할 때, cls

#2  요청시 해더 정보를 크롬으로 지정
# 네이버의 경우 알 수 없는 정보들을 다 쳐내기 때문에 기기정보를 작성해주는 것
request_headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98Safari/537.36'), }


# 1 requests 모듈 ==> 웹피이지를 요청하고 응답데이터를 받을 수 있음.
import requests as req

# 파이썬에게 태그의 이미를 알려줘야 하는데 div, a 등 다량의 태그를 알려줄 수 없으므로 그 태그를 알려주는 모듈을 사용해서 html을 해석 --> BeautifulSoup 
from bs4 import BeautifulSoup 

# 1-1. requests 모듈 get
response = req.get("https://news.naver.com/", headers=request_headers) # 특정 사이트에 페이지 요청, 응답데이터 변환
print(response)
# 1-2. <Response [200]> --> 정상 출력된 화면, 만약 출력되지 않을 경우 기기정보를 작성해야함.(출력 전에 정보 입력해야함)



# 요청이 완료되면 html을 읽어와야 함.
# print(response.text) # 너무 길다

# BeautifulSoup _Quick Start
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

print(html_doc)

# 파싱 단계 --> soup을 이용하여 html_doc 문자열을 html 파싱(문자열을 쪼개서 구조화하는 것)
soup = BeautifulSoup(html_doc, 'html.parser')
# 그 내용을 soup 변수로 대입

# 공식문서에서 css selectors 찾기
list1 = soup.select("a") # 선택자를 이용해 태그를 선택, 리스트로 반환

# print(list1) # a태그는모두 출력
# 결과
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>] <-- 리스트 형식, a 태그 3개 가져옴

# a 태그 중 선택해서 출력할 때, 리스트함수에서 선택했던 방법을 이용하여 추출.
print(list1[1])

# 1. 텍스트를 이용하여 원하는 것을 추출
print(list1[1].text)
# 결과 Lacie

# 2. 속성값을 가져오기 <태그명="속성값" 
# a href= --> 속성값
print(list1[1]["href"])
# 결과 http://example.com/lacie

