# Arithmetic Operators
print("Addition: ", 5 + 3)        # Output: 8
print("Subtraction: ", 5 - 3)     # Output: 2
print("Multiplication: ", 5 * 3)   # Output: 15
print("Division: ", 5 / 3)        # Output: 1.6666666666666667
print("Modulus: ", 5 % 3)         # Output: 2
print("Exponentiation: ", 5 ** 3)  # Output: 125

# Assignment Operators
x = 5
x += 3
print("After += 3, x =", x)   # Output: 8
x -= 2
print("After -= 2, x =", x)   # Output: 6
x *= 4
print("After *= 4, x =", x)   # Output: 24
x /= 2
print("After /= 2, x =", x)   # Output: 12.0
x //= 2
print("After //= 2, x =", x)  # Output: 6.0
x %= 3
print("After %= 3, x =", x)   # Output: 0.0
x **= 2
print("After **= 2, x =", x)  # Output: 0.0

# Operators Precedence
result = 5 + 3 * 2
print("Result: ", result)  # Output: 11
result = (5 + 3) * 2
print("Result: ", result)  # Output: 16
result = 5 + 3 ** 2
print("Result: ", result)  # Output: 14
result = (5 + 3) ** 2
print("Result: ", result)  # Output: 64
result = 5 + 3 * 2 ** 2
print("Result: ", result)  # Output: 17
result = (5 + 3) * 2 ** 2
print("Result: ", result)  # Output: 32
result = 5 + 3 * 2 ** 2 / 4
print("Result: ", result)  # Output: 8.0
result = (5 + 3) * 2 ** 2 / 4
print("Result: ", result)  # Output: 8.0
result = 5 + 3 * 2 ** 2 / 4 - 1
print("Result: ", result)  # Output: 7.0
result = (5 + 3) * 2 ** 2 / 4 - 1
print("Result: ", result)  # Output: 7.0

# Comparison Operators
print("Equal: ", 5 == 3)        # Output: False
print("Not Equal: ", 5 != 3)     # Output: True
print("Greater Than: ", 5 > 3)   # Output: True
print("Less Than: ", 5 < 3)      # Output: False
print("Greater Than or Equal: ", 5 >= 3)  # Output: True
print("Less Than or Equal: ", 5 <= 3)   # Output: False

# Logical Operators
print("Logical AND: ", True and False)  # Output: False
print("Logical OR: ", True or False)   # Output: True
print("Logical NOT: ", not True)       # Output: False

print("Logical AND with variables: ", (5 > 7) and (2 < 4))  # Output: False
print("Logical OR with variables: ", (5 > 3) or (2 > 4))   # Output: True
print("Logical NOT with variables: ", not (5 < 7))         # Output: False

# Conditional Operators
age = 20
if age > 18:
    print("Is adult")
elif age < 18:
    print("Is not adult")
else:
    print("Age is exactly 18")

marks = 55
if marks >= 80:
    print("Grade: A")
elif marks >= 60 and marks < 80:
    print("Grade: B")
else:
    print("Grade: C")

