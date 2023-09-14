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

# 나중에 DB 읽어오는 코드로 변경된다.
menu = [
    {'id':1,'title':'HTML','body':'html is ...'},
    {'id':2,'title':'CSS','body':'css is ...'},
    {'id':3,'title':'JS','body':'javascript is ...'}
]


@app.route('/')
def index():
    liTags = ""
    for i in menu:
        # f-string 사용법
        # 1. 문자열 앞에 f를 붙인다.
        # 2. 문자열 중간에 변수나 계산식을 넣을 수 있다. (중괄호 {} 를 이용하면)

        liTags = liTags + f'<li><a href="/read/{i["id"]}" />{i["title"]} </a></li>'

    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>Welcome</h2>
                Hello, Web
            </body>
        </html>
    '''

@app.route('/create')
def create():
    return '<h2> Create </h2>'


# 파라미터는 String이지만, int로 변경해준다.
@app.route('/read/<int:id>')
def read(id):
    liTags = ""
    for i in menu:
        liTags = liTags + f'<li><a href="/read/{i["id"]}" />{i["title"]} </a></li>'

    title = ''
    body = ''
    for i in menu:
        if id == i['id']:
            title = i['title']
            body = i['body']
            break

    return f'''
        <!doctype html>
        <html>
            <body>
                <h1><a href="/">WEB</a></h1>
                <ol>
                    {liTags}
                </ol>
                <h2>{title}</h2>
                {body}
            </body>
        </html>
    '''


# 디버깅 모드
app.run(debug=True)