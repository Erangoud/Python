'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''

#some basic practice programs of list and multiple methods 
fruits=['apple','banana','grapes']
print(fruits)

#allows duplicate values bcsv its indexe based (ordered)
automobiles=['ferrari','jaguar','ferrari','jaguar']
print(automobiles)
print(len(automobiles))
print(type(automobiles))

#list constructor :- to create a new list 
makelist=list((1,2,3,4,5,6))
print(makelist)

# access items

print(fruits[1])
print(fruits[-1])
print(automobiles[2:])
print(automobiles[-3:-1])
print(automobiles[3:])

if 'apple' in fruits:
    print("yes apple is present")


#change list items 

number=[1,2,3,4,5,6]
oldvalue=number[-1]
number[-1]=7
print(f'the number is changing from {oldvalue}-->{number[-1]}')
print(number)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert a number 
number.insert(1,22)
print(number)

#append items
number.append('eran')
print(number)

#extend the list 
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)

#using .extend you can add any iterable objects (tuples,sets,dic)
tuple1=(11,22,33)
list1.extend(tuple1)
print(list1)

#Remove an objects 
list1.remove(3)
print(list1)

# pop is used to remove the specified index
list4=[1,2,3,4,5,6]
list4.pop(3)
print(list4)

#if not specified any index in list1.pop() it removes the last item


# del list4[4]
# del list4 # deletes the entier list

#list.clear()

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
   print(thislist[i])

i=0
while i<len(thislist):
   print(thislist[i])
   i+=1

[print(x)for x in thislist]

fruit=['apple','ornge']
newlsit=[]
for i in fruit:
   if "a" in i:
      newlsit.append(i)
print(newlsit)