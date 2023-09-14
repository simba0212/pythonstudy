num = [10,20,30,40,50]
print(type(num)) # 해당 변수의 type을 나타냄

num2 = (10,20,30,40,50)
print(type(num2)) # 해당 변수의 type을 나타냄

for i in num:
    print(i)

print('*' * 30)

for i in num:
    print(i, end=' ')
print()
print('*' * 30)

# 인덱스값 이용
for i in range(0, num.__len__()):
    print(num[i], end=' ')   # 자동으로 줄바꿈이 아니라 띄어쓰기가 됨
print()

# 거꾸로 찍기
for i in range(num.__len__()-1, -1, -1):
    print(num[i], end=' ')   # 자동으로 줄바꿈이 아니라 띄어쓰기가 됨
print()

