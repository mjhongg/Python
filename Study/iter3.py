
'''
it = iter(range(3))
it2 = next(it)
print(it2)
it2 = next(it)
print(it2)
it2 = next(it)
print(it2)
'''

import random

it = iter(lambda : random.randint(0,5), 2)
it2 = next(it)
print(it2)
it2 = next(it)
print(it2)
it2 = next(it)
print(it2)