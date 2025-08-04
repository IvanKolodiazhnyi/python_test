class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} гавкає!"
    
    def get_human_age(self):
        return self.age * 7
