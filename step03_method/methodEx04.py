# 최대값 구하기
# 입력 : 숫자가 n개 들어있는 리스트
# 출력 : 리스트 중 가장 최대값 출력하기

def find_max(a):
    n = len(a)      # 입력 크기
    max_v = a[0]    # 리스트의 첫번째 값을 최대값으로 초기화
    min_v = a[0]
    for i in range(1,n):    # 1~n-1까지 반복
        if a[i] > max_v:
            max_v = a[i]
        if a[i] < min_v:
            min_v = a[i]
    return [max_v,min_v]

v = [85,981,18,65,897,651,898,9681,6851,8,49,84]
print(find_max(v))