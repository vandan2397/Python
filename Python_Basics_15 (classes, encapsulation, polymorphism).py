# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:17:24 2020

@author: Vandan
"""

#polymorphism 
#Ability to take more than one form
class India:
    def capital(self):
        print('Capital of the India is New Delhi')
    def language(self):
        print('National language of the India is Hindi')
    def game(self):
        print('National game of the India is Hockey')
class America:
    def capital(self):
        print('Capital of the America is Washington DC')
    def language(self):
        print('National language of the America is English')
    def game(self):
        print('National game of the America is Baseball')

#create objects
ind = India()
usa = America()

#iterate over tuple containing objects to call their respective functions 
for i in (ind,usa):
    i.capital()
    i.language()
    i.game()


#polymorphism with inheritance
class animal:
    def __init__(self,name):
        self.name = name
        print('{} is an animal'.format(self.name))
    
class cow(animal):
    def __init__(self,name):
        super().__init__(name)
        
    def type(self):
        print('{} is a herbivorous animal'.format(self.name))

class lion(animal):
    def __init__(self,name):
        super().__init__(name)
        
    def type(self):
        print('{} is a carnivorous animal'.format(self.name))

def call_methods(obj):
    obj.type()

cow1 = cow('cow')
call_methods(cow1)
lion1 = lion('lion')
call_methods(lion1)


    
#encapsulation
class salary:
    
    def __init__(self):
        #private varaible
        self.__salary=1000
    
    def display(self):
        print('salary: ', self.__salary)
    
    def setter(self,amt):
        self.__salary = amt

#instantiate
s = salary()
s.display()

#trying to change value of variable
s.salary=1200
s.display()

#uses setter method to change varible
s.setter(1200)
s.display()



#Class methods and static methods

class employee:
    amount=1000
    def __init__(self,name,last,age):
        self.name = name
        self.last = last
        self.age = age
    #decorators to declare a class method
    #takes first argument as class
    #it takes string and converts into object
    @classmethod
    def string_obj(cls,str1):
        name, last, age = str1.split(',')
        return cls(name, last, age)
    
    #class method to change value of class variable
    @classmethod
    def change(cls,amt):
        cls.amount=amt
            
    def display(self):
        print('name {}'.format(self.name))
        print('last {}'.format(self.last))
        print('age {}'.format(self.age))
        print('amount {}'.format(self.amount))
        
    @staticmethod
    def is_adult(age):
        if age>18:
            return	True
        return	False
    
    def __repr__(self):
        return 'employee({},{},{})'.format(self.name,self.last,self.age)
    
    def __str__(self):
        return 'employee({},{},{})'.format(self.name,self.last,self.age)
    

print('amount before: {}'.format(employee.amount))    
emp1 = employee.string_obj('vandan,pandya,24')
employee.amount = 1200

#emp1 = employee(name, last, age)
print(emp1.display())

#Static method
print(employee.is_adult(23))

#dunder methods
print(emp1.__str__())
print(emp1.__repr__())



#decorators
class customer:
    def __init__(self,name,last):
        self.name = name
        self.last = last
    
    @property
    def fullname(self):
        return 'full name: {} {}'.format(self.name,self.last)
    
    @fullname.setter
    def fullname(self,name,last):
        self.name = name
        self.last = last
    
cust1 = customer('vandan','pandya')
print(cust1.fullname)
cust1.name='vedant'
print(cust1.fullname)















