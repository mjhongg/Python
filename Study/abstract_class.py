'''
from abc import *

class 추상클래스이름(metaclass=ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        코드
'''

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('study')

    def go_to_school(self):
        print('go_to_school')
    
mj = Student()
mj.study()
mj.go_to_school()