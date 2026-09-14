"""
Practice Exercise 5

Problem 1:
Given a list of roll numbers: [101, 105, 102, 101, 108, 105, 110]. Print all unique roll nums in the list.

Problem 2:
Given Employee records in the form of a list of tuples where each tuple contains:
(Employee ID, Employee Name, Salary)

Example - [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

Ask user to enter Employee ID & search it inside records.
"""

# ==========================================
# Solution for Problem 1
# ==========================================
roll_numbers = [101, 105, 102, 101, 108, 105, 110]
unique_roll_nums = set(roll_numbers)

print("Unique Roll Numbers:", unique_roll_nums)


# ==========================================
# Solution for Problem 2
# ==========================================
employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

search_id = int(input("Enter Employee ID to search: "))

found = False
for emp in employees:
    if emp[0] == search_id:
        print(f"Employee Found -> ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}")
        found = True
        break

if not found:
    print("Employee ID not found.")