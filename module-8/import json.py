import json

with open ('Student.json') as input_file:
    data = json.load(input_file)

print(type(data))