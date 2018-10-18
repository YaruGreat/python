import random
import math


def shot():
    return random.uniform(0, 1), random.uniform(0, math.pi / 2)


def check(x, a):
    if x < 0.5:
        return x - 0.5 * math.cos(a) <= 0
    elif x > 0.5:
        return x + 0.5 * math.cos(a) >= 1
    else:
        return a == math.pi

try:
    n = int(input())
except:
    print('Something went wrong')
    exit(1)
success = 0
if n < 1:
    print('Uncorrect input')
    exit(2)
for i in range(n):
    x, a = shot()
    success += int(check(x, a))
counted_p = 2 / (success / n)
print(counted_p)
