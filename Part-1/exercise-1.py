"""
Practice Exercise-1:
- Add a person with first name as Tony and last name as Stark
- Tony's age is 53
- Tony's height is 1.85m
- Tony is secretly a superhero. Take his superhero name as input & print it
"""

#Solution

first_name = "Tony"
last_name = "Stark"
age = 53
height = 1.85
is_genius = True

superhero_name = input("Enter Tony's secret superhero name: ")

print("Full Name:", first_name, last_name)
print("Age:", age, "years old")
print("Height:", height, "m")
print("Secret Identity:", first_name, "is secretly", superhero_name)