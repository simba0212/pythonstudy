'''
* 파일 처리
파일객체 = open(파일이름, 모드)
-- 모드 : 'r' : 읽기모드
         'w' : 쓰기모드 (파일이 존재하는 경우, 원래 내용이 지워지고 열린다.)
         'a' : 추가모드
'''

# fp = open("test01.txt",'w')
# for i in range(1,5):
#     content = '%d 번째 줄...\n' %i
#     fp.write(content)
# fp.close()

# 모든 정보 읽기
# fp = open("test01.txt",'r')
# # 리스트에 담아서 나오는 메서드 -> readlines()
# datas = fp.readlines()
# print(datas)
# for i in datas:
#     print(i, end='')
# fp.close()

fp = open("test01.txt",'a')
for i in range(5,8):
    data = '%d 번째 줄...\n' %i
    fp.write(data)
fp.close()

fp = open("test01.txt",'r')
data = fp.read()
print(data)

print('='*30)

with open('text02.txt','w')as f:
    f.write('with 문을 이용해서 파일 쓰기 테스트')

