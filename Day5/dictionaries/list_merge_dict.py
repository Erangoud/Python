#Combine Two Lists into a Dictionary
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dict1={}
for i in range(len(keys)):
    dict1[keys[i]]=values[i]

print(dict1)