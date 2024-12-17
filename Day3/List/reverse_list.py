#Write a Python program to reverse a list without using the reverse() method.
user_data=input("enter the string value : ")
my_list=[str(i)for i in user_data.split(",")]
print(my_list)
# my=user_data.split(",")
# print(my)

rev_list=my_list[::-1]
print(rev_list)


rev=[]
count=-1
for _ in my_list:
    rev.append(my_list[count])
    count=count-1
print(rev)
