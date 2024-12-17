#Write a Python program to create a list of integers from user input and print the list.
user_data=input("enter the list items seperated by commas : ")
my_list=user_data.split(",")
#my_list=[int(i) for i in user_data(",")]
print(my_list)
for i in my_list:
    print(i)

x=len(my_list)

for i in range(x):
    print(my_list[i])