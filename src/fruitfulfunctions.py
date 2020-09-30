import math


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print(math.sqrt((x2-x1)**2 + (y2-y1)**2))
    return (dx ** 2 + dy ** 2)**(1/2)


print(distance(1, 1, 3, 3))
