user_data=input("enetr the elements with sperated by commas ")
my_list=[int(i)for i in user_data.split(",")]
print(my_list)
if 1 in my_list:
    print(f'the elemenet 1 present in the list')
