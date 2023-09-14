import pandas as pd
import pandasEx02 as ex02

div = ex02.city / 1000000
print(div)
print('-' * 50)

# 시리즈 인덱싱 0부터
print(ex02.city[1])
print(ex02.city['대전'])
print('-'*30)

# 배열 인덱싱을 사용할 경우 (순서, 변경 가능)
print(ex02.city[[1,3,0]])
print('-'*30)

# 슬라이싱
print(ex02.city[1:3])
print('-' * 30)

a = pd.Series(range(3), index=['가','1','A']) # 0~2까지 값 할당하기
print(a)
print('-' * 30)
print(a['A'])
print(a.A)
print(a['1'])
print(a.가)
print(a[1])
