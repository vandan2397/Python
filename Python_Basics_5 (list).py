# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:38:35 2020

@author: Vandan
"""

# list

list1 = ['a','b','c']
list2=[1,2,3,3]

#sort
list1.sort(reverse=True)
print(list2)

#insert
list2.insert(1,3)

#remove
list2.remove(3)

#extend
list1.extend(list2)
list3 = list1 + list2
list3

#delete at index
del list2[0]

list_1 = ["M", "na", "i", "Ke"] 
list_2 = ["y", "me", "s", "lly"]

#combining elements of same index
list3=[]
for i,j in zip(list_1,list_2):
    list3.append(i+j)
    
#list comprehensions
list_4 = [i+j for i in zip(list_1,list2)]    

#list operation
list5 = ["Hello ", "take "]
list6 = ["Dear", "Sir"]
list7=[]

for i in list5:
    for j in list6:
        list7.append(i+j)
        
list7 = [i+j for i in list5 for j in list6]   

#
list9 = [10, 20, 30, 40]
list10 = [100, 200, 300, 400]
for i,j in zip(list9,list10[::-1]):
    print(i,j)


#remove space
list11 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list11 = [i for i in list11 if i != "" ]


#remove all occurences of a number in list
list12 = [5, 10, 15, 20, 25, 50, 20]
list12 = [i for i in list12 if i !=20]


#replace value
for i in list12:
    if i == 20:
        index1=list12.index(i) 
        list12[index1]=200


#slicing    
print(list10[-1])



 
    
    