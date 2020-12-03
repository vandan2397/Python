# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:24:10 2020

@author: Vandan
"""
class employee:
    #class variable
    company='Google'
    salary_raise=1.05
    tot_emp = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        employee.tot_emp += 1
        
        
class business_executive(employee):
    bus_tot = 0
    def __init__(self,name,age,post,salary):
        super().__init__(name,age)
        self.post = post
        self.salary = salary
        business_executive.bus_tot += 1
    
    def details(self):
        print('Name of an employee: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Position: {}'.format(self.post))
        print('Salary: {}'.format(self.salary * 1.10))
        print('Company: {}'.format(self.company))

class developer(employee):
    dev_tot = 0
    def __init__(self,name,age,post,salary):
        super().__init__(name,age)
        self.post = post
        self.salary = salary
        developer.dev_tot += 1

    def details(self):
        print('Name of an employee: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Position: {}'.format(self.post))
        print('Salary: {}'.format(self.salary * 1.20))
        print('Company: {}'.format(self.company))    


dev1 = developer('Vandan',24,'developer',100000)
dev1.details()
dev2 = developer('Raj',25,'developer',200000)
dev2.details()
bus1 = business_executive('Parth',24,'Business',100000)
bus1.details()


#number of employees
print("total employees: ", employee.tot_emp)
print("business executives: ", business_executive.bus_tot)
print("developers: ", developer.dev_tot)
