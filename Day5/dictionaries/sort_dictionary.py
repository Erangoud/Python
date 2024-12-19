data={'a': 3, 'b': 1, 'c': 2}
output=dict(sorted(data.items(), key=lambda item:item[1]))
print(output)

#------- one more method 

sorted_data={}


while data:
    smallest_key=None
    smallest_value=None
    for key,value in data.items():
        if smallest_value is None or value<smallest_value:
            smallest_value=value
            smallest_key=key

    sorted_data[smallest_key]=smallest_value
    del data[smallest_key]
print(sorted_data)
