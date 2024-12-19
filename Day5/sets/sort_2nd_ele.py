#sort element based on the second element

tuple_data = ((1, 5), (3, 2), (4, 1), (2, 4))

# Sort by second element of each tuple
sorted_tuple = sorted(tuple_data, key=lambda x: x[1])
print(sorted_tuple)

#(1,5)---->5

