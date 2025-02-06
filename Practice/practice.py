"""
Reverse a String Without Using Built-in Functions
Write a Python function to reverse a given string without using [::-1] or the reversed() function.
"""

# str1 = "Python function to reverse"
# leng= len(str1)
# reve=""
# for i in range(leng-1,-1,-1):
#     reve+=str1[i]

# print(reve)


"""
Find the Missing Number in a List
Given a list of n-1 integers in the range 1 to n, find the missing number.
Example: [1, 2, 4, 5, 6] → Missing number is 3.
"""

# list1=[1,2,4,5]

# for i in range(1,7):
#     if i not in list1:
#         print(i)
    

"""
Check for Palindrome
Write a function to check if a given string is a palindrome.
Example: "madam" → True, "hello" → False.
"""
# a = "madam"
# b= a[::-1]

# print(b)
# if a == b:
#     print("its a palindrome")

"""
Count Frequency of Elements in a List
Given a list, count the frequency of each element without using Counter from collections.
"""
# from collections import Counter
# a = "frequency"
# x = Counter(a) 
# print(x)

# dict1={}

# for char in a:
#     if char not in dict1:
#         dict1[char] = 1
#     else:
#         dict1[char]+=1
    
# # dict2= sort(dict1.values)
# print(dict1)

"""
Find the First Non-Repeating Character in a String
Write a Python function to find the first non-repeating character in a string.
Example: "swiss" → First non-repeating character is 'w'.
"""
# from collections import Counter
# a = "swiss"
# b ={}

# for char in a:
#     if char not in b:
#         b[char]=1
#     else:
#         b[char]+=1

# for i in b:
#     if b[i]==1:
#         print(i)
#         break

# from collections import Counter
# a= "swiss"
# b=Counter(a)
# for i in b.items():
#     if i[1]==1:
#         print(i)
#         break


"""
Check if Two Strings are Anagrams
Given two strings, check if they are anagrams of each other.
Example: "listen" and "silent" → True
# """
# from collections import Counter
# a="listen"
# b="silent"


# if sorted(a)==sorted(b):
#     print("anagram")
# else:
#     print("not a anagaram")

# if Counter(a)==Counter(b):
#     print("anagram")

"""
Sum of Digits of a Number
Write a function that returns the sum of digits of a given number.
Example: 1234 → 10
"""
# a=1234

# b= a%10
# c= a//10
# print(b)
# print(c)

# b = 0
# while True :
#     b +=a%10
#     a=a//10
#     if a == 0:
#         break
# print(b)

"""
Move All Zeros to the End
Write a Python function to move all zeros in a list to the end while maintaining the order of other elements.
Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0].
"""
# a = [0,1,0,3,12]
# b=[]
# c=[]

# for i in a :
#     if i == 0:
#         c.append(i)
#     else:
#         b.append(i)

# result=b+c
# print(result)

"""
Find the Longest Word in a Sentence
Write a function that takes a sentence and returns the longest word.
Example: "The quick brown fox" → "quick" or "brown"
"""
# def big(sentence):
#     word=sentence.split(" ")
#     length=""
#     for i in word:
#         if len(i)>len(length):
#             length=i
        
#     return length

# print(big("The quick brown fox"))
        

# a = [1,2,3,4,3,5]
# b=[1,2,4,5,5,6]
# a=set(a)
# b=set(b)
# print(a.intersection(b))


"""
set 24-D
# """
# a="This is a learning program"
# print(len(a.split(" ")))

"""
Write a function that checks if a given strinig has all unique characters.
it returns True if all characters are unique (no duplicate character found) or False
ex:- 
given string:- "test",returns false as "False is duplicated and machine,returns "True",as all characters are unique
"""

# a="Erangoud"
# b=""
# for char in a:
#     if char not in b:
#         b+=char
#     else:
#         print("False") 
#         break
# else:
#     print("True")

"""
check the enetred number is prime or not !

"""
# def fun(n):
#     if n>1:
#         for i in range(2,(n//2)+1):
#             if (n%i)==0:
#                 print("not a prime")
#                 break
#         else:
#             print("its a prime ")

#     else:
#         print("not a prime")
# fun(7)

"""
product of array except itself
"""
#output:- [24,12,8,6]
# a=[1,2,3,4]
# b=[]
# for i in range(len(a)):
#     v=1
#     for j in range(len(a)) :
#         if i == j:
#             continue
#         else:
#             v *=a[j]
#     b.append(v)
    
# print(b)

"""
Binary search implementation
"""

# a=[1,2,3,4,5,6,7]
# target=3
# for i in range(len(a)):
#     if a[i]== target:
#         print(f"the target index is {i}")

""""
Find Duplicates
"""

# a=input("enter the numbers")
# b=[int(i)for i in a.split(",")]
# print(b)
# f=[]
# # c={}
# # for i in b:
# #     if i not in c:
# #         c[i]=1
# #     else:
# #         c[i]+=1

# # for i in c.items():
# #     if i[1] >1:
# #         f.append(i[0])

# # print(f)
# from collections import Counter
# c=Counter(b)
# print(c)

# for i in c.items():
#     if i[1]>1:
#         f.append(i[0])

# print(f)


# a=["ate","tea","eat"]
# b=[]
# for i in a:
#     for j in a:
#         if sorted(i)==sorted(j):
#             b.append(j)

# print(b)

# from abc import ABC,abstractmethod
# class Car(ABC):
    
#     @abstractmethod
#     def engine(self,n):
#         print(n)
        


# class Owner(Car):
#     def engine(self,n):
#         super().engine(n)
#     def colur(self):
#         print("hi")


# eran=Owner()
# print(eran.engine(3))

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"Book: {self.title} by {self.author}"

#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}')"

# book = Book("1984", "George Orwell")
# print(book)   # Output: Book: 1984 by George Orwell
# # print(repr(book))  # Output: Book('1984', 'George Orwell')
"""
"""


# a = "hi everyone"
# b=[]
# c=""
# for i in a:
#     b.append(i)

# for i in range(len(b)-1,-1,-1):
#     c+=b[(i)]
# print(b)
# print(c)

"""

"""

# class Calculator:
#     def add(self,a,b,c=0,d=0):
#         return a+b+c+d
#     def sub(self,a,b,c=0,d=0):
#         return a-b-c-d
#     def mul(self,a,b,c=1,d=1):
#         return a*b*c*d
#     def div(self,a,b,c=1,d=1):
#         return a/b/c/d

# ob1=Calculator()   
# while True :
#     print("1:- add ")
#     print("2:- sub ")
#     print("3:- mul ")
#     print("4:- div ")
#     print("5:- exit ")
#     z= int(input("enter your choice : "))
#     a= int(input("enetr the digits to add "))
#     b= int(input("enter the digit "))
#     match z:
#         case 1:
#             print(ob1.add(a,b))
#         case 5:
#             break

# from collections import Counter

# a="aaabbc"
# b= Counter(a)
# c=""
# for i in b.items():
#     # print(i)
#     c+=(i[0]+str(i[1]))

# print(c)

"""
i/p: [4,8,9,5,6,7,9]
o/p: [8,4,5,9,7,6,9]

"""
# a=[1,2,3,4,5,6,7,8]
    # [3,4,1,2,7,8,5,6]
# for i in range(0,len(a),2):
#     print(i)
#     if i == len(a)-2:
#         break
#     else:
#         a[i],a[i+2]=a[i+2],a[i]
# print(a)


"""
|
|
|
|
|
|
|
"""
# a=[1,2,3,4,5,6,7,8]
# for i in range(0,len(a),4):
#     if len(a)==len(a)-1:
#         break
#     a[i:i+2],a[i+2:i+4]=a[i+2:i+4],a[i:i+2]

# print(a)



# a=[1,2,3,4]
# b=[]
# for i in range(len(a)):
#     v=1
#     for j in range(len(a)):
#         if i==j:
#             continue
#         else:
#             v*=a[j]
#     b.append(v)

# print(b)

# a=[1,2,3,4,5,6,7]
# def bin(target):
#     for i in range(len(a)-1):
#         if a[i]==target:
#             return i
#     else:
#         return -1     
# print(bin(5))



# custom_filter.py
# def to_uppercase(value):
#     return value.upper()

# class FilterModule(object):
#     def filters(self):
#         return {"to_uppercase": to_uppercase}

# print("hello"| to_uppercase)

"""
##
# """
# a = [3,1,2,4]
# b=[]
# c=[]
# for i in a:
#     if i%2 == 0:
#       b.append(i)
#     else:
#         c.append(i)
    

# print(b+c)

"""
Create a method whether a string is anagram or not 
"""
# from collections import Counter
# def anagram(string1,string2):
#     string1=string1.replace(" ","").lower()
#     string2=string2.replace(" ","").lower()
#     if Counter(string1) == Counter(string2):
#         return True
#     else :
#         return False

# print(anagram("Desperation","A rope Ends it"))

"""
write a program to return sum of digits 
# """
# a = 123
# b=0
# while a>0:
#     temp=a%10
#     a=a//10
#     b+=temp

# print(b)

a =[3,1,4,1,5,9,2,6,5]
b= []
for i in a:
    if i not in b:
        b.append(i)
        
b.sort()
print(b)