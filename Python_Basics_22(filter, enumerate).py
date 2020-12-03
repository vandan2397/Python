# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:11:18 2020

@author: Vandan
"""

#filter
#The filter() method filters the given sequence with the help of a function 
#that tests each element in the sequence to be true or not.

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
    
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

filtered = filter(fun, sequence) 
for i in filtered:
    print(i)



#using lambda function
list1 = [1,2,3,4,5,6,7,8]
result = filter(lambda x: x%2==0, list1)
print(list(result))



#enumerate
#Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
for i,j in enumerate(sequence):
    print(i,j)
    
    
for i,j in enumerate(sequence,100):# start of counter
    print(i,j)    
    
#reduce
#reduce applies a function of two arguments cumulatively to the elements of an iterable
from functools import reduce 
my_numbers = [10,2,4,6]    
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(reduce_result)