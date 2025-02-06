import csv 
"""write  a csv file """

data = [
    ["name","age"],
    ["eran",21],
    ["goud",22]
]

with open("test.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("test.csv","r",newline="") as file :
    data = csv.reader(file)
    for row in data:
        print(row)

    
with open("test.csv","r",newline="")as file:
    data = csv.DictReader(file)
    for i in data :
        print(i)

data = [
    {"name":"eran","age":21},
    {"name":"goud","age":22}
]

with open("dict.csv","w",newline="") as file :
    dat = csv.DictWriter(file,fieldnames=["name","age"])
    dat.writeheader()
    dat.writerows(data)

with open("dict.csv","r",newline="") as file :
    data = csv.DictReader(file)
    for row in data :
        print(row)



f = open("demo1.txt", 'r')
# f.write("hello1")
print(f.read())
f.close()

with open("demo.txt",'w') as file:
    file.write("Pushpa")

