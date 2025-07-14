# python multiplay mane 2 squer

## using by double **


x = 2
y = 3
z = 4

ans = (x + y) * z
print(ans)

ans2 = x + (y * z)
print(ans)

# how can i get float number to convert int number 

print("first int ", int(5.78))

a = 5.50
print(int(50) + a)

# how can i get int number to convert float

print("second float ", float(72.22))

b = 10
print(float(5.50)+b)

# Operator overloading

print("python overloading ---> " "hello" + "shahriar")


print("my number = ", 2 ** 1000)

# python boolen true & false

print(a > 5)

print(3<4)

# math

import math


print(math.floor(5.80))
print(math.floor(3.80))
print(math.floor(- 5.60))


print(math.trunc(4.2))
print(math.trunc(- 4.2))


# random
import random

print(random.random())


print(random.randint(1, 10))

print(random.choice())

names = ['shahriar', 'emon', 'akash', 'hasan']
print(random.choice(names))


print(random.shuffle(names))

# set

setone = {1, 2, 3, 4}

print(setone & {1, 3})

print(setone | {1, 3})

print(setone | {1, 3, 7})

print(setone)

print(setone - {1, 2, 3, 4})

# fractions

from fractions import Fraction

myFra = Fraction(2, 7)
print(myFra)

# Decimal

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1'))