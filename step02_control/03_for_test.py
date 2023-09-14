# 1~10 까지의 합, 홀수의 합, 짝수의 합 구하기
total = 0
even = 0
odd = 0

for i in range(11):
    if i%2 == 0 :
        even = even +i
    else:
        odd = odd + i
    total = total + i

print("합계 : ", total)
print("짝수 : ", even)
print("홀수 : ", odd)

print("범위(range) : " , sum(range(11)))
