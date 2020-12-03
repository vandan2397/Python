# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:51:01 2020

@author: Vandan
"""
def file(file_name):
    try:
        #context manager
        #with open(file_name,'r') as f:
        #no need to explicitly close file if you use context manager
        f = open(file_name,'r+',encoding='utf-8')
        print('File name: '+f.name)
        print('File mode: '+f.mode)
        #reading file using read function
        #print(f.read())
        
        #reading file using while loop
        size_to_read=10
        content=f.read(size_to_read)
        while len(content)>0:
            print(content,end='')
            content=f.read(size_to_read)
        
        
        #reading file using for loop
        for line in f:
            print(line)
        
        
        #reading file using readlines
        #It returns a list holding all lines
        print(f.readlines()) 
        
        
        #seek function
        #It sets the cursor to particular position
        size_to_read=10
        content=f.read(size_to_read)
        print(content)
        f.seek(0)
        content=f.read(size_to_read)
        print(content)
        
        
        #tell function returns current file location
        size_to_read=10
        content=f.read(size_to_read)
        print(f.tell())
        
            
        #writing and appending content in file 
        #f.write('how can I help you?') 
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except IsADirectoryError as e:
        print(e)
    except ProcessLookupError as e:
        print(e)
#general exception
    except Exception as e:
        print(e)
#executes the code
    finally:
        print("Executes always")
        
file('text.txt')


    
#to remove file
import os
os.remove('rem.txt')
os.mkdir("test")
