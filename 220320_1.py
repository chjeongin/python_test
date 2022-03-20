request_headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98Safari/537.36'), }


# 1 requests 모듈 ==> 웹피이지를 요청하고 응답데이터를 받을 수 있음.
import requests as req

# 파이썬에게 태그의 이미를 알려줘야 하는데 div, a 등 다량의 태그를 알려줄 수 없으므로 그 태그를 알려주는 모듈을 사용해서 html을 해석 --> BeautifulSoup 
from bs4 import BeautifulSoup 

# # 1-1. requests 모듈 get
# response = req.get("https://news.naver.com/", headers=request_headers) # 특정 사이트에 페이지 요청, 응답데이터 변환
# print(response)
# # 1-2. <Response [200]> --> 정상 출력된 화면, 만약 출력되지 않을 경우 기기정보를 작성해야함.(출력 전에 정보 입력해야함)

# # print(response.text)


# soup = BeautifulSoup(response.text, 'html.parser')
# alist = soup.select(".cluster_text_headline nclicks(cls_eco.clsart)")
# print(alist)

# alist = soup.select(".cluster_text_headline nclicks(cls_eco.clsart) > a") # a 태그를 찾아가는 것 



response = req.get("https://news.daum.net/foreign#1", headers=request_headers) # 특정 사이트에 페이지 요청, 응답데이터 변환
print(response)
# 1-2. <Response [200]> --> 정상 출력된 화면, 만약 출력되지 않을 경우 기기정보를 작성해야함.(출력 전에 정보 입력해야함)

# print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')
alist = soup.select(".link_txt")
print(alist[1].text)

# 뉴스의 텍스트 가져오기
# 1 싸이트 주소
url = alist[1]["href"]
response2 = req.get(url, headers=request_headers)
print(response2)
title = soup.select(".link_txt")
# ---------------------------------------


