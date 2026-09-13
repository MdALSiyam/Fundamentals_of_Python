'''
Practice Exercise 4:

1. Print all odd numbers from 1 to 20.
2. Print the table of 57.
3. Print all multiples of 3 from 1 to 50 but skip 15.
4. Take two integers a and b as input. 
   Find and print the first number between 1 and 1000 that is divisible by both numbers.
'''

# 1. Print all odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i)

# 2. Print the table of 57
for i in range(1, 11):
    print(f"57 x {i} = {57 * i}")

# 3. Print all multiples of 3 from 1 to 50 but skip 15
for i in range(3, 51, 3):
    if i == 15:
        continue
    print(i)

# 4. First number between 1 and 1000 divisible by both a and b
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

found = False
for num in range(1, 1001):
    if num % a == 0 and num % b == 0:
        print(f"The first number divisible by both {a} and {b} is: {num}")
        found = True
        break

if not found:
    print(f"No number between 1 and 1000 is divisible by both {a} and {b}.")