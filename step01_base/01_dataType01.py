# 주석표현

# 자료형 (DateType) : 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불린

# 1) 숫자형 (정수형(integer), 실수 (부동소수점))
# 정수 : 123
# 실수 : 123.45

num01 = 124  # long형이 따로 없이 모든 정수는 int형으로 담을 수 있다.
print(num01)
num01 = -124  # long형이 따로 없이 모든 정수는 int형으로 담을 수 있다.
print(num01)

num02 = 12.574
print(num02)

# 여러줄 주석 (''',""")
'''
    숫자연산 : 사칙연산(+,-,*,/) 을 계산기와 마찬가지로 사용
    % : 나머지 값을 반환
    // : 소숫점 자리를 버리는 연산자(몫)
'''
su1 = 7
su2 = 3
print(su1 / su2)
print(su1 % su2)
print(su1 // su2)

# 2) 문자열 : 작은따옴표 사용 가능 'Hello Python'
#            큰따옴표 사용 가능 "Hello Python"
# 여러줄 문자열 표현 : ''', """
# 파이썬에서는 char가 없고 다 String이다.
print(
'''안녕하세요~~
Hi~~~
방가방가~~''')
print("*"*15)
print(
'''안녕하세요~~
Hi~~~
방가방가~~''')
# 파이썬에서는 문자열을 더하고 곱할 수 있다.
# [문자열 더하기] 문자열 + 문자열
# [문자열 곱하기] 문자열 * 문자열

msg1 = 'Hello'
msg2 = '홍길동'

print(msg1 + msg2)
print(msg1 * 10)

# 문자열에는 인덱싱과 슬라이싱이 존재한다.
# 인덱싱은 위치에 존재하는 문자를 반환한다.
# 슬라이싱
str = '문자열에는 인덱싱과 슬라이싱이 존재한다.'
print(str[-1])
print(str[-2])
print("+"*20)

print(str[0:])
print(str[4:])
print(str[4:7])

