'''
    def 함수명(인자):
        실행문장1
        실행문장2
        [return 리턴값]
'''

def view():     # 함수 정의
    print('hello')
    return

def view2():     # 함수 정의
    print('hello')

def view3():     # 함수 정의
    return 10

def view4():     # 함수 정의
    return 'Hi'
# 메인함수  : 프로그램의 엔트리 포인트

if __name__ == '__main__':
    view()  # 함수 호출
    view2()  # 함수 호출
    print(view3())  # 함수 호출
    str = view4()
    print(str)  # 함수 호출
