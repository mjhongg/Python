'''
class 기반클래스이름1:
    코드

class 기반클래스이름2:
    코드

class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드
'''

class Person:
    def greeting(self):
        print('안녕.')

class University:
    def manage_credit(self):
        print('학점 관리.')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기.')

mj = Undergraduate()
mj.greeting()
mj.manage_credit()
print(Undergraduate.mro())
mj.study()
print(int.mro())
