"""
class 클래스이름:
    def 메서드(self):
        코드
"""

class Person:
    def greeting(self):
        print('Hello')

    def hello(self):
        self.greeting()

class Person2:
    pass  #빈 클래스

james = Person()
james.greeting()
james.hello()
print(isinstance(james, Person))