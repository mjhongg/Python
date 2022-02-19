class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕.'

class Student(Person):
    '''
    def __init__(self):
        print('Student __init__')
        super().__init__()
        self.school = '공부하기.'
    '''
    pass

mj = Student()
#print(mj.school)
print(mj.hello)