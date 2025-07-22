user_profile = {
    "name": "Ivan",
    "age": 27,
    "city": "Byrshtun",
    "is_active": True
}

print(user_profile["age"], user_profile["city"])
user_profile["age"] = 28
user_profile["email"] = "some_email@gmail.com"
user_profile.pop("is_active")
print(user_profile)

for key in user_profile.keys():
    print(key)

for value in user_profile.values():
    print(value)

for key, value in user_profile.items():
    print(f"key:{key}, value: {value}")

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5]

new_set = set(numbers_with_duplicates)
print(new_set)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set_sum = set1.union(set2)
print(set_sum)

set_intersection = set1.intersection(set2)

print(set_intersection)