'''
1. 클래스 속성 사용하기
clase 클래스이름:
    속성 = 값

class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff)

mj = Person()
jm = Person()

mj.put_bag('book')
jm.put_bag('pen')

print(jm.bag)
print(mj.bag)
print(jm.bag)
print(mj.bag)

print(Person.bag)
print(mj.__dict__)
print(Person.__dict__)
'''


'''
2. 인스턴스 속성 사용하기
class 클래스이름:
    def __init__(self):
        self.속성 = 값

class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)
    
mj = Person()
jm = Person()

mj.put_bag('note')
jm.put_bag('cup')

print(mj.bag)
print(jm.bag)
'''


'''
3. 비공개 클래스 속성 사용하기
class 클래스이름:
    __속성 = 값
'''
class Knight:
    __item_limit = 10

    def print_item_limit(self):
        '''비공개 속성 출력 메서드입니다.'''
        print(Knight.__item_limit)

mj = Knight()
#print(mj.__item_limit)
print(mj.print_item_limit.__doc__)
mj.print_item_limit()