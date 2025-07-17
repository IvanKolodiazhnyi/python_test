import random

print("Task 1")
fruits = ["яблуко", "банан", "апельсин"]
print(fruits[1])

print("Task 2")
i = 5
while i > 0:
    print(i)
    i = i - 1

print("Task 3")
vegetables = ["помідор", "огірок", "капуста"]
if "морква" in vegetables:
    print("Морква є")
else:
    print("Моркви нема")

print("Task 4")

print(random.randint(1, 10))

print("Task 5")

if random.randint(1, 2) == 1:
    print("Орел")
else: 
    print("Решка")

print("Task 6")

s = "Python is fun!"

print(s.upper())

print("Task 7")

greetings = "Hello, world!"
check = "Hello"

print(greetings[:len(check)] == check)

print("Task 8")

numbers = [3, 7, 2, 9, 4]
max = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    else:
        continue

print(max)



