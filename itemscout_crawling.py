# 라이브러리
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 브라우저가 로딩될 때까지 기다림
from selenium.webdriver.support import expected_conditions as EC # 상태를 확인
from selenium.webdriver.chrome import options

browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe") # 일반 모드

# 크롬 브라우저 내부 대기
browser.implicitly_wait(3)

# 브라우저 사이즈
browser.set_window_size(580, 580)

url = 'https://www.itemscout.io/'
browser.get(url)

# 검색창 input 선택
enter = browser.find_element_by_css_selector("#app > div > nav > div.v-navigation-drawer__content > div > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div")
enter.click()

enter = browser.find_element_by_css_selector("#app > div > main > div > div > div > div.toggle-search-input-container > div > div > div")
enter.click()

