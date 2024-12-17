# Write a Python program to find the length of a list without using the len() function.

user_data=input("enetr the data with commas")
my_list=[str(i)for i in user_data.split(",")]

count=0
for i in my_list:
    count+=1

print("the length of list is ",count)