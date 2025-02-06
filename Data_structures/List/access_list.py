#Write a Python program to access the first, middle, and last elements of a list.
user_data=input("enter the elements : ")
print(type(user_data))
my_list=[str(i) for i in user_data.split(",")]
middle_element_pos=len(my_list)//2
print(type(my_list))
print("the first element is ",my_list[0])
print("the middle element is ",my_list[middle_element_pos])
print("the last element is ",my_list[-1])


