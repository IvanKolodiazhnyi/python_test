import re

text = "Контакти: email@example.com, phone: +380991234567, second.email@domain.org"

email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

print(email)
