
file2 = open(r"C:\Users\egoud\OneDrive\Documents\Desktop\python\FileIO\example2.txt", "w")
file2.write("hello guys this is file IO ")
file2.close()


file2 = open(r"C:\Users\egoud\OneDrive\Documents\Desktop\python\FileIO\example2.txt", "r")
print(file2.read())


# using 'with' which automatically close the file 


with open(r"C:\Users\egoud\OneDrive\Documents\Desktop\python\FileIO\example2.txt", "w") as file:
    file.write("hi everyone :")
    file.write("\nthis is the second line")
    file.write("\nimage.jpg")


with open(r"C:\Users\egoud\OneDrive\Documents\Desktop\python\FileIO\example2.txt", "rb") as file :
    for line in file:
    # content=file.read()
        print(line.strip())  


with open("sample.txt","r") as file :
    data=file.read()

print(data)

repl=data.replace("pyhton","java")
print(repl)

with open("sample.txt","w") as file2 :
    file2.write(repl)



file = open("sample.txt","w")
file.write("hi everyone this is file io")
file.close()

file =open("sample.txt","r")
print(file.readlines())
file.close()

with open("sample.txt","a") as file :
    file.write("\n using with fun")
    file.write("\n using append and with ")

with open("sample.txt","r") as file:
    for line in file :
        print(line.strip())

with open("sample.txt","r") as file :
    data= file.read()
print(type(data))


with open("sample.txt","r") as file:
    data=file.read()
    if "fun" in data :
        print("found")
    else :
        print("not found ")

import re
with open("sample.txt","r") as file1:
    file2=file1.read()
    if re.findall(r"\bfun\b",file2):
        print(re.findall(r"\bfun\b",file2))
    else:
        print("no")