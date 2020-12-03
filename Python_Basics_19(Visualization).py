# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:39:17 2020

@author: Vandan
"""

import pandas as pd #import pandas library
import matplotlib.pyplot as plt #import matplotlib library
import numpy as np #import numpy library
import seaborn as sns #import seaborn library 

#import data
data = pd.read_csv('Iris.csv')
data.set_index('Id',inplace=True)


#color palletes
#It is used to give colors to plots
#palplot is used to plot the array of colors horizontally.
current_palette = sns.color_palette(palette='husl',n_colors=5)
sns.palplot(current_palette)
plt.show()

sns.palplot(sns.color_palette('Greens'))
plt.show()


#Distplot for visualization of distribution
sns.distplot(data['SepalLengthCm'], bins=None,hist=True,kde=True)
sns.distplot(data['SepalWidthCm'], hist=True)
plt.show()

#kde plot
#Kernel Density Estimation (KDE) is a way to estimate the probability density function of a continuous random variable
fig = plt.figure(figsize=(10,10))
sns.kdeplot(data['PetalWidthCm'], color='b', shade=True,Label='None') 
sns.kdeplot(data['PetalLengthCm'], color='r', shade=True,Label='None') 
plt.show()

#jointplot
#It combines two plots: Scatter plot and distribution plot
sns.jointplot(data['PetalWidthCm'],data['PetalLengthCm'])
plt.show()

#It combines two plots: contour plot and distribution plot
sns.jointplot(data['PetalWidthCm'],data['PetalLengthCm'],kind='kde')
plt.show()

# hexbin plot
#It is used when data is too much scattered and difficult to analyze
sns.jointplot(data['PetalWidthCm'],data['PetalLengthCm'],kind='hex')
plt.show()



filt = (data['Species']=='Iris-setosa')
df1 = data.iloc[:,0:4][filt]

filt2 = (data['Species']=='Iris-versicolor')
df2 = data.iloc[:,0:4][filt2]

filt3 = (data['Species']=='Iris-virginica')
df3 = data.iloc[:,0:4][filt3]

fig = plt.figure(figsize=(10,10))
sns.kdeplot(df1['PetalWidthCm'],df1['PetalLengthCm'], cmap="Reds", shade=True, bw=.15,label='Iris-setosa')
sns.kdeplot(df2['PetalWidthCm'],df2['PetalLengthCm'], cmap="Blues", shade=True, bw=.15,label='Iris-versicolor')
sns.kdeplot(df3['PetalWidthCm'],df3['PetalLengthCm'], cmap="Greens", shade=True, bw=.15,label='Iris-virginica')
plt.show()

#Pairplot
#It helps to show relationship between multiple variables
sns.set_style("ticks")
sns.pairplot(data,hue = 'Species',diag_kind = "hist",kind = "scatter",palette = "deep")
plt.show()


#rug plot
#It shows distribution in form of sticks
sns.rugplot(data['PetalLengthCm'])


#To plot categorical data
#It is used to check relationship between categorical and numerical variable

#striplots
fig = plt.figure(figsize=(5,5))
#sns.stripplot(data['Species'], y = data['PetalLengthCm'],jitter=True)
sns.stripplot(data['Species'], y = data['PetalWidthCm'],hue=None,jitter=True)
plt.show()


#swarm plots
fig = plt.figure(figsize=(5,5))
sns.swarmplot(data['Species'], y = data['PetalWidthCm'],hue=None)
plt.show()

#boxplot
#Boxplot is a convenient way to visualize the distribution of data through their quartiles
fig = plt.figure(figsize=(10,10))
sns.boxplot(data['Species'], y = data['PetalWidthCm'],hue=None)
#sns.stripplot(data['Species'], y = data['PetalWidthCm'],hue=None,jitter=True)
plt.show()
sns.boxplot(data=data.iloc[:,0:4],orient='h')




#violin plot
#It is combination of boxplot and kde. It helps to easily understand distribution of data
sns.stripplot(data['Species'], y = data['PetalWidthCm'],hue=None)
sns.violinplot(data['Species'], y = data['PetalWidthCm'],color='w',hue=None)
plt.show()

#catplot
sns.catplot(x="sex", y="total_bill",hue="smoker", col="time", data=data, kind="strip",
                height=4, aspect=.7);

            
#bar plot
#It shows mean
sns.barplot(data['Species'],data['PetalLengthCm'], hue = None)
plt.show()
data['PetalLengthCm'][data['Species']=='Iris-setosa'].mean()


#countplot
sns.countplot(data['Species'], hue = None)
plt.show()

#point plot
sns.pointplot(data['Species'],data['PetalLengthCm'], hue = None)
sns.pointplot(data['Species'],data['PetalWidthCm'], hue = None,color='r')
plt.show()


#factor plot
sns.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin', col = "diet", data = data);
plt.show()


#heatmap
#correlation with heatmap
sns.heatmap(data.corr(),annot=True,cmap='YlGnBu')



#regression plot
sns.regplot(data['PetalWidthCm'],data['PetalLengthCm'])

#Implot
sns.lmplot(x='PetalWidthCm',y='PetalLengthCm',data=data,order=2)
plt.show()


#FacetGrid class helps in visualizing distribution of one variable as well 
#as the relationship between multiple variables separately within subsets 
#of your dataset using multiple panels.
df = sns.load_dataset('tips')
g = sns.FacetGrid(df, col = "sex",row='time', hue = "smoker")
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()


#facetgrid 
g = sns.FacetGrid(df, col = "sex",row='time', hue = "smoker")
g.map(sns.distplot, "total_bill")
plt.show()



#Pairgrid
g = sns.PairGrid(data, diag_sharey=True,palette = "deep")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot)



#displays data in 1 row and 4 column
penguins = sns.load_dataset("penguins")
x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
y_vars = ["body_mass_g"]
g = sns.PairGrid(penguins, hue="species", x_vars=x_vars, y_vars=y_vars)
g.map_diag(sns.kdeplot, color=".3")
g.map_offdiag(sns.scatterplot)
g.add_legend()








