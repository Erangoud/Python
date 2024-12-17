list1=[1,2,3,4,5]
list2=[2,3,6,8,9]

diff=list(set(list1)-set(list2))
diff2=list(set(list2)-set(list1))
print(diff)
print(diff2)

# 13. Write a Python program to append a list to the second list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Combined list:", combined)


#15. Write a Python program to find common items from two lists.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_items = list(set(list1) & set(list2))
print("Common items:", common_items)

