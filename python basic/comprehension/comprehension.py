from collections import Counter

numbers = [1, 5, 8, 12, 15, 20, 25]

even_squares = [x**2 for x in numbers.copy() if x % 2 == 0]
print(even_squares) # [64, 144, 400]

words = ["apple", "banana", "cherry", "date"]

word_lengths = {x: len(x) for x in words}

print(word_lengths) # {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}

sentence = "hello world python programming"

unique_chars = sorted({x for x in sentence if x != " "})

print(unique_chars) # {'t', 'm', 'w', 'i', 'o', 'd', 'a', 'r', 'y', 'e', 'g', 'h', 'l', 'p', 'n'}

# Генератор фібоначі

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci_generator = fibonacci_sequence()
fibonacci_list = []

for i in range(10):
    fibonacci_list.append(next(fibonacci_generator))

print(fibonacci_list)

text_words = ["apple", "banana", "apple", "orange", "banana", "apple"]

def words_counter(list):
    count_list = Counter(list)
    
    return count_list.most_common(2)


print(words_counter(text_words)) #[('apple', 3), ('banana', 2)]

products = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Mouse", "price": 25, "category": "Electronics"},
    {"name": "Keyboard", "price": 75, "category": "Electronics"},
    {"name": "Book", "price": 15, "category": "Books"},
    {"name": "Pen", "price": 2, "category": "Stationery"},
]

new_products = [x for x in products if x["category"] == "Electronics" and x["price"] > 50]

print(new_products) # [{'name': 'Laptop', 'price': 1200, 'category': 'Electronics'}, {'name': 'Keyboard', 'price': 75, 'category': 'Electronics'}]

