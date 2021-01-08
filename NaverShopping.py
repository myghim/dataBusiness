# 쇼핑 인사이트

import urllib.request
import json

client_id = "LYVN7sWKm9FfARzXNb9a"
client_secret = "mE5x2hLibJ"
url = "https://openapi.naver.com/v1/datalab/shopping/categories";

body = {
    "startDate": "2020-01-01",
    "endDate": "2020-12-31",
    "timeUnit": "date",
    "category": [{"name": "수입커트러리", "param": ["50000000"]}],
    "device": "",
    "gender": "", "ages": [ ]
}

body = json.dumps(body, ensure_ascii=False)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    jsondic = json.loads(response_body)
    #print(jsondic)
    for i in range(0,100):
        print(jsondic["results"][0]["data"][i])
        
    #print(jsondic["results"][0]["title"])
    #print(response_body.decode('utf-8'))
else: print("Error Code:" + rescode)

