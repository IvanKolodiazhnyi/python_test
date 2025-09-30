import os, datetime

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    temperature = input("Введіть температуру:")
    type_temperature = input("Введіть з якого вимірювання буде відбуватися конвертація (С - цельсія, Ф - фаренгейт):")
    if type_temperature == "С":
        print(celsius_to_fahrenheit(int(temperature)))
    else:
        print(fahrenheit_to_celsius(int(temperature)))

def file_info(filepath):
    if os.path.exists(filepath):
        timeStamp = datetime.datetime.fromtimestamp(os.path.getatime(filepath))
        return {"size": os.path.getsize(filepath), "modification_time": str(timeStamp)}
    else:
        return "File doesn't exist"

print(file_info("test_file.txt"))
print(file_info("any_file.txt"))
