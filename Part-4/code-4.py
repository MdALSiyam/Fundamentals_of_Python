# Range

num = range(5)
print(num)

print(list(range(1, 5)))

r = range(1, 5, 2) # (1 = start, 5 = stop, 2 = step)
print(list(r))


# While Loop

i = 1
while i <= 5:
    print(i)
    i += 1
print("While loop ended.")

i = 1
while i <= 5:
    print(i * "*")
    i += 1
print("Traingle pattern using while loop ended.")


# For Loop

for i in range(1, 6):
    print(i)

for i in range(1, 10):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

for i in range(3, 9, 3):
    print(i, "is divisible by 3")


# Break and Continue

for i in range(1, 50):
    if i == 10:
        break
    print(i)
print("Loop ended.")

for i in range(1, 50):
    if (i == 25):
        continue
    if (i % 3 == 0):
        print(i)
print("Out of Loop.")