# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:38:59 2020

@author: Vandan
"""

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False


has_lucky_number([0])


def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)

def myFun(**kwargs): 
    for key, value in kwargs.items():
        print ("{} == {}".format(key, value))
 
# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks') 

list_num=[1,2,3,4]
mul=1
for i in list_num:
    mul*=i
print(mul)

a=['abc', 'xyz', 'aba', '1221']
count=0
for i in a:
    if len(i) >= 2 and i[0]==i[-1]:
        count+=1
print(count)