# flask 설치해야 됨
# https://flask-docs-kr.readthedocs.io/ko/latest/quickstart.html 공식문서
import random
from urllib.parse import urlencode

import requests
from flask import Flask
from requests import Request

# server01. 에서 내용을 접목 시키자.
url1 = 'http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline'
response1 = requests.get(url1)

url2 = 'http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList'
params2 ={'serviceKey' : '0DBrKl7WuhdZaII03xAXg+FQPoceGkJoa0IZeuXxXwUkmQb04VtOZEbBY5PmdhogxE+5hNlCStJ4UNsT1bBUag==', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'JSON', 'dataCd' : 'ASOS', 'dateCd' : 'DAY', 'startDt' : '20100101', 'endDt' : '20100601', 'stnIds' : '108' }
response2 = requests.get(url2, params=params2)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2> random : '+str(random.random())+'</h2>'

@app.route('/create')
def create():
    return '<h2> Create </h2>'

@app.route('/read/<id>')
def read(id):
    return '<h2> Read %s </h2>' %id


# 디버깅 모드
app.run(debug=True)