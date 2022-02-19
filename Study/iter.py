'''
print(dir([1,2,3]))

it = [1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
'''


'''
it = range(3).__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())
'''


class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


'''
for i in Counter(3):
    print(i)
'''

a, b, c = Counter(3)
print(a, b, c)
