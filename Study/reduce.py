def f(x,y):
    return x+y

a = [1,2,3,4,5]
from functools import reduce
print(reduce(f,a))

print(reduce(lambda x,y:x+y, a))