# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:15:26 2020

@author: Vandan
"""

import errno

try:
   file_name = open('Data.txt')
# 2 is 'No such file or directory'
except IOError as e:
   if e.errno == 2:
      print(e.strerror)
      print("File to be printed no found")
      # handle exception



def file(file_name):
    try:
        #context manager
        #with open(file_name,'r') as f:
        f = open(file_name)
        print('File name: '+f.name)
        print('File mode: '+f.mode)
        #f.write('hey')
        #seek can change the marker
    except FileNotFoundError as e:
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
    else:
        print(f.read())
      
#Finally code must executes
    finally:
        print('Always executes')
        f.close()
        
file('text.txt')

#copy content of one file to another
with open('text2.csv','r') as fr:
    with open('text2.txt','w') as fw:
        content = fr.read()
        fw.write(content)