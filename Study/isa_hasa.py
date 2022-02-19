'''
1. is-a 관계

class Person:
    def greeting(self):
        print('안녕하세요.')
    
class Student(Person):
    def study(self):
        print('공부하기.')

mj = Student()
mj.greeting()
mj.study()
'''

'''
2. has-a 관계
'''
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []
    
    def append_person(self, person):
        self.person_list.append(person)
        #print(self.person_list)

    def print_list(self):
        print(self.person_list)

'''
class Student(Person):
    def study(self):
        print('공부하기.')



mj = PersonList()
mj.append_person(mj)
'''

mj = PersonList()
mj.append_person(mj)
mj.print_list()