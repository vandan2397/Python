# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:42:28 2020

@author: Vandan
"""



#exception within loop
while True:
    try:
        a = int(input())
        b = int(input())
        c = a/b
        print("Answer: ", c)
    except Exception as e:
        print("Error: {}".format(e))
    else:
        break

#index error
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


while True:   
    try:
        a = input()
    except EOFError as e:
        print(e)


#type error        
try :
    ny = 'Statue of Liberty'
    my_list = [3, 4, 5, 8, 9]
    print(my_list + ny)
except TypeError as e:
    print(e)
        


#attribute exception
class toy():
    def __init__(self):
        self.a = 'Vandan'
obj = toy()

try:
    print(obj.a)
    print(obj.c)
except AttributeError:
    print("No such attribute")

#nameerror
try:
    books = ["Near Dark", "The Order", "Where the Crawdads Sing"]
    print(boooks)
except NameError:
    print('Not defined')