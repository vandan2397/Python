# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:37:19 2020

@author: Vandan
"""
#tuple
tup1 = (1,2,3,4)
tup2 = (5,6,7,8)
tup3 = (1,2,3,4)


#len
print('length', len(tup1))


#add elements
tup1 = tup1 + (10,)


#compare
if (tup1>tup3)-(tup1<tup3) == 0:
    print('Same tuples')
else:
    print('Not same')


#slicing tuple
tupr = tup1[::-1]
tup5 = tup1[1:]


#generators
#generators can be used instead of tuples to modify elements
#elements in generator can be accesed by iterating over it
tup6 = (1,2,3,4)
tup6 = (i**2 for i in tup6)
for i in tup6:
    print(i)
    


# Dictionary
dict1 = {'name':'vandan','last':'pandya','age':24}

#access elements
print(dict1['name'])
print(dict1.get('age'))

#changing elements
dict1['age']=23
dict1['game']='cricket'


print(dict1)

#making dictionary from 2 list 
names = ['vandan','raj','parth','shreyak']
lnames = ['Pandya','patel','gandhi','patel']
#print (zip(names,lnames))

dict_n={name:lname for name, lname in zip(names,lnames)}
print(dict_n)

#keys and items
print(dict1.keys())
print(dict1.values())
#seperate object with keys and values
print(dict1.items())


#pop 
element=dict1.pop('game')
print('element popped', element)


#update
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)

#dictionary comprehensions
dict3 = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
dict4 = {k:v+5 for (k,v) in dict3.items() if v%2==0}

#nested dictionary
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)





#set
list1 = [1,2,3,4,5,2,3]
set1 = set(list1)
set2 = {2,3,11,12,22,23}

#add element
set1.add(10)
print(set1)

#union
print(set1.union(set2))

#intersection
print(set1.intersection(set2))

#difference
print(set1.difference(set2))

set1.difference_update(set2)
print(set1)

#pop
set1.pop()

#remove
set1.remove(1)

#symmetric difference
print(set1.symmetric_difference(set2))


#set comprehensions
set3 = {i*2 for i in range(1,10)}
print(set3)



#Generators
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
# Using for loop
for item in my_gen():
    print(item)


#you can also iterate using next
a = my_gen()
next(a)




