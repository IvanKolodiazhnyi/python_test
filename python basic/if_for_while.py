import random

#Перевірка віку з логічними операторами:

age = int(input("Введіть скільки вам років:"))

has_license = input("Чи володієш ти водійськими правами:")

while has_license != "Так" and has_license != "Ні":
    has_license = input("Введіть Так або Ні:")

if age >= 18 and has_license == "Так":
    print("Ви можете водити автомобіль.")
elif age >= 18 and has_license =="Ні":
    print("Ви можете отримати права")
else:
    print("Ви ще занадто молоді для водіння")


#Генерація пароля (імітація):
random_pasword = ""

while len(random_pasword) != 5:
    new_number = random.randint(0,9)
    random_pasword += str(new_number)
    print(new_number)
    print(random_pasword)

#Гра "Вгадай число":
random_number = random.randint(0,10)

while True:
    user_number = int(input("Вгадай число від 0 до 10:"))
    if user_number > 10:
        continue
    elif user_number > random_number:
        print("Твоє число більше")
    elif user_number < random_number:
        print("Твоє число менше")
    else:
        print("Вітаю!Ви вгадали число!")
        break

#"Відлік" з break та continue:

for number in range(0, 10):
    if number % 2 == 0:
        print(f"Парне число:{number}")
        continue
    elif number == 7:
        print("Досягнуто число 7. Виходимо.")
        break
    else:
        print(number)