'''
class Person:
    def __init__(self, name, age, address, wallet):
        self.hello  = 'hi'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def greeting(self):
        pass
        print('{0} 저는 {1} 입니다.' .format(self.hello, self.name))
        
    def pay(self, amount):
        if( self.__wallet-amount < 0 ):
            print('돈 부족! 잔액 : {0}' .format(self.__wallet))
            print('{0} 부족해요' .format(amount-self.__wallet))
        else:
            self.__wallet -= amount
            print('이제 {0} 남았네요.' .format(self.__wallet))
        

maria = Person('maria', 28, 'seoul', 10000)
maria.greeting()
maria.pay(2000)
'''

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()