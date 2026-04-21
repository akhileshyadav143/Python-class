# write a program to print the list of first and last element of each list of lists

# lst=[[23,45,76],[45,3,12],[3,5,20]]
# lst1=[]
# for i in lst:
#      lst1.append(i[0])
#      lst1.append(i[-1])
#      print(lst1)



 #  wap to claculate and oprint the sum of max elemenr=t of each list of lists.
# lst3=[[1,2,4,5],[3,5,4,3],[4,5,3,2]]
# ans=0
# for i in lst3:
#     ans+=max(i)
# print(ans)   



# lst3=[[1,2,4,5],[3,5,4,3],[4,5,3,2]]
# ans=0
# for i in lst3:
#     ans+=sum(i)
# print(ans) 


# wap a python progam to divide the list int two equal halves and print the sum of each half.
# lst=[2,4,6,8,3,5,8,9]
# print(sum(lst[:len(lst)//2])),
# print(sum(lst[len(lst)//2:
#               ]))
   
# wap  create a list divisibal by a 3 bettwenn 4 and 25 and print the list.
# lst=[]
# for i in range(4,26):
#     if i%3==0:
#         lst.append(i)
#     print(lst)

# lst=[i for i in range(4,26) if i%3==0]
# print(lst)


# wap to ceate a list of square of even no and square of odd no.
# lst=[6,9,12,18,21,24]
# lst1=[i**2 for i in lst if i%2==0]
# lst2=[i**2 for i in lst if i%2!=0]
# print(lst,"\n",lst1,"\n",lst2)


# lst=[2,3,4,5,2,4]
# lst1=['even'if i%2==0 else 'odd'for i in lst]
# print(lst1)


lst=[[23,45,76],[45,3,12],[3,5,20]]
lst1=[]


#write a program to calculate and print the sum of elemnts in each list of list and add the resultant value.without using sum()function

lst=[[1,2,4,5],[3,5,4,3],[4,5,3,2]]
lst1=[sum(i) for i in lst]
print(lst1)