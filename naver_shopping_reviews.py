# 1. 목적 : 상품 리뷰를 통해 제품 구입한 고객의 니즈를 확인함
# 2. 목표 : 네이버 쇼핑 카테고리에 있는 제품 리뷰 400개 크롤링
# 3. 특징 : TEXT 파일로 저장되며 리뷰 한 개마다 띄어쓰기가 이루어짐
# 4. 대상 : 네이버 쇼핑 리뷰
# 5. 기대효과 : 네이버 쇼핑 리뷰 400여 개를 빠르게 스크리닝할 수 있음
# --------------------------------------------------------------------------------------------------------

# 환경 : Anaconda Python 3.7
# 식별자 : 스네이크 표기법
# 라이브러리
# BeautifulSoup : html 파싱
# requests : html 로드
# time : 크롤링 지연
# random : 크롤링 지연 시 시간 난수 생성
# textwrap : 한 줄 단위 텍스트 수 조절

# --------------------------------------------------------------------------------------------------------

# 변수

# 라이브러리
from selenium import webdriver
import time
from random import randint
import textwrap

# webdriver 설정(chrome)
browser = webdriver.Chrome("./chromedriver_win32/chromedriver.exe") # 일반 모드

# 변경할 사항
# URL
# 크롤링할 대상 네이버 쇼핑 카테고리 링크
url = "https://search.shopping.naver.com/catalog/20622820026"

# 유저 컴퓨터에 저장할 경로
local = 'C:/Users/onycom/Desktop/네이버베스트/밀대2.txt'

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

with open('C:/Users/onycom/Desktop/네이버베스트/밀대.txt', 'w', encoding="utf-8") as f:
    for line in review_text_lst:
        f.write(line)


with open(local, 'w', encoding="utf-8") as f:
    for line in review_text_lst:
        #print("line : ", line)
        width_text = textwrap.wrap(line, width=50)
        #print("width_text : ", width_text)
        count = len(width_text)
        for i in range(count):
            #print("width_text[i] : ", width_text[i])
            f.write(width_text[i])
            f.write('\n')
        f.write('\n')