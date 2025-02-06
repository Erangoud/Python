list1=['S001', 'S002', 'S003', 'S004']
name=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
score=[85, 98, 89, 92]

dict2={}
#output:- {'s001':{'name':'adina park','score':85}}

for i in range(len(list1)):
    dict2[list1[i]] = {'name':name[i],'score':score[i]}

print(dict2)