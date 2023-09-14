class Calc:
    def __init__(self,first,second):
        self.first=first
        self.second=second

    def add(self):
        result = self.first + self.second
        return  result

# 상속(Calc 클래스는 부모클래스가 된다.)
class MoreCalc(Calc):
    # 아무것도 하지 않으려면
    pass

# 자식은 부모의 것을 마음대로 사용할 수 있다.
a = MoreCalc(4,2)
print(a.add())
