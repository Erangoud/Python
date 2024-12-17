my_dict={ 
    'name':'eran',
    'age':21,
    'city':'raichur'
    }
# print(my_dict)
# print(my_dict['age'])
# my_dict['number']=99111
# my_dict['job']='automation engineer'
# my_dict['age']=22
# print(my_dict)
# for i in my_dict:
#     if 'age' in my_dict:
#         my_dict['age']=23
#     print(my_dict[i])

x=my_dict.keys()
print(x)
x=my_dict.values()
print(x)
x=my_dict.items()
print(x)

my_dict.update({'age':19})
print(my_dict['age'])

my_dict.pop('age')
print(my_dict)

if 'name' in my_dict.keys():
    print('the key name is present in the dict') 

for key,value in my_dict.items():
    print(key,value)

print(len(my_dict))
my_dict2={
    'age':21
}


# to merge the dictionaries use update or | or unpack dictionary (**)

my_dict3=my_dict2 | my_dict
print(my_dict3)


my_dict={**my_dict,**my_dict2}
print(my_dict3)

my_dict3=my_dict2
my_dict3.update(my_dict)
print(my_dict3)


##