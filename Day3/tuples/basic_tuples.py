my_tuple=('a','b','c')
print(my_tuple)


#creating tuple with one variable 
tuple1=(1)
tuple2=(1,)
print(type(tuple1)) #int
print(type(tuple2)) #tup

# allows int,str,bool,...

#  tuple constructor

thistuple=tuple(("apple","banana"))
print(thistuple)
print(thistuple[0])
print(thistuple[-1])
print(thistuple[0:2])
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# As the we tuple is unchangeable so convert to list and update the list and convert to tuple again
x=(1,2,3,4,5)
y=list(x)
y[1]=22
x=tuple(y)
print(x)


fruits=("apple","banana")
fruits_T=list(fruits)
fruits_T.append("orange")
fruits=tuple(fruits_T)
print(fruits)

