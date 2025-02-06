'''
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')'''



data=input("enter the comma-seperated number :")
my_list=data.split(",")
my_tuple=tuple(my_list)
print("list:",my_list)
print("list:",type(my_list))
print("Tuple:",my_tuple)

