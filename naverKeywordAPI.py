# 1. 목적 : 네이버 API를 활용하여 키워드에 대한 검색수를 확인하여 소비자들이 원하는 제품에 대해 확인하고자 함
# 2. 목표 : 네이버 API 연동 후 품목 별 경쟁강도 산출
# 3. 특징 : 품목 리스트를 읽은 후 Pandas, Numpy, NaverAPI를 활용하여 연산
# 4. 대상 : 경쟁강도를 알고 싶은 사람들
# 5. 기대효과 : 빠르고 쉽게 키워드 분석이 가능하여 시간 절약이 되며 분석 결과에 대한 인사이트 도출이 가능함

#--------------------------------------------------------------------------------------------------------

# 환경 : Anaconda Python 3.7
# 식별자 : 스네이크 표기법
# 라이브러리
# urllib
# os
# sys

# 변수
#

# 라이브러리
import os
import sys
import urllib.request
from datetime import datetime

# 변수값 설정
start_date = "2020-11-01" # 시작하고자 하는 날짜
end_date = str(datetime.today().year) +"-" + str(datetime.today().month)+ "-" + str(datetime.today().day) # 오늘 날짜(yyyy-mm-dd)
time_unit = "date" # date, month
group_ko_name = "엘지"
ko_keywords = "엘지"
group_en_name = "lg"
en_keywords = "lg"
device = ""
ages = ""
gender = ""
print(start_date)

client_id = "LYVN7sWKm9FfARzXNb9a"
client_secret = "mE5x2hLibJ"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2020-11-15\"," \
       "\"endDate\":\"2020-12-16\"," \
       "\"timeUnit\":\"date\"," \
       "\"keywordGroups\":[{\"groupName\":\"삼성\",\"keywords\":[\"삼성\",\"korean\"]}," \
       "{\"groupName\":\"samsung\",\"keywords\":[\"samsung\",\"english\"]}]," \
       "\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}".format(start_date, );

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)




"""
client_id = "LYVN7sWKm9FfARzXNb9a"
client_secret = "mE5x2hLibJ"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2020-11-15\"," \
       "\"endDate\":\"2020-12-16\"," \
       "\"timeUnit\":\"date\"," \
       "\"keywordGroups\":[{\"groupName\":\"삼성\",\"keywords\":[\"삼성\",\"korean\"]}," \
       "{\"groupName\":\"samsung\",\"keywords\":[\"samsung\",\"english\"]}]," \
       "\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
"""

# 네이버 API 키워드 조회 모듈
#class key_api :


# 품목 리스트 읽기
#    def read_category(self):
#        return

# 읽은 품목에 대해 API로 데이터 조회
#    def read_data(self):
#        return

# 읽은 데이터를 분석
#    def analyze_data(self):
#        return

