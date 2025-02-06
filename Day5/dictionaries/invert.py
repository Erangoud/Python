# Write a program to invert a dictionary so that keys become values and values become keys.
# {'a': 1, 'b': 2, 'c': 3}
# {1: 'a', 2: 'b', 3: 'c'}

data={'a': 1, 'b': 2, 'c': 3}
inveret_data={}

for key,values in data.items():
    inveret_data[values]=key

print(inveret_data)