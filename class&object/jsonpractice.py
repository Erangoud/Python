import json

string = """
{
  "name": "John",
  "age": 30,
  "married": true,
  "divorced": false,
  "children": ["Ann", "Billy"],
  "pets": null,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
"""

data = json.loads(string)
print(data)



with open('text.txt','r') as e:
    print(e.name)