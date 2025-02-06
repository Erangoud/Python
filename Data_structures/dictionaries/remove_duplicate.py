data = {'a': 1, 'b': 2, 'c': 2, 'd': 3,}
data1={}
for  key,values in data.items():
    # print(key,values)
    if values in data1.values():
        continue
    else:
        data1[key]=values

print(data1)