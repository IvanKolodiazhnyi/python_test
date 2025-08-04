from car import Car, ElectricCar
from dog import Dog
from count import Counter

car1 = Car("BMW", "M5")
car2 = Car("Mersedens", "C")
print(car1.display_info())
print(car2.display_info())

dog1 = Dog("Alisa", 12)
dog2 = Dog("Barbos", 3)
print(dog1.bark(), dog1.get_human_age())
print(dog2.bark(), dog2.get_human_age())

electricCar1 = ElectricCar("BMW", "I8", "80")
electricCar2 = ElectricCar("HONDA", "Acord", "50")

print(electricCar1.display_info(), electricCar1.change())
print(electricCar2.display_info(), electricCar2.change())

count1 = Counter()
count2 = Counter()

count1.increment()
count1.increment()
count2.increment()
count2.reset()

print(count1.count)
print(count2.count)
