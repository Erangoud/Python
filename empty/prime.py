# def prime_no(n):
#     count=0
#     while 2<=n:
#         for i in range(1,n//2+1):
#             if n%i==0:
#                 count+=1
#         if count>1:
#             print(f'{n} is not a prime')
#             break      
#         else:
#             print(f'{n} is a prime ')
#             break
           

            
# prime_no(7)

# user_data=input("enter the string")
# reveres_string=user_data[::-1]
# print(reveres_string)

#string and it should give each letter as key, and value as frequency of that letter 

user_data=input("enter the letter : ")
empty_dict={}
for char in user_data :
    if char in empty_dict:
        empty_dict[char]+=1
    else:
        empty_dict[char]=1

print(empty_dict)

#A=2,B=2   create a new dictnory 
# example empty_dict1= { 'a':2,'b':2,'c':1 }
# output  empty_dict2={ 2:['a','b'], 1:['c']}
# create a function for it to pass the dictionary 

def dict_list(n):
    output={}
    for key, value in n.items():
        if value not in output:  
            output[value]=[]
        output[value].append(key)
    return output

        
        

print(dict_list(empty_dict))