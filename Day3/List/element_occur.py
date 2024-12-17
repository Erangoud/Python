user_data=input("enetr the elements with sperated by commas ")
my_list=[str(i)for i in user_data.split(",")]
print(my_list)
count=0

element=input("enter the element to search :")
for i in my_list:
    if i == element:
       count+=1
    
print(f'the total no.of element{element} occured is {count}')
