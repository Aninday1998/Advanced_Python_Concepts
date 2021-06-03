# we use this to create an java script compatible object
import json

data = '{"d1": "Harry", "d2": 56}'
print(data)

parsed = json.loads(data)       # parsed the dictionary(converted into python object)
print(parsed["d2"])             # we can't say print(data['d1'])
