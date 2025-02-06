import json 

"""Reading from the json file """
with open(r"C:\Users\egoud\OneDrive\Documents\Desktop\python\data.json","r") as file:
    data=json.load(file)

print(data["name"])
print(data["address"]["city"])

"""writing a json file """

data={
    "name":"Eran",
    "number":7795796117,
    "age":22
}

with open("output.json","w") as file :
    json.dump(data,file,indent=3)


"""Modifing a json file """

with open("output.json","r") as file :
    data=json.load(file)

data["name"]= "Goud"
data["carrier"] = "Devops"

with open("output.json","w") as file :
    json.dump(data,file,indent=4)


with open("output.json","r") as file :
    data = json.load(file)
    print(data)

    
"""some basics of json """
import json
data ={"name":"eran","number":78787878}
print(data)
print(type(data))
json_str=json.dumps(data,indent=4)
print(type(json_str))
print(json_str)