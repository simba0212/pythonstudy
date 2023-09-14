from urllib.parse import urlencode
import requests
from urllib.request import urlopen, Request
import pandas as pd
import xml.etree.ElementTree as ET

# url = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
# params ={'serviceKey' : '0DBrKl7WuhdZaII03xAXg+FQPoceGkJoa0IZeuXxXwUkmQb04VtOZEbBY5PmdhogxE+5hNlCStJ4UNsT1bBUag==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
# response = requests.get(url, params=params)
# print(response.content)

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerInfo'
params ='?'+ urlencode({'serviceKey' : '0DBrKl7WuhdZaII03xAXg+FQPoceGkJoa0IZeuXxXwUkmQb04VtOZEbBY5PmdhogxE+5hNlCStJ4UNsT1bBUag==', 'pageNo' : '1', 'numOfRows' : '10', 'zcode' : '11' })
request = Request(url+params)
response_body = urlopen(request).read()
# print(response_body)

root = ET.fromstring(response_body)

df = pd.DataFrame()
for item in root.iter('item'):
    # 딕셔너리
    item_dict={}
    item_dict['충전소명'] = (item.find('statNm').text)
    item_dict['주소'] = (item.find('addr').text)
    item_dict['위도'] = (item.find('lat').text)
    item_dict['경도'] = (item.find('lng').text)
    item_dict['충전기상태'] = (item.find('stat').text)
    df = df._append(item_dict, ignore_index=True)


print(df)
