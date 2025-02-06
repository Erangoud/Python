"""
1.Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# nums = [2,7,11,15] 
# target = 9
# output=[]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             output=[i,j]
#             break
#     if output:
#         break

# print(output)


"""
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

# nums = [3,2,4]
# target = 6
# output= []

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         print(nums[i],nums[j])
#         if nums[i]+nums[j] == target:
#             output=[i,j]
#             break
#     if output:
#         break

# print(output)


"""
Input: nums = [3,3], target = 6
output: [0,1]
"""
# nums = [3,3]
# target = 6
# output= []

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         print(nums[i],nums[j])
#         if nums[i]+nums[j] == target:
#             output=[i,j]
#             break
#     if output:
#         break

# print(output)


"""
2.Reverse Integer:
Input= 123
output: 321
Input: -4576
output: -6754
"""
# input= 123
# output: 321

# reversed_string = str(input)[::-1]
# print(reversed_string)

# input2 =-4576
# output2=-6754

# a = -int(str(-input2)[::-1])
# print(a)

# a="-int(str(-input2)[::-1])"
# print(len(a))


#questions in interactions 

# dict1 = {
#     "name":[],
#     "age":21
# }

# dict1["name"].append("Eran")
# dict1["name"].append("goud")
# dict1["name"].remove("Eran")
# print(dict1)

# while True:
#     count = 0
#     for i in range(1,5):
#         print(i)
#         count+=1
#     if count <=5:
#         break

#from abc import ABC,abstractmethod

"""
*
**
***
****
"""

# num = int(input("enter the number "))
# for i in range(1,num):
#     for j in range(i):
#         print("*",end="")   
#     print("")

"""
*****
****
***
**
*
"""

# for i in range(num,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print("")

# data ="Role and Playbook both are the same in principle. It has individual files. Instead of having a single file that contains everything that you need – one for variables, one for tasks, and another for handlers."
# with open("new_text.txt","w") as file:
#     file.write(data)

# import re 

# pattern = r"(?<=that).*"
# with open("new_text.txt","r") as file:
#     d = file.read()
#     searched=re.findall(pattern,d)
#     print(searched)

# pattern = r"need(.*)"
# with open("new_text.txt","r") as file:
#     d = file.read()
#     searched=re.search(pattern,d) # returns the object to print that matched object use .group()
#     print(searched.group(1)) # one represents what ever captured after the need inside a group 



# ram mohan asked questions
# txt="luckyram9392@gmail.com"
# reverse=txt[::-1]
# # print(reverse)
# for char in reverse:
#     print(char)

# import re
# pattern=r"\d+"
# d = re.search(pattern,txt)
# print(d.group())

# read local file from remote complier or local 
# import os 
# d = os.listdir("D:/")
# print(d)

# import csv
# data=[
#     {"name":"eran","age":212131},
#     {"name":"goud","age":212132},
#     {"name":"ram","age":313121}
# ]

# with open("z.csv",'w',newline="") as file :
#     writer= csv.DictWriter(file,fieldnames=["name","age"])
#     writer.writeheader()
#     writer.writerows(data)

# with open("z.csv","r",newline="") as file :
#     d= csv.DictReader(file)
#     print(d)
#     for row in d :
#         if int(row["age"]) >= 20 and int(row["age"]) <30 :
#             print(row["name"])


# import re
# pattern =r"2121.*"
# with open("z.csv","r",newline="") as file :
#     d= csv.DictReader(file)
#     print(d)
#     for row in d :
#         if re.findall(pattern,row["age"]) :
#             print(row["name"])


# punith 


# class Car:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# ob1=Car("Bmw",21000000)
# # print(ob1.name)


# str1= "hii"

# try:
#     print(str1)
# except Exception as e:
#     print(e)


# a="punith223@gmail.com"
# b=a.split("@")
# print(b)
import re 
# pattern=r"(.*)@(.*)"
# d=re.search(pattern,a)
# print(d.group(1),d.group(2))





"""4.Given an array nums, write a function to move all zeroes to the end of it while
maintaining the relative order of the non-zero elements."""
# Input=[0,1,0,3,12]
# output1=[]
# output2=[]


# for i in Input:
#     if i >0:
#         output1.append(i)
#     elif i <1:
#         output2.append(i)

# output=output1+output2
# print(output)


"""
Input: [1,7,0,0,8,0,10,12,0,4]
Output: [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
"""

# input= [1,7,0,0,8,0,10,12,0,4]
# output2=[]
# output1=[]

# for i in input:
#     if i >0:
#         output1.append(i)
#     if i<1:
#         output2.append(i)

# output=output1+output2
# print(output)



"""
5. Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,1]
Output: 1
Input: nums = [4,1,2,1,2]
Output: 4

"""
# nums=[2,2,1,1,1,1,1,3,3,3,3,3]
# my_dict={}
# for i in nums:
#     if i not in my_dict:
#         my_dict[i]=1
#     else:
#         my_dict[i] +=1

# print(my_dict[3])


# nums=[4,1,2,1,2]
# dict1={}

# for i in nums:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i] +=1

# print(dict1[1])


############

# txt = "340_egoud@gmail.com"
# pattern= r"\d+"
# import re
# print(re.findall(pattern,txt))


###########


# data="The toolbar offers several controls. Use the first two buttons for undoing and redoing edits. Adjust the minimum word length and minimum number of repeats using the sliders (third and fourth buttons on smaller screens). Toggle the fifth control to switch between case-sensitive and insensitive modes. The word and character counts are displayed on the right side."
# with open("text.txt","w") as file:
#     file.write(data)

# import re
# pattern = r"buttons"
# with open("text.txt","r") as file:
#     d=file.read()
#     dd=d.split(" ")
#     print(dd)
#     count=0
#     for i in dd:
#         if re.search(pattern,i):
#             count+=1

# print(count)




"""
6.Given an array nums of size n, return the majority element.
Input: nums = [3,2,3]
Output: 3
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# nums=[2,2,1,1,1,2,2]
# dict1={}

# for i in nums:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i] +=1

# major=[0,0]
# for i in dict1:
#     if dict1[i]>major[1]:
#         print(i)
#         major=[i,dict1[i]]



# print(major)

"""
8.Given a positive number, check if it is a perfect square without using any
built-in library function. A perfect square is a number that is the square of an
integer.
Input: n = 25
Output: true
Explanation: 25 is a perfect square since it can be written as 5×5.
Input: n = 20
Output: false

"""

# n= 36
# length =n//2
# for i in range(length):
#     for j in range(length):
#         if i == j and i * j == n:
#             print(i,"x",j)


"""
10.Given an integer array, in-place reverse it without using any inbuilt functions.
Input : [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""
# input=[1, 2, 3, 4, 5]
# output=[]
# # output=input[::-1]

# for i in reversed(input):
#     output.append(i)

# print(output)


"""
Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4
"""

# k = 3
# def print_3_smallest(array):
#     a=array.sort()
#     first=input[0]
#     second=input[1]
#     print(input[2])


# if __name__ == '__main__':
#     input=[7, 4, 6, 3, 9, 1]
#     print_3_smallest(input)


"""
Python has a built-in os module with methods for interacting with the operating system, 
like creating files and directories, 
management of files and directories, input, output, environment variables, process management, etc
"""
# import os
# print(os.path.isfile('data1.csv'))


# txt ="Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc"
# file=open("text.txt","w")
# file.write(txt)
# file.close


# import re 
# pattern =r"with(.*with)"
# with open("text.txt","r") as file:
#     d=file.read()
#     dd=re.search(pattern,d)
#     print(dd.group(1))


"""
11.Given a sorted integer array and a target, determine if the target exists in the
array in logarithmic time. If a target exists in the array, the procedure should
return the index of it.
Input: nums[] = [2, 3, 5, 7, 9], target = 7
Output: 3
Explanation: Element found at 4th (index 3) position
"""

# nums=[2, 3, 5, 7, 9]
# target=7
# pos=["1st","2nd","3rd","4th"]
# for i in range(len(nums)):
#     if nums[i] ==  target:
#         print(f"Element found at {pos[i]} (index {i}) position")


"""
19.Create a function that takes two numbers as arguments (num, length) and
returns a list of multiples of num until the list length reaches length.
Examples
list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]
"""

# def multiples(num,length):
#     a=num
#     while length>0:
#         print(a)
#         a=num+a
#         length -=1

# multiples(3,10000000)


"""
20.Given a string containing unique letters, return a sorted string with the letters
that don't appear in the string.
Examples:
get_missing_letters("abcdefgpqrstuvwxyz") ➞ "hijklmno"
get_missing_letters("zyxwvutsrq") ➞ "abcdefghijklmnop"
get_missing_letters("abc") ➞ "defghijklmnopqrstuvwxyz"
get_missing_letters("abcdefghijklmnopqrstuvwxyz") ➞ ""


"""
# alpha="abcdefghijklmnopqrstuvwxyz"
# input="abcdefgpqrstuvwxyz"
# a=""
# for char in alpha:
#     if char not in input:
#         a +=char

# print(a)



"""
A 
b C
d E f
G h I j
"""
# a=0
# k=0
# for i in range(0,5):
#     for j in range(0,i):
#         if k%2==0:
#             print(chr(a+65),end=" ")
#         else:
#             print(chr(a+97),end=" ")

#         a+=1
#         k+=1
#     print("")

# a=0 
# k=0
# num=4
# for i in range(a,num+1):
#     for j in range(i):
#         if k%2==0:
#             print(chr(a+65),end=" ")
#         else:
#             print(chr(a+97),end=" ")
        
#         a+=1
#         k+=1
#     print("")


import practice

print(practice.add(10,3))
print(practice.__name__)