import json

sintoma_peso = '''
{
    "Problema a la garganta": 1,
    "Mucosidad": 1,
    "Sangrado": 6,
    "Dolor abdominal": 5,
    "Dolor en el pecho": 6, 
    "Dolor de cabeza": 3,
}
'''

json_data = '''
{
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
'''

# Load the JSON string into a Python dictionary
data = json.loads(sintoma_peso)

# Iterate through the keys
print("Iterating directly over the dictionary:")
for key in data:
    print(key)

print("\nIterating using .keys() method:")
for key in data.keys():
    print(key)