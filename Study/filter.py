def f(x):
    return x>5 and x<10

a = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(f,a)))
print(list(filter(lambda x: x>5 and x<10, a)))