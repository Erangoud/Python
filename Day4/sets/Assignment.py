#1.create a set
my_set = {1, 3, 4, 5,2}
print("Set:", my_set)
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2. iterate over sets
for item in thisset:
    print(item)

#3.add members to set
my_set.add(21)
my_set.update([24,56])
print(my_set)

#4.remove items from set
my_set.remove(3)
print(my_set)


#5. remove an item if its present in the set
item_in=4
if item_in in my_set:
    my_set.remove(item_in)

print(my_set)

#6.intersection of sets

set1={1,2,3,4}
set2={5,6,7,3}
intersection=set1 & set2
print(intersection)

#7.union of sets
union=set1 | set2
print(union)

#8.set difference 
difference=set1-set2
print(difference)

#9.symmetric difference 
symmetric_difference = set1 ^ set2
print(symmetric_difference)

#10. clear a set 

my_set.clear()
print("Set after clearing:", my_set)


#11. using the frozenset
# You can't add or remove items from a frozenset
my_set1=frozenset([1,2,3,4,5])
print(my_set1)

#12.max and min
print(max(my_set1))
print(min(my_set1))