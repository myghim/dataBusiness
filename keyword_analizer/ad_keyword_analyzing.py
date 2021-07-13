# 라이브러리
import pandas as pd
import numpy as np

# csv 파일 위치
loc = ".csv"

# 함수 load_data : 플랫폼 별 파일 로드
def load_data(path):

    data = pd.read_csv(path, encoding="cp949")

    return data

# 함수 analyzed : 플랫폼 별 데이터 분석

# 노출수, 유입수, 구매건수, 광고비용, 매출, 마진(매출 20% 기준), 상세페이지 순위

# 노출수 X 유입수
# 노출수 X 구매건수
# 노출수 X 광고비용
# 노출수 X 매출
# 노출수 X 마진
# 노출수 X 상세페이지 순위

# 유입수 X 구매건수
# 유입수 X 광고비용
# 유입수 X 매출
# 유입수 X 마진
# 유입수 X 상세페이지 순위

# 구매건수 X 광고비용
# 구매건수 X 매출
# 구매건수 X 마진
# 구매건수 X 상세페이지 순위

# 광고비용 X 매출
# 광고비용 X 마진
# 광고비용 X 상세페이지 순위

# 매출 X 마진
# 매출 X 상세페이지 순위

# 마진 X 상세페이지 순위


# G마켓, 옥션 기준
# case 1 : business : 과거 1주일 간 구매전환이 일어난 것 -> CPC 단가를 높여 페이지의 순위를 높임, data : 구매전환의 값이 0보다 크면 키워드 조회
# 기간 : 1주일, 기준 : 구매전환 Y/N

# case 2 : business : , data :
# case 3 : business : , data :
# case 4 : business : , data :
# case 5 : business : , data :

def analyzed(data):

    return


load_data(loc)