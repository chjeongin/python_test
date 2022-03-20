# 자동화 프로그래밍
# pip install Selenium
# 구글 버전에 맞춰서 다운로드 https://sites.google.com/chromium.org/driver/downloads
# from lib2to3.pgen2 import driver
# from webbrowser import Chrome
from selenium import webdriver
import time
Chrome_driver_path = "C:\m\chromedriver"
url = "https://www.naver.com/"
browser = webdriver.chrome(Chrome_driver_path)
# get --> 원하는 것을 실행하기 위한 명령
browser.get(url)
browser.find_element_by_xpath('//*[@id="account"]/a').click()
time.sleep(1)
browser.find_element_by_css_selector('#account > a').click()
time.sleep(1)

id = "000545"
browser.find_element_by_xpath('//*[@id="id"]/a').send_key(id)
time.sleep(1)
pw = ' dfdf '
browser.find_element_by_xpath('//*[@id="pw"]/a').send_key(pw)
time.sleep(1)


# 팝업창 뜰떄 --> 메인창을 인식할 수 있도록 해야함
browser.switch_to.window(browser.window_handles[-1]) # 제일 최신 팝업창으로 이동, 팝업창이 많을 경우[] 안의 숫자를 변경
time.sleep(1)
browser.switch_to.window(browser.window_handles[0]) #원래 창으로 복귀

# id 창 내에 내용이 이미 있는 경우 지우기
browser.find_element_by_xpath('//*[@id="id"]/a').clear() # 글자 지움

# 닫을 떄
browser.close()

# 실행 --> run 삼각형을 클릭
