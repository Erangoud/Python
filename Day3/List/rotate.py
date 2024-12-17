# 14. Write a python program to check whether two lists are circularly identica

def circular (list1,list2):

    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        rotated_list=list1[i:]+list1[:i]
        if rotated_list==list2:
            return True

    return False




list1 = [1, 2, 3, 4]
list2 = [3, 4, 1, 2]

print(circular(list1,list2))




'''
Example: Suppose list1 = [1, 2, 3, 4]:

When i = 0: list1[0:] = [1, 2, 3, 4], list1[:0] = [] → rotated_list = [1, 2, 3, 4].
When i = 1: list1[1:] = [2, 3, 4], list1[:1] = [1] → rotated_list = [2, 3, 4, 1].
When i = 2: list1[2:] = [3, 4], list1[:2] = [1, 2] → rotated_list = [3, 4, 1, 2].
When i = 3: list1[3:] = [4], list1[:3] = [1, 2, 3] → rotated_list = [4, 1, 2, 3].'''

