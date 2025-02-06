# import re 
# txt ="The python coding language"
# x=re.search("^The.*language$",txt)
# if x:
#     print("yes")
# else:
#     print("no")


import re 
txt = "The python coding language"
pattern = "^The.*language$"
x = re.search(pattern,txt)
print(x)
if x:
    print("yes")
else :
    print("no")

#set of characters
txt = 'The rain in spain '
x=re.findall('[a-m]',txt)
print(x)


# find all digits characters 
txt = "that will be 69 dollars"
x=re.findall("\d+",txt)
print(x)



# # # . 
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# x = re.findall("pl....", txt)
# print(x)

# # #  *
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
# x = re.findall("pla.*", txt)
# print(x)

# # #  +
# txt = "hello planet"
# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
# x = re.findall("he.+ ", txt)
# print(x)

# # # findall()
# txt = 'theee not is ee'
# x = re.findall("\s",txt)
# print(x)

# # # search()
# txt='thee rain in spain'

# x=re.search('\s',txt)
# print(x.start())

# # # split()
# txt = 'the rain in spain'
# x = re.split('\s',txt)
# print(x)

# #sub()
txt='the rain in spain'
x = re.sub("\s",'*',txt)
print(x)

