import math

def circle_area(radius):
    return math.pi * (radius ** 2)

def rectangle_perimeter(length, width):
    return 2 * (length + width)

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Неможливо ділити на нуль.")
        return None
    except TypeError:
        print("Ведене значення повине бути числом")
        return None
    else:
        print(f"Ділення пройшло успішно {result}")
        return result

def ValueErrorFun():
    while True:
        try:
            number = int(input("Ведіть число "))
        except ValueError:
            print("Будь ласка, введіть дійсне число!")
        else:
            print(f'Ви ввели число: {number}')
            return number

def process_file(filename):
    try:
        file = open(filename)
    except FileNotFoundError:
        print("Файл не знайдено.")
    else:
        print(f"Вміст файлу: {file}")
    finally:
        print("Спроба обробки файлу завершена.")

def checkName():
    print(__name__)