# Sum, Difference, Product and Quotient of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Quotient:", a / b)
else:
    print("Quotient: Cannot divide by zero")

"""Problem:
Take price of 3 products as input (eg - 99.5, 23.75, 16.15)
Print the total Bill amount
Print the average price"""

price1 = float(input("Enter price 1: "))
price2 = float(input("Enter price 2: "))
price3 = float(input("Enter price 3: "))

total_bill = price1 + price2 + price3
average_price = total_bill / 3

print("Total Bill Amount:", total_bill)
print("Average Price:", average_price)

# Problem: Take a superhero name as input & check if it starts with 'S' / 's' or not.
hero_name = input("Enter superhero name: ")

# Method 1: Using lower() and startswith()
if hero_name.lower().startswith('s'):
    print("Yes, it starts with 'S' or 's'")
else:
    print("No, it does not start with 'S' or 's'")

# Method 2: Alternative using indexing
if hero_name[0] == 'S' or hero_name[0] == 's':
    print("Yes, it starts with 'S' or 's'")
