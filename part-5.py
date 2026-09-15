# List

marks = [90, 80, 70, 60, 50, 'A', 'B', 'C', 84.5, 75.0]
print(marks, type(marks), len(marks))


# Indexing

print(marks[1])
print(marks[-2])

# Slicing

print(marks[2:5])
print(marks[:3])
print(marks[3:])
print(marks[:])

for score in marks:
    print(score)

print (96 in marks)

marks.append(95)
print(marks)

marks.insert(2, 85)
print(marks)

marks.clear()
print(marks, len(marks))


# Tuple

grades = (90, 80, 70, 60, 50, 'A', 'B', 'C', 84.5, 75.0)
print(grades, type(grades), len(grades))
print(grades[2])
print(grades[-2])
print(grades.index(70))


# Set

scores = {90, 80, 70, 60, 50, 'A', 'B', 'C', 84.5, 75.0}
print(scores, type(scores), len(scores))

for score in scores:
    print(score)


# Dictionary

mark_sheet = {
    'Maths': 90,
    'Science': 80,
    'English': 70,
    'History': 60,
}
print(mark_sheet, type(mark_sheet), len(mark_sheet))

print(mark_sheet['Maths'])
print(mark_sheet.get('Science'))
print(mark_sheet.keys())
print(mark_sheet.values())
print(mark_sheet.items())
print(mark_sheet.get('Geography', 'Not Found'))

for subject, score in mark_sheet.items():
    print(f"{subject}: {score}")

for key in mark_sheet.keys():
    print(key, mark_sheet[key])
