# Function

def sum(a, b):
    return a + b
print(sum(5, 10))

# Function Define
def gst(price): # Parameter
    new_price = price + (price * 0.18)
    return new_price

# Function Call
gst(100) # Argument
print(gst(250))

# In-built Function
print(len("Hello, World!"))
print(max(10, 20, 30, 40, 50))
print(min(10, 20, 30, 40, 50))
# print(sum([10, 20, 30, 40, 50]))
print(sorted([10, 20, 30, 40, 50], reverse=True))
print(abs(-10))
print(round(3.14159, 2))
print(type(10))
print(type(3.14))
print(type("Hello"))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({'a': 1, 'b': 2, 'c': 3}))
print(isinstance(10, int))

# Module Function

import math
print(dir(math))

from math import sqrt, log2
print(sqrt(16))
print(log2(16))

import random
print(random.randint(1, 100))





