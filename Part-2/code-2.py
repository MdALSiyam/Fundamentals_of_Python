# Type Casting & Conversion
age = input("Enter your age: ")
new_age = int(age) + 1

print(new_age)
print(float(new_age))

print(1 + 2.5) #Implicit Type Conversion
print(1 + int(2.8)) #Explicit Type Conversion

# String Operations
name = "Abdul Latif"

print(name.upper())
print(name.lower())
print(name.capitalize())

print(name.find("Latif"))
print(name.find("S")) # Returns -1 if not found

print(name.replace("Abdul Latif", "Siyam"))
print(name.replace("Latif", "Siyam"))

print('S' in name) # Returns True if found, else False

# Reserved Keywords
True = "abc" # This will raise a SyntaxError because True is a reserved keyword
False = "def" # This will raise a SyntaxError because False is a reserved keyword
# True, False, int, string, while, for, if, else, elif, break, continue, return, def, class, import, from, as, pass, raise, try, except, finally, with, lambda, yield are some of the reserved keywords in Python.