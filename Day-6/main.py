# main.py
import lib
print(lib.x)
print(lib.sum_2_number(2, 3))

from lib import x, sum_2_number

print(sum_2_number(2, 3))

import math

print(math.sin(3.141592654/2))