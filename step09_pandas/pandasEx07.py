import pandas as pd


print('--- 데이터 프레임 생성 ---')
# 1. 하나의 열이 되는 데이터를 리스트나 1차원 배열로 준비
# 2. 이 각각의 열에 대한 이름을 키로 가지고 딕셔너리 만들기
# 3. 이 데이터를 DataFrame 생성자에 넣으면서
# 4. 열 방향 인덱스는 columns 인수를 사용하고
# 5. 행 방향 인덱스는 index 인수를 사용한다.

se = pd.Series(['뽀로로','패티','코롱','루피','에디'])
df = pd.DataFrame(['뽀로로','패티','코롱','루피','에디'])

print(se)
print('-'*50)

print(df)
print('-'*50)

# 테이블에서 열 하나 추출하기
print(df[0])
print('-'*50)

df = pd.DataFrame({'name':['뽀로로','패티','코롱','루피','에디']})
print(df)
print('-'*50)

df = pd.DataFrame({'name':['뽀로로','패티','코롱','루피','에디'],
                   'id':['pororo','paty','cron','ruppy','edi'],
                   'addr':['마포구','노원구','동대문구','중랑구','양평군']
                   },
                  index=["No.1","No.2","No.3","No.4","No.5"])

print(df)
print('-' * 50)

print('--- 데이터 프레임 생성2 ---')
data={"2015": [9904312, 3448737, 2890451, 2466052],
      "2010": [9631482, 3393191, 2632035, 2431774],
      "2005": [9762546, 3512547, 2517680, 2456016],
      "2000": [9853972, 3655437, 2466338, 2473990],
      "지역": ["수도권", "경상권", "수도권", "경상권"],
      "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]}
columns = ['지역','2015','2010','2005','2000','2010-2015 증가율']
index = ['서울','부산','인천','대구']

df = pd.DataFrame(data, index=index, columns=columns)
print(df)
print('-' * 30)

print(df.values)
print('-' * 30)

print(df.columns)
print('-' * 30)

print(df.index)
print('-' * 30)

df.index.name = '도시'
df.columns.name = '년도'
print(df)

print('--- 데이터 프레임 인덱싱 ---')
print(df['지역'])
print('-' * 30)

print(df['2010'])
print('-' * 30)