class Person:
    def greeting(self):
        print('안녕.')

class Student(Person):
    def greeting(self):
        super().greeting()
        print('내 이름은 mj 야.')

class Student_smart(Person):
    def study(self):
        print(' 나는 공부중 ')

mj = Student()
mj.greeting()
mm = Student_smart()
mm.greeting()