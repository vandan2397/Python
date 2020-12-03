# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:54:25 2020

@author: Vandan
"""


#exception handling
# =============================================================================
n1=10
n2=0

try:
    d=n1/n2
    print(d)
except Exception:
    print("number cannot be divided by 0")
#     
# =============================================================================
#

#custom exception handling
#custom exception class    
class namematching(Exception):
    def __init__(self,msg):
        super().__init__(msg)


try:
    f = open('text.txt')
    if f.name == 'text.txt':
        raise namematching('File name matching')    # raise custom exception
#specific exception of file not found 
except FileNotFoundError as e:
    print(e)
#general exception
except Exception as e:
    print(e)
#executes the code
else:
    print(f.read())
    f.close()
#Finally code must executes
finally:
    print('Always executes')


#index error exceptions  
list1=[1,2,3,4]

try:
    print(list1[5])
except IndexError as a:
    print(a)
    

#key error exceptions
dict1={'name':'vandan','last':'pandya'}
try:
    print(dict1['age'])
except KeyError:
    print("key not found in dictionary")


#multiple exceptions
try:
    for i in range(0,10):
        print(i) 
except (IndentationError, SyntaxError):
    print(SyntaxError)
    print('Indentation error')
  
#type exceptions    
try:
    Str='vandan'
    print(sum(Str))
except TypeError:
    print('Type error')


















    
    