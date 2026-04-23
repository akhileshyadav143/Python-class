# # sum
# lst=[[1,2,3][3,4,5][3,4,5][5,7,3,2]]
# lst1=[sum(i) for i in lst]
# print(lst1)
# # min
# lst=[[1,2,3][3,4,5][3,4,5][5,7,3,2]]
# lst1=[min(i) for i in lst]
# print(lst1)

# wap tp compute the differnce between two lists.

# smaple data:["red","orange","green","blue","white"],["black","yellow","green","blue"]
# Expected output


# color1 = ["red","orange","green","blue","white"]
# color2 = ["black","yellow","green","blue"]

# lst1 = []
# lst2 = []

# # elements in color1 but not in color2
# for i in color1:
#     if i not in color2:
#         lst1.append(i)

# # elements in color2 but not in color1
# for i in color2:
#     if i not in color1:   
#         lst2.append(i)

# print("Color1 - Color2:", lst1)
# print("Color2 - Color1:", lst2)     


# wap  to pack consentive duplicare of a given list of element int sub liste
# original list:[0,0,1,2,3,4,4,6,6,6,7,8,9,4,4]
# after packing constrive dupli
# 
# 
lst = [0,0,1,2,3,4,4,6,6,6,7,8,9,4,4]

# lst1 = []
# lst2 = [lst[0]]

# for i in range(1, len(lst)):
#     if lst[i] == lst[i-1]:
#         lst2.append(lst[i])
#     else:
#         lst1.append(lst2)
#         lst2 = [lst[i]]


# lst1.append(lst2)

# print("Packed List:", lst1)                                        


lst = [0,0,1,2,3,4,4,6,6,6,7,8,9,4,4]
lst1=0
if lst1[-1]!=1:
    lst1.append(i)
print(lst1)    