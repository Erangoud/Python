# 1.create a tuple
my_tuple=(1,2,3,4,4)
print(my_tuple)

#2.with diff datat type



mix=(1,0.1,True,"hello",[1,2,3])
print(mix)

#3.unpack
tuple_unpack=(1,"hello",0.1)
a,b,c=tuple_unpack
print( a,b,c)

#4. clone
original_tuple = (1, 2, 3, 4)
cloned_tuple = tuple(original_tuple)
print("Original Tuple:", original_tuple)
print("Cloned Tuple:", cloned_tuple)


#5. repeated
repeated_tuple=(1,2,3,4,1,4,2,6,3,5,2)
repeated_items={item for item in repeated_tuple if repeated_tuple.count(item)>1}
print(repeated_items)


#6. check the element 
tuple_items=(1,2,4,5,6,7)
element=5
if element in tuple_items:
    print('yes its present',+ element)
else:
    print('no element is present',+element)

#7.convert list to tuple
list1=[1,2,3,4,5]
my_tup=tuple(list1)
print(my_tup)
print(type(my_tup))


#8.remove an item form tuple as it is unchangeable
tuple1=(1,2,3,4,5)
remove=1
new_tuple=tuple(item for item in tuple1 if item !=remove)
print(new_tuple)

#9.slice a tuple
sliced_tuple=tuple1[1:4]
print(sliced_tuple)


#10. reverse a tuple
reveresed=tuple1[::-1]
print(reveresed)

