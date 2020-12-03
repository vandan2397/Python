# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:59:00 2020

@author: Vandan
"""

class Error(Exception):
    pass

class Large(Error):
    def __init__(self):
        self.message='Wrong guess! Too Large'
    def __str__(self):
        return self.message    
        
class Small(Large):
    def __init__(self):
        self.message='Wrong guess! Too Small'
    def __str__(self):
        return self.message  

class Correct(Small):
    def __init__(self):
        self.message='Right Guess!'
    def __str__(self):
        return self.message  

while True:
    try:
        num = int(input('Enter a number'))
        if num==10:
            raise Correct
        if num > 10:
            raise Large
        if num < 10:
            raise Small
    except Large as a:
        print(a)
    except Small as a:
        print(a)
    except Correct as a:
        print(a)