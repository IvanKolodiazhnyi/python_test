import json
import os

data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(data, indent=4)

if os.path.exists("data.json"):
    read_j = open("data.json", "r")
    convert_json = json.load(read_j)
    print("convert_json", convert_json)
else:
    with open("data.json", "x") as j:
        j.write(json_string)

