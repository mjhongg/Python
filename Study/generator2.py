'''
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
    

for i in number_generator(3):
    print(i)
'''

def upper_generator(x):
    for i in x:
        yield i.upper()

fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']

for i in upper_generator(fruits):
    print(i)