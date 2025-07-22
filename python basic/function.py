#Проста функція привітання:
def greet(name = "Гість"): 
    print(f"Привіт {name}")

greet("Іван")
greet("Петро")
greet()

#Функція для додавання чисел:

def odd_numberes(a = 0, b = 0):
    print(int(a) + int(b))

odd_numberes(321 + 755)
odd_numberes()

#Функція для перевірки парності:

def is_even(number = 0):
    if int(number) % 2 == 0:
        print(True)
    else:
        print(False)

is_even(21)
is_even(44)

#Функція з параметром за замовчуванням: Я це зробив на самому початку
#Функція для розрахунку площі (з *args - необов'язково, для цікавості):

def calculate_area(*args):
    if len(args) == 1:
        return args[0] * args[0]
    else:
        return args[0] * args[1]

print(calculate_area(22))
print(calculate_area(22, 11))

#Функція для фільтрації списку (завдання як на CodeWars):

def filter_long_words(words, min_length):
    check_array = []
    for word in words:
        if len(word) == min_length:
            check_array.append(word)

    return check_array

print(filter_long_words(["apple", "banana", "cat"], 6))    