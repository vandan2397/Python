# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:23:59 2020

@author: Vandan
"""


class file_management:  
    
    def __init__(self,filename):
        self.filename = filename
    
    #reading file        
    def read_file(self):
        try:
            self.f = open(self.filename,'r',encoding='utf-8')
            a = self.f.read()
            print(a)
        except Exception as e:
            print(e)
        finally:
            self.f.close()
            
    #overwrites content in file 
    def write_file(self):
        try:
            self.f = open(self.filename,'w',encoding='utf-8')
            a = str(input())
            self.f.write(a)
            print('File Successfully Written!')
        except Exception as e:
            print(e)
        finally:
            self.f.close()
    
    #appends content in file
    def append_file(self):
        try:
            self.f = open(self.filename,'a',encoding='utf-8')
            a = str(input())
            self.f.write(a)
            print('Successfully Appended!')
        except Exception as e:
            print(e)
        finally:
            self.f.close()      

#Instance of class
file1=file_management('text3.txt')

#read function 
file1.read_file()

#write fucnction
file1.write_file()

#append function
file1.append_file()

##############################################################################################

#Few operations on file

#read first n lines
f1 = open('text4.txt','r')
n = int(input('How many lines you need to read?'))
file_1 = f1.readlines()
for i in range(0,n):
    print(file_1[i],end="")
    
    
#change content of particular line
f2 = open('text4.txt','+r')
n = int(input('Enter Line number: '))
content='content changed\n'
lines=f2.readlines()
lines[n-1] = content
f2.close()

f3 = open('text4.txt','w')
f3.writelines(lines)
f3.close()

f4 = open('text4.txt','r')
a = f4.read()
print(a)


#replace words
f5 = open('text5.txt','r')
words = f5.read()
new_words = words.replace('game','name')
f5.close()

f6 = open('text5.txt','w')
f6.write(new_words)
#c=f5.read()
#print(c)
f6.close()


###########################################################################################
#read and write in csv file

import csv

with open('csv1.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #read content
    #for i in csv_reader:
        #print(i[1])
    
    
    with open('csv1_new.csv','w') as csv_file_n:
        csv_writer = csv.writer(csv_file_n)
    
        for line in csv_reader:
            csv_writer.writerow(line)
    

#to read using dictreader
with open('csv1.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    #for line in csv_reader:
        #print(line)
    
    with open('csv2.csv','w') as csv_file_w:
        fieldnames=['Customer Name','Country']
        csv_writer = csv.DictWriter(csv_file_w,fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for line in csv_reader:
            #del line['Country']
            csv_writer.writerow(line)
















