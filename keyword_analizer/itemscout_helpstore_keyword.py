# 라이브러리
import pandas as pd

# 경로 지정
# 상품 키워드 업로드 저장경로
item_keyword = str(list(pd.read_csv("C:/Users/onycom/Documents/카카오톡 받은 파일/Product_20210222.csv", encoding = "cp949").iloc[0]))

# scout 키워드 업로드
scout_keyword = pd.read_csv("C:/Users/onycom/Documents/카카오톡 받은 파일/itemscout_io.csv", encoding = "cp949").to_numpy()

# store 키워드 업로드
store_keyword = pd.read_csv("C:/Users/onycom/Documents/카카오톡 받은 파일/helpstore.csv", encoding = "cp949").to_numpy()

split_item_keyword = item_keyword.split(" ")

# 전처리
lst_keyword = []
for i in range(len(split_item_keyword)):
    text = split_item_keyword[i].replace("'", "")
    text = text.replace("[","")
    text = text.replace("]","")
    lst_keyword.append(text)

# item scout 조회 결과
print("------item scout 키워드 포함되는 경우-----")
for i in range(len(lst_keyword)):
    for j in range(len(scout_keyword)):
        if lst_keyword[i] == scout_keyword[j][0]:
            print(lst_keyword[i])

# Help Store 조회 결과
print("------Help Store 키워드 포함되는 경우-----")
for i in range(len(lst_keyword)):
    for j in range(len(store_keyword)):
        if lst_keyword[i] == store_keyword[j][0]:
            print(lst_keyword[i])