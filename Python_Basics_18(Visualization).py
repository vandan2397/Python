# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:16:36 2020

@author: Vandan
"""

import pandas as pd
import matplotlib.pyplot as plt #import matplotlib library
import numpy as np

#import data
data = pd.read_csv('Iris.csv')
data.set_index('Id',inplace=True)

#simple line plot
x = [1,2,3,4]
y = [4,2,3,1]
plt.plot(x,y,label='line1')
plt.xlabel('X axis') #label x axis
plt.ylabel('Y axis') #label y axis
plt.title('Simple plot') #label title

#simple plot with two lines
#figure class
fig = plt.figure(figsize=(5,5))
plt.plot(data['SepalLengthCm'],data['SepalWidthCm'],label='Sepal',color='g')
plt.plot(data['PetalLengthCm'],data['PetalWidthCm'],label='Petal')
plt.xlabel('Length in cm') #label x axis
plt.ylabel('Width in cm') #label y axis
plt.legend() #set legend
plt.title('IRIS') #label title

#plot with axes object
fig = plt.figure(figsize=(5,5))
ax = fig.add_axes([0,0,1,1])
x = [1,2,3,4,5]
y = [4,2,3,1,6]
x1 = [1,2,3,1,6]
y1 = [3,5,3,4,5]
ax.plot(x,y,label='line1')
ax.plot(x1,y1,label='line2')
ax.set_xlabel('X axis') #label x axis
ax.set_ylabel('Y axis') #label y axis
ax.legend(labels = ('Line 1', 'Line 2'), loc = 'lower right') #set legend
ax.set_xlim(0,6) #setting limit of x axis
ax.set_ylim(0,6) #setting limit of y axis
ax.set_title('Simple plot') #label title

# subplots
# 4 plots in one graph
fig = plt.figure(figsize=(10,10))
fig, ax =  plt.subplots(nrows=2,ncols=2) #rows and columns
x = np.arange(1,5)
ax[0][0].plot(x,x*x) #first plot
ax[0][0].grid(True)
ax[0][0].set_title('square')
ax[0][1].plot(x,np.sqrt(x)) #second plot
ax[0][1].set_title('square root')
ax[1][0].plot(x,np.exp(x)) #third plot
ax[1][0].set_title('exp')
ax[1][1].plot(x,np.log10(x)) #fourth plot
ax[1][1].set_title('log')
#plt.tight_layout()
plt.show()
#plt.gcf()


#twin axes
#a graph can have dual axes
fig = plt.figure()
a1 = fig.add_axes([0,0,1,1])
x = np.arange(1,11)
a1.plot(x,np.exp(x),'gs--')
a1.set_ylabel('exp')
a2 = a1.twinx()
a2.plot(x, np.log(x),'ro-')
a2.set_ylabel('log')
fig.legend(labels = ('exp','log'),loc='upper left')
plt.show()


###############################################################################################
#bar plot
#It is generally used with categorical variable
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
a1=data['Species'].unique()
a1=list(a1)
count = data['Species'].value_counts()
count = list(count)
ax.bar(a1,count)
plt.show()


#Side by side bar plots
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
x_index = np.arange(len(ages_x))
py_dev_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
ax.bar(x_index+ 0.00, py_dev_y, color="#008fd5", label="Python",width = 0.25)

js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
ax.bar(x_index + 0.25, js_dev_y, color="#e5ae38", label="JavaScript",width = 0.25)
ax.set_xticks(x_index)
ax.set_xticklabels(ages_x)
ax.legend(labels=['Python', 'Java'])
plt.show()


#stacked bar plots
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]
ax.bar(ages_x, py_dev_y, color="#008fd5", label="Python")
js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]
ax.bar(ages_x, js_dev_y, color="#e5ae38", label="JavaScript")
ax.legend(labels=['Python', 'Java'])
plt.show()

###############################################################################################
#Histogram

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.hist(data['SepalLengthCm'],label='Length',bins=10)
ax.hist(data['SepalWidthCm'],label='Width',bins=10)
ax.legend(labels=['Length', 'Width'])
ax.set_xlabel('Size')


#step filled histogram
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.hist(data['SepalLengthCm'],label='Length',bins=10,histtype='step')
ax.plot(bins=10)

###############################################################################################
#Pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
prog_lang = ['Julia', 'Java','Go','Python']
Developers = [45372, 48876, 53850, 57287]
ax.pie(Developers, labels = prog_lang,autopct='%1.2f%%')
plt.show()

###############################################################################################
#Scatter plot
fig = plt.Figure(figsize=(10,10))
ax = fig.add_axes([0,0,1,1])
ax.scatter(data.SepalLengthCm,data.SepalWidthCm)
ax.scatter(data.SepalLengthCm,data.PetalWidthCm)
ax.set_xlabel('Length')
ax.set_ylabel('Width')
plt.show()


#other way
data.plot.scatter(x='SepalLengthCm',y='SepalWidthCm')
plt.show()

plt.scatter(data.SepalLengthCm,data.SepalWidthCm,label='Sepal',color='r')
plt.scatter(data.PetalLengthCm,data.PetalWidthCm,label='Petal',color='b')
plt.xlabel('Length')
plt.ylabel('Width')
plt.legend()

###############################################################################################
#boxplot
fig = plt.Figure(figsize=(10,10))
#ax = fig.add_axes([0,0,1,1])
#d=data.iloc[:,0:4]
plt.boxplot([data['SepalLengthCm'],data['SepalWidthCm']])
plt.show()


###############################################################################################
#violin plot
fig = plt.Figure(figsize=(10,10))
ax = fig.add_axes([0,0,1,1])
#d=data.iloc[:,0:4]
ax.violinplot([data['SepalLengthCm'],data['SepalWidthCm']])
plt.show()


###############################################################################################







