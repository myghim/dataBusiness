from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import random
# https://velog.io/@hyukstory/python7-%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%87%BC%ED%95%91-%ED%81%AC%EB%A1%A4%EB%A7%81-json-data
#url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000"
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




# 패션의류, 패션잡화, 화장품/미용, 디지털/가전, 가구/인테리어, 출산/육아, 식품, 스포츠/레저, 생활/건강, 여가/생활편의
lst_category = []
"""for i in range(1, 10):
    url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    metadata = soup.select('div.category_lst > div.summary_area > div > a.on')
    category = metadata[0].text
    lst_item = []

    for j in range(1, 101):
        time.sleep(random.randint(1, 3))
        url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        metadata_item = soup.select('#productListArea > ul > li:nth-child({}) > p > a'.format(j))
        item = metadata_item[0].text
        lst_item.append(item)
        print(item)
        #print(j," : ",item)
    lst_length = []
    for a in range(1,len(lst_item)+1):
        lst_length.append(a)
    rank_data = pd.DataFrame({"순위" : lst_length, "아이템명" : lst_item})
    print(rank_data)
    category = category.replace("/","")
    rank_data.to_csv("C:/Users/onycom/Desktop/네이버베스트/네이버 베스트 100 {}.csv".format(category), encoding="cp949")
"""

# 면세품
lst_category = []
for i in range(10, 11):
    url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    metadata = soup.select('div.category_lst > div.summary_area > div > a.on')
    category = metadata[0].text
    lst_item = []

    for j in range(1, 40):
        time.sleep(random.randint(1, 3))
        url = "https://search.shopping.naver.com/best100v2/detail.nhn?catId=" + str(50000000+i)
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        metadata_item = soup.select('#productListArea > ul > li:nth-child({}) > p > a'.format(j))
        item = metadata_item[0].text
        lst_item.append(item)
        print(item)
        #print(j," : ",item)
    lst_length = []
    for a in range(1,len(lst_item)+1):
        lst_length.append(a)
    rank_data = pd.DataFrame({"순위" : lst_length, "아이템명" : lst_item})
    print(rank_data)
    category = category.replace("/","")
    rank_data.to_csv("C:/Users/onycom/Desktop/네이버베스트/네이버 베스트 100 {}.csv".format(category), encoding="cp949")
