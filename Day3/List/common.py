
# 9. Write a Python function that takes two lists and returns True if they have at
# least one common member.

list1=[1,2,3,4,5]
list2=[2,3,6,7,8]
list3=[]
for i in list1:
    for j in list2:
        if i==j :
            list3.append(j)
    
print(list3)

# or

common=any(item in list1 for item in list2)
print(common)

