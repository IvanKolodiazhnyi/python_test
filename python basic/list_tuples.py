fruits = ["банан", "яблоку", "груша", "черешня"]

#Вивести перший та останій фрукт зі списку
print(fruits[0], fruits[-1])

#Змінити другий елемент і вивести новий список
fruits[1] = "полуниця"
print(fruits)

#Операції зі списком додати новий фркукт в кінець списку потім видалити його

fruits.append("мандаринка")
print(fruits)
fruits.pop(-1)
print(fruits)

#Створи другий список vegetables з трьома овочами. Об'єднай fruits та vegetables в один новий список groceries. Виведи groceries

vegetables = ["огірок", "помідора", "капуста"]
groceries = fruits + vegetables
print(groceries)

#Використай цикл for, щоб вивести кожен фрукт зі списку fruits на окремому рядку.

for fruit in fruits:
    print(fruit)

#Створи кортеж coordinates з трьома числовими значеннями (наприклад, (10, 20, 30)).

coordinates = (10, 20, 30)

#Спробуй змінити перший елемент цього кортежу (ти отримаєш помилку, і це нормально – поясни чому).

#coordinates[1] = 40 Покаже помилку по причині того що кортежі вони є не мутабильні. Їхні зміні не можна змінювати.

#Виведи другий елемент кортежу.

print(coordinates[1])

#Парні числа

numbers = list(range(1, 11))
even_numbers = []

for number in numbers: 
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)