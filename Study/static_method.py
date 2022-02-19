'''
class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드
'''
class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
    
    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(1,2)
Calc.mul(2,5)