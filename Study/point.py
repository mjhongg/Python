'''
클래스를 활용하여 2차원 평면에서 위치를 표현한 뒤 두 점 사이의 거리를 구한다.
'''

import math


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point2D(30, 20)
p2 = Point2D(60, 50)

print('p1: {} {}' .format(p1.x, p1.y))
print('p2: {} {}' .format(p2.x, p2.y))

a = p2.x - p1.x
b = p2.y - p1.y

#c = math.sqrt((a*a) + (b*b))
#c = math.sqrt(math.pow(a,2) + math.pow(b,2))
c = math.sqrt((a**2) + (b**2))
print(c)