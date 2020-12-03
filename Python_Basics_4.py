# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:45:25 2020

@author: Vandan
"""
#Basic Operators

#Arithmentic operators

def operation(i,a,b):
    switcher={
            1:a+b,
            2:a-b,
            3:a*b,
            4:a/b,
            5:a//b,
            6:a%b,
            7:a**b
            }
    return switcher.get(i,"Invalid input")


print("1) Addition")
print("2) Subtraction")
print("3) Multiply")
print("4) Division")
print("5) Floor Division")
print("6) Mod")
print("7) Power")
print("Select Operation")
i = int(input())
print("Input number 1:")   
a = int(input())
print("Input number 2:")
b = int(input())
operation(i,a,b)


#Relational Operators
a = 10
b = 2
  
# a > b is True 
print(a > b) 
  
# a < b is False 
print(a < b) 
  
# a == b is False 
print(a == b) 
  
# a != b is True 
print(a != b) 
  
# a >= b is True 
print(a >= b) 
  
# a <= b is False 
print(a <= b) 



#Logical Operators
x = True
y = False
#and 
print(x and y)

#or
print(x or y)

#not 
print(not x)


#assignment operator
sum = 0
mul = 1
for i in range(0,10):
    sum += i
print(sum)

for i in range(1,10):
    mul *= i
print(mul)


#special operators
a=3
b=3
#is
print(a is b)

#is not
print(a is not b)


#membership operators
list_1 = [1,2,4,6]

#in
print(1 in list_1)

#not in 
print(1 not in list_1)


# conditional statements and Data types
num = 10

if type(num)==int:
    print("type is integer")
elif type(num)==float:
    print("type is float")
elif type(num)==complex:
    print("type is complex")
elif type(num)==str:
    print("type is String")
elif type(num)==bool:
    print("type is Boolean")
elif type(num)==list:
    print("type is List")
elif type(num)==dict:
    print("type is dict")
    
















