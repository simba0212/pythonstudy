from random import *

# 0.0 이상 1.0미만
print(random())

# 1.0 이상 3.0미만
print(uniform(1.0, 3.0))

# 1이상 10이하
print(randint(1,10))

# step
print(randrange(1,10,3))

# [] 안에 존재하는 값중 한개 랜덤선택
print(choice([1,54,9,32,75,11]))

