# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:28:09 2020

@author: Vandan
"""
#map it allows to apply function to iterate over iterable

list1 = [1, 2, 3] 
list2 = [4, 5, 6] 

a = lambda x: print(x**2)
print(a(2))
  
result = map(lambda x, y: x + y, list1, list2) 
print(list(result)) 


list_str=['vandan','pandya','raj','patel']
upp_case=map(lambda x: x.upper(),list_str)
#put into list
list_upp=list(upp_case)


dict1 = {'name':'vandan','last':'pandya','age':24}
upp_case_1=map(lambda x: len(x), dict1)
lis = list(upp_case_1)


list_customer = [{'country':'India', 'sales':120},{'country':'US', 'sales':100}]
country_key = map(lambda x: x['country'], list_customer)
print(list(country_key))