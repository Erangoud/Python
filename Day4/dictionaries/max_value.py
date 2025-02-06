data={'a':10,
      'b':50,
      'c': 30}
max_value=max(data,key=data.get)
print(data[max_value])