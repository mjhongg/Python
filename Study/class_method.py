'''
class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드
'''

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0} 명 생성되었습니다.' .format(cls.count))

    @classmethod
    def create(cls):
        p = cls()
        return p

mj = Person()
Person.print_count()
jm = Person()
Person.print_count()
hmj = Person.create()
Person.print_count()