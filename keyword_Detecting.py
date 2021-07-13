# 1. 목적 : 시장조사 시 크롤링을 통해 쉽게 경쟁력을 분석하기 위함
# 2. 목표 : 엑셀에 입력된 키워드를 활용하여 상위 품목의 내용을 확인하고자함
# 3. 특징 : 키워드 결과에 대해 쉽게 확인이 가능하며 경쟁력이 강한 혹은 약한 키워드 상위 50개를 각각 도출 가능함
# 4. 대상 : 키워드에 대한 결과를 쉽게 알고 싶은 사람들
# 5. 기대효과 : 빠르고 쉽게 키워드 분석이 가능하여 시간 절약이 되며 분석 결과에 대한 인사이트 도출이 가능함

# 라이브러리
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

#keyword
keyword = input("입력하세요 :")
url = "https://search.shopping.naver.com/search/all?query={}&cat_id=&frm=NVSHATC".format(keyword)
html = requests.get(url)
print(html)
soup = BeautifulSoup(html.text, 'lxml')
for i in range(1,46):
    print(i)
    time.sleep(random.randint(1, 3))
    metadata_item = soup.select('#__next > div > div.style_container__1YjHN > div.style_inner__18zZX > div.style_content_wrap__1PzEo > div.style_content__2T20F > ul > div > div:nth-child({}) > li > div > div.basicList_info_area__17Xyo > div.basicList_title__3P9Q7 > a'.format(i))
    item = metadata_item[0].text
    print(item)
