my_tuple = ('apple', 'banana', 'apple', 'cherry', 'banana', 'banana')

count_dict = {}

for item in my_tuple:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)
