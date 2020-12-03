# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:01:10 2020

@author: Vandan
"""

import re

# Search 
txt = "The rain in Spain"
# matches starting and ending string
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# Multiple Occurences
string1 = 'The abc abc end'
y = re.search('^The.abc*.*end$',string1)

if y:
  print("YES! We have a match!")
else:
  print("No match")


# Regular expression for email
string2 = 'vandan@gmail.com'
y = re.search('[a-z]+@[a-z]+\.[a-z]+',string2)

if y:
  print("YES! We have a match!")
else:
  print("No match")
  

# other pattern
string3 = 'Code: 333-abda'
z = re.search('^[0-9][0-9][0-9]-[a-z]{4}$',string3)

if z:
  print("YES! We have a match!")
else:
  print("No match")


# Methods of match object
string4 = 'Phone no: 999-888-9999'
p = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',string4)

if p:
  print("YES! We have a match!")
else:
  print("No match")


# group() method to extract string matching pattern
print('No. :',p.group())


# Returns whole string where it matches pattern
print('String :',p.string)


# returns position (start- and end-position) of the first match occurrence
print('Position :',p.span())



# Retrieve all groups at once
string5 = r'My no. 818-252-8976'
x = re.search(r'(\d\d\d)-(\d\d\d-\d\d\d\d)',string5)
print(x.group(1))


# Using re.compile
heroRegex = re.compile (r'Batman|Tina Fey') 
mo1 = heroRegex.search('Batman and Tina Fey.') 
print(mo1.group())


# Findall Method
# returns a list containing all matches

txt = "The rain in Spain"
x = re.findall("Spain", txt)
print(x)



txt2 = 'Phone numbers: 999-888-9999 , 998-898-9776 , 155-676-8876'
p = re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',txt2)
print(p)



txt3 = 'vandan2@gmail.com raj3@gmail.com parth23@gmail.com'
c = re.findall(r'[a-z]+[0-9]*@[a-z]+\.[a-z]+',txt3)
print(c)


# Split Method
# Returns a list where the string has been split at each match 
str1 = 'foo635bar4125mango2apple21orange'
#split with regular expression
chunks = re.split('\d+',str1)
print(chunks)



str2 = "The rain in Spain"
# splits the string at the first white-space character
x = re.split("\s", str2, 1)
print(x)


str3 = "vandan,raj,parth"
x = re.split(",", str3)
print(x)

str4 = "Vandan rgr123 parth rgr123 raj"
x = re.split("\s\w{3}\d{3}\s", str4)
print(x)



# sub method
# Replaces one or many matches with a string

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


txt2 = "Hey this is @ I am vandan Pandya @" 
x = re.sub("[^a-zA-Z0-9\s]", "5", txt2)
print(x)


# Replace the first 2 occurrences
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

















