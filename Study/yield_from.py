'''
def number_generator():
    x = [1,2,3]
    yield from x
    
for i in number_generator():
    print(i)
'''

from tkinter import N


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3)

for i in three_generator():
    print(i)
    