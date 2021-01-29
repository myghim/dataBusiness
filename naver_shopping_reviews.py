# 1. 목적 : 자바스크립트 등의 동적 변화가 있는 경우를 위해 Selenium을 활용하여 크롤링
# 2. 목표 :
# 3. 특징 :
# 4. 대상 :
# 5. 기대효과 :
# --------------------------------------------------------------------------------------------------------

# 환경 : Anaconda Python 3.7
# 식별자 : 스네이크 표기법
# 라이브러리
# BeautifulSoup : html 파싱
# requests : html 로드
# pandas : 변수 데이터프레임화 및 CSV 쓰기
# time : 크롤링 지연
# random : 크롤링 지연 시 시간 난수 생성

# --------------------------------------------------------------------------------------------------------
# https://coalastudy.com:8181/api/static/user/kl8t0qvzx9t.html

# 변수

# 라이브러리
from selenium import webdriver
import time
from random import randint
import pandas as pd

# webdriver 설정(chrome)
browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe") # 일반 모드

# URL
url = "https://search.shopping.naver.com/catalog/22834543427"
#url = "https://search.shopping.naver.com/catalog/20622820026"

# 크롬 브라우저 내부 대기
browser.implicitly_wait(3)

# 브라우저 사이즈
browser.set_window_size(580, 580)

# URL
browser.get(url)

# 페이지 내용
#print("Page Contents : {}".format(browser.page_source))

# 세션 값 출력
#print("Session ID : {}".format(browser.session_id))

# 타이틀 출력
#print("Title : {}".format(browser.title))

# 현재 URL 출력
#print("URL : {}".format(browser.current_url))

# 현재 쿠키 정보 출력
#print("Cookies : {}".format(browser.get_cookies()))


# 크롤링 결과 저장 리스트
review_text_lst = []

# 파일 쓰기


# 첫 번째 페이지 리뷰 크롤링
try:
        for j in range(1, 21):
                time.sleep(randint(2, 4))
                meta_review = browser.find_element_by_css_selector("#section_review > ul > li:nth-child({}) > div.reviewItems_review__1eF8A > div.reviewItems_review_text__2Bwpa > p".format(j))
                review_text = meta_review.text
                review_text_lst.append(review_text)


except :
        print("첫 번째 페이지 리뷰 크롤링 애러")

# 두 번째 페이지부터 열 번째 페이지 리뷰
try:
        for i in range(2, 11):
            button = browser.find_element_by_css_selector("#section_review > div.pagination_pagination__2M9a4 > a:nth-child({})".format(i))
            button.click()
            time.sleep(randint(1, 3))
            for k in range(1, 21):
                meta_review = browser.find_element_by_css_selector("#section_review > ul > li:nth-child({}) > div.reviewItems_review__1eF8A > div.reviewItems_review_text__2Bwpa > p".format(k))
                review_text = meta_review.text
                review_text_lst.append(review_text)
except:
        print("두 번째 페이지부터 열 번째 페이지 리뷰 크롤링 애러")

# 열 한번째 페이지 리뷰
try:
        button = browser.find_element_by_css_selector("#section_review > div.pagination_pagination__2M9a4 > a.pagination_next__3ycRH")
        button.click()
        for j in range(1, 21):
                time.sleep(randint(2, 4))
                meta_review = browser.find_element_by_css_selector("#section_review > ul > li:nth-child({}) > div.reviewItems_review__1eF8A > div.reviewItems_review_text__2Bwpa > p".format(j))
                review_text = meta_review.text
                review_text_lst.append(review_text)
except: 
        print("열 한번째 페이지 리뷰 크롤링 애러")

# 열 두번째 페이지 리뷰
try:
        button = browser.find_element_by_css_selector("#section_review > div.pagination_pagination__2M9a4 > a.pagination_now__gZWGP")
        button.click()
        time.sleep(randint(1, 3))
        for k in range(1, 21):
                meta_review = browser.find_element_by_css_selector("#section_review > ul > li:nth-child({}) > div.reviewItems_review__1eF8A > div > p".format(k))
                review_text = meta_review.text
                review_text_lst.append(review_text)
except:
        print("열 두번째 페이지 리뷰 크롤링 애러")

# 열 세번째 페이지 리뷰 ~ 이십 번째 리뷰
try:
        for i in range(5, 13):
            button = browser.find_element_by_css_selector("#section_review > div.pagination_pagination__2M9a4 > a:nth-child({})".format(i))
            button.click()
            time.sleep(randint(1, 3))
            for k in range(1, 21):
                meta_review = browser.find_element_by_css_selector("#section_review > ul > li:nth-child({}) > div.reviewItems_review__1eF8A > div.reviewItems_review_text__2Bwpa > p".format(k))
                review_text = meta_review.text
                review_text_lst.append(review_text)
except:
        print("열 세번째부터 이십번째 페이지 리뷰 크롤링 애러")

with open('C:/Users/onycom/Desktop/네이버베스트/배수구클리너.txt', 'w', encoding="utf-8") as f:
    for line in review_text_lst:
        f.write(line)


# 데이터 다운로드
print(pd.DataFrame(review_text_lst))

#pd.DataFrame(review_text_lst).to_csv("C:/Users/onycom/Desktop/네이버베스트/review_text_lst.csv", encoding="euc-kr")