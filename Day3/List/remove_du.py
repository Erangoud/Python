# 6. Write a Python program to remove duplicates from a list.

sample_list=[1,2,3,2,34,1,2]
unique_list=list(set(sample_list))
print(unique_list)

#7. Write a Python program to clone or copy a list.

my_list = [1, 2, 3, 4]
copied_list = my_list[:] 
print("Original list:", my_list)
print("Copied list:", copied_list)


#8. Write a Python program to find the list of words that are longer than n from a
# given list of words.

list_of=["apple","banana","orange","kwi"]
n=3
longer_wrd=[word for word in list_of if len(word)>n]
print(longer_wrd)

