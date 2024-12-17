# Write a Python program to find the largest and smallest numbers in a list without using built-in functions.

user_data=input("enter the list emlements")
my_list=user_data.split(",")
print(max(my_list))
print(min(my_list))

small=large=my_list[0]

for i in my_list:
    if small>i:
        small=i
    if large<i:
        large=i

print('the largest no.is ',large)
print('the smallest no.is ',small)