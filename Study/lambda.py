#plus_ten = lambda x : x + 10
#print(plus_ten(1))
#list_ten = list(map(lambda x : x+10, [1,2,3]))
#print(list_ten)

a = [1,2,3,4,5,6,7,8,9,10]
#print_list = list(map(lambda x : str(x) if x%3 == 0 else x, a))
#print(print_list)
#print_list = list(map(lambda x : str(x) if x==1 else float(x) if x==2 else x+10, a))
#print(print_list)


def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x+10

print(list(map(f, a)))
