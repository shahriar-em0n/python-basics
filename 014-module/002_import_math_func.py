# Full import
import math_func
print(math_func.add(3, 5))

# Full import with rename
import math_func as mf
print(mf.square(4))

# Partial import
from math_func import square
print(square(3))