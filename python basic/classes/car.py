class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}"

class ElectricCar(Car):
    def __init__(self, model, brand, battery_size):
        super().__init__(model, brand)
        self.battery_size = battery_size
    
    def change(self):
        return f"Автомобіль {self.model} заряджається. Розмір батареї: {self.battery_size} kWh."

    def display_info(self):
        return f"{super().display_info()}, Розмір батареї: {self.battery_size}"
    
