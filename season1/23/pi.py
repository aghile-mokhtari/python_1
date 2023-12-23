from random import uniform
from math import sqrt

n = 4000
c = 0

for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    l = sqrt((x**2)+(y**2))
    if l < 1:
        c += 1

print(4*c/n)