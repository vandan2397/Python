# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 14:12:10 2020

@author: Vandan
"""


# list comprehension program
# squares even numbers
list1 = [-2,-3,1,2,3,4,5,6,7,8,9,10]

list2 = [i**2 for i in list1 if i % 2==0]

print(list2)

# positive numbers
list3 = [i for i in list1 if i>0 ]


#string
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
words_1=[word for word in words if word!='the']



# Patterns 
for i in range(1,6):
        print(" "*(6-i),"*"*i)

for i in range(0,5):
        print(" "*(5-i),"*"*i)
        
        
#Debugging
def display(first,last):
    var = 10
    print('Hello {} {}'.format(first,last))
    var=20
    sum=var+250
    print(sum)
    
name1='vandan'
last1='pandya'    
display(name1,last1)


def func(n):
    for i in range(1,n):
        for j in range(i):
            print(i, end=" ")
        print(" ")    
func(7)
    
    
    
    
    
    