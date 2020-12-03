# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:30:30 2020

@author: Vandan
"""

class string_operation:
    def __init__(self):
        pass
    
    def upp_low(self,*str1):
        print("Uppercase: ", str1[0].upper())
        print("Lowercase: ", str1[1].lower())
        
    def concat(self,*str1):
        print("Concatenation ",str1[0] + str1[1] )
    
    def sub_string(self,str1,str2):
        #if str1.find(str2) == -1:
        if str1 in str2 == True:
            print('Substring found')
        else:
            print('No Substring found')
    
    def type_string(self,str1):
        if str1.isalnum() == True:
            print('String is alphanumeric')
        if str1.isalpha() == True:
            print('String is alphabetic')
        if str1.isnumeric() == True:
            print('It is numeric')
    
    def reverse(self,str1):
        print('reverse string: ', str1[::-1])
            

o = string_operation()
#converts string to uppercase and lowercase 
o.upp_low('vandan','PANDYA')

#concatenates two string
o.concat('vandan','PANDYA')

#checks substring within string
o.sub_string("vandan",'ka')

#checks type of string
o.type_string('vandan') 

#reverse string
o.reverse('vandan')

##########################################################################################

#formatting strings using format method
name = 'Vandan'
print('My name is {}'.format(name))

#default order
order = 'Names of students: {}, {} and {}'.format("Vandan","Raj","Parth")
print(order)

#positional order
pos_order= 'Name of students {1}, {0} and {2}'.format("Vandan","Raj","Parth")
print(pos_order)

#keyword order
key_order = 'Name of students {c}, {a} and {b}'.format(a="Vandan",b="Raj",c="Parth")
print(key_order)

#round off
print('number is {0:.2f}'.format(1/3))

############################################################################################
#Splitting
#it will split string in to list
str1 = 'I am a intern data scientist'
lst = str1.split()  

#joining 
str2 = ' '.join(lst)

#replace
str2=str2.replace('intern','junior')

#escape sequence
str3 = 'hey \nhow are you?'
print(str3)

#strip spaces
str4 = '     vandan  pandya   '
print(str4.strip())

#check white spaces
txt = "   "
x = txt.isspace()
x

#get index of character
print(str2.index('d'))

str5='game game game play play cricket'
print(str5.count('game'))




