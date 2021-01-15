# 1. 목적 : 네이버 베스트 100 대분류 카테고리별 아이템 품목 리스트화로 상품 트렌드를 파악
# 2. 목표 : 네이버 베스트 100 대분류 카테고리 10개의 아이템 품목 리스트 CSV 파일 만들기
# 3. 특징 : 크롤링을 통해 품목을 읽고 CSV 파일에 작성
# 4. 대상 : 네이버 쇼핑에서 판매되는 상품의 트렌드를 알고 싶은 사람들
# 5. 기대효과 : 빠르고 쉽게 아이템 트렌드를 확인 가능함
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

# 변수
# category : 대분류 카테고리명
# item : 상품명
# lst_item : 상품 리스트
# lst_length : 상품 리스트 길이 계산을 위한 리스트
# rank_data : 순위와 상품 매칭 데이터프레임
# price : 가격
# lst_price : 가격 리스트
# reviews_num : 리뷰수
# lst_reviews_num : 리뷰수 리스트

# --------------------------------------------------------------------------------------------------------

# 라이브러리
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random

# --------------------------------------------------------------------------------------------------------

# 크롤링 html url
# 패션의류 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000
# 패션잡화 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000001
# 화장품/미용 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000002
# 디지털/가전 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000003
# 가구/인테리어 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000004
# 출산/육아 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000005
# 식품 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000006
# 스포츠/레저 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000007
# 생활/건강 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000008
# 여가/생활편의 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000009
# 면세품 : https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000010

# ---------------------------------------------------------------------------------------------------------

# 대분류 카테고리 읽기
for i in range(0, 10):
    url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'lxml')
    metadata = soup.select('div.category_lst > div.summary_area > div > a.on')
    category = metadata[0].text
    lst_item = []
    lst_price = []
    lst_reviews_num = []
    # 50000001 ~ 50000010 : 패션의류, 패션잡화, 화장품/미용, 디지털/가전, 가구/인테리어, 출산/육아, 식품, 스포츠/레저, 생활/건강, 여가/생활편의
    # 50000001 ~ 50000010 html 상품 리스트화
    if i < 10:
        for j in range(1, 101):
            time.sleep(random.randint(1, 3))
            url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'html.parser')
            metadata_item = soup.select('#productListArea > ul > li:nth-child({}) > p > a'.format(j))
            metadata_price = soup.select('#productListArea > ul > li:nth-child({}) > div.price > strong > span.num'.format(j))
            try:
                metadata_reviews_num = soup.select('#productListArea > ul > li:nth-child({}) > div.info > span > a.txt > em'.format(j))
            except :
                pass
            # productListArea > ul > li:nth-child(1) > div.info > span > a.txt > em
            item = metadata_item[0].text
            price = metadata_price[0].text
            price = price.replace(",","")

            # ----------------다시하기 파싱이 안된 부분 reviews 문제를 해결해야 함
            try :
                reviews_num = metadata_reviews_num[0].text
            except :
                reviews_num = ""

            reviews = reviews_num.replace(",", "")
            reviews_num = reviews_num.replace("(", "")
            reviews_num = reviews_num.replace(")", "")

            # 판매처 애러 고쳐야 함
            item_href = metadata_item[0].get('href')
            print("item href")
            print(item_href)
            item_url = item_href
            item_html = requests.get(item_url)
            item_soup = BeautifulSoup(item_html.content, 'html.parser')
            print("item soup")
            print(item_soup)
            metadata_url_item = item_soup.select('#snb > ul > li.floatingTab_on__299Bi > a > em')

            print("matadata url item")
            print(metadata_url_item)
            supply_cnt = metadata_url_item[0].text
            print("supply cnt")
            print(supply_cnt)
            # snb > ul > li.floatingTab_on__299Bi > a > em


            lst_item.append(item)
            lst_price.append(price)
            lst_reviews_num.append(reviews_num)


    # 50000011 : 면세품
    # 50000011 html 상품 리스트화
    else:
        for j in range(1, 40):
            time.sleep(random.randint(1, 3))
            url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000 + i)
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'html.parser')
            metadata_item = soup.select('#productListArea > ul > li:nth-child({}) > p > a'.format(j))
            metadata_price = soup.select('#productListArea > ul > li:nth-child({}) > div.price > strong > span.num'.format(j))
            metadata_reviews_num = soup.select('#productListArea > ul > li:nth-child({}) > div.info > span > a.txt > em'.format(j))

            item = metadata_item[0].text
            price = metadata_price[0].text
            try :
                reviews_num = metadata_reviews_num[0].text
            except :
                reviews_num = ""

            reviews_num = reviews_num.replace(",", "")
            reviews_num = reviews_num.replace("(", "")
            reviews_num = reviews_num.replace(")", "")

            lst_item.append(item)
            lst_price.append(price)
            lst_reviews_num.append(reviews_num)

    # 상품 리스트 길이 계산 리스트
    lst_length = []
    for a in range(1,len(lst_item)+1):
        lst_length.append(a)

    # 순위, 상품명, 상품가격 데이터프레임화
    rank_data = pd.DataFrame({"순위": lst_length, "아이템명": lst_item, "가격" : lst_price, "리뷰수" : lst_reviews_num})
    print(rank_data)
    # 기존 카테고리명에 포함된 '/' 제거
    if "/" in category:
        category = category.replace("/","")
    else:
        pass

    # 순위, 상품명 데이터 프레임 CSV 쓰기
    rank_data.to_csv("C:/Users/onycom/Desktop/네이버베스트/네이버 베스트 100 {}.csv".format(category), encoding="cp949")
