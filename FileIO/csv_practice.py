import csv
"""Writing to a Csv file """
data =[
    ["name","age"],
    ["eran",21]
]

with open("data1.csv","w",newline="") as file  :
    writer=csv.writer(file)
    writer.writerows(data)


# with open("data1.csv","r",newline="") as file :
#     data=csv.reader(file)
#     for row in data :
#         print(row)

# """Reading a CSV file """
# with open("data.csv","r",newline="") as file :
#     data= csv.reader(file)

#     for row in data:
#         print(row)

# print(data)

# """Reading CSV as a dictionary"""

with open("data1.csv","r",newline="") as file :
    data=csv.DictReader(file)
    for row in data:
        if row["name"] == "ram":
            print(row["age"])


"""Writing a csv file as a dict"""
data1=[
    {"na":"eran","age":21},
    {"na":"goud","age":22}
]

with open("dict.csv","w",newline="")as file :
    data=csv.DictWriter(file,fieldnames=["na","age"])
    data.writeheader()
    data.writerows(data1)



# with open("dict.csv","r",newline="") as file :
#     data=csv.DictReader(file)
#     for row in  data:
#         print(row)