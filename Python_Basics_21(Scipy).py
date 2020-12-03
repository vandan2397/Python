# It is used to solve the complex scientific and mathematical problems. 
#It is built on top of the Numpy extension, which means if we import the SciPy, 
#there is no need to import Numpy.

import numpy as np
import seaborn as sns

#stats module
#It contains a large number of statistics, probability distributions functions. 

#Distributions
#uniform distribution
from scipy.stats import uniform
data_uniform = uniform.rvs(size=1000, loc = 10, scale=20)
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')


#normal distribution
from scipy.stats import norm
data_normal = norm.rvs(size=10000,loc=0,scale=1)
ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


#Posisson distribution
from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)
ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')


#bernoulli distribution
from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)
ax= sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')


#to compute cdf
print(norm.cdf(np.array([1,10, 20, 11, 30, 4, -2, 6])))






#linear algebra
from scipy import linalg

#soling equation
#Declaring the numpy arrays
a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])
#Passing the values to the solve function
x = linalg.solve(a, b)
#printing the result array
print(x)



#Calculating determinant
A = np.array([[1,2],[3,4]])
#Passing the values to the det function
x = linalg.det(A)
#printing the result
print(x)



#eigen vectors and eigen values
A = np.array([[1,2],[3,4]])
#Passing the values to the eig function
l, v = linalg.eig(A)
#printing the result for eigen values
print(l)
#printing the result for eigen vectors
print(v)



#singular value decomposition
#Declaring the numpy array
a = np.random.randn(3, 2) + 1.j*np.random.randn(3, 2)
#Passing the values to the eig function
U, s, Vh = linalg.svd(a)
# printing the result
print(U, Vh, s)








#Statistical hypothesis test
# p value less than 0.05 which means that probablity of occurunce of null hypothesis is less
# than 5 %

#Some tests do not return a p-value, requiring an alternative method 
#for interpreting the calculated test statistic directly.
#In given case stat refers to critical values
import pandas as pd
data = pd.read_csv('Iris.csv')
data.set_index('Id',inplace=True)


#Normality test
#This are test which can be used to check if your data has a gaussian distribution
#If the P-value is less than (or equal to) , then the null hypothesis is rejected 
#in favor of the alternative hypothesis. And, if the P-value is greater than , 
#then the null hypothesis is not rejected.
from numpy import random
norm = random.normal(100,size=(10000))

# Example of the Shapiro-Wilk Normality Test
from scipy.stats import shapiro
stat, p = shapiro(data['SepalLengthCm'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')

#plot    
sns.distplot(data['SepalLengthCm'])


#Example of the Anderson darling test
from scipy.stats import anderson
result = anderson(data['SepalLengthCm'])
print('stat=%.3f' % (result.statistic))
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < cv:
		print('Probably Gaussian at the %.1f%% level' % (sl))
	else:
		print('Probably not Gaussian at the %.1f%% level' % (sl))


#Example of the D agistino test
from scipy.stats import normaltest
stat, p = normaltest(norm)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably Gaussian')
else:
	print('Probably not Gaussian')
        


#correlation test
#statistical tests that you can use to check if two variables are related.
#h0: No significance between two variables  
#h1: Significance between two variables
    

#pearson correlation coefficient test 
from scipy.stats import pearsonr
stat, p = pearsonr(data['SepalLengthCm'], data['PetalLengthCm'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')
    
sns.regplot(data['SepalLengthCm'],data['PetalLengthCm'])



#Spearman's correlation coefficient test 
from scipy.stats import spearmanr
stat, p = spearmanr(data['SepalLengthCm'], data['PetalLengthCm'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')
    
sns.regplot(data['SepalLengthCm'],data['PetalLengthCm'])



#Kendall's Rank Correlation Test
from scipy.stats import kendalltau
stat, p = kendalltau(data['SepalLengthCm'], data['PetalLengthCm'])
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')



#Test for categorical variables
#Chi square test
from scipy.stats import chi2_contingency
dataset=sns.load_dataset('tips')
dataset_table=pd.crosstab(dataset['sex'],dataset['smoker'])
print(dataset_table)

stat, p, dof, expected = chi2_contingency(dataset_table)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably independent')
else:
	print('Probably dependent')


#one sample T test 
#The test will tell us whether means of the sample and the population are different
from scipy.stats import ttest_1samp
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]

#take a sample
sample_size=10
age_sample=np.random.choice(ages,sample_size)

ttest,p_value=ttest_1samp(age_sample,30)

if p_value < 0.05:
    print(" There is significance, we are rejecting null hypothesis")
else:
    print("There is no significance, we are accepting null hypothesis")


#two sample t test 
#The Independent Samples t Test or 2-sample t-test compares the means of two independent groups 
#in order to determine whether there is statistical evidence that the associated population 
#means are significantly different. 
from scipy.stats import ttest_ind
import scipy.stats as stats

np.random.seed(12)
ClassB_ages=stats.poisson.rvs(loc=18,mu=33,size=60)
classA_ages=stats.poisson.rvs(loc=18,mu=30,size=60)
ClassB_ages.mean()
_,p_value=stats.ttest_ind(a=classA_ages,b=ClassB_ages,equal_var=False)
if p_value < 0.05:    # alpha value is 0.05 or 5%
    print("There is significance we are rejecting null hypothesis")
else:
    print("There is no significance we are accepting null hypothesis")


#paired test
#When you want to check how different samples from the same group are,
#you can go for a paired T-test
from scipy.stats import ttest_rel
weight1=[25,30,28,35,28,34,26,29,30,26,28,32,31,30,45]
weight2=weight1+stats.norm.rvs(scale=5,loc=-1.25,size=15)

weight_df=pd.DataFrame({"weight_10":np.array(weight1),
                         "weight_20":np.array(weight2),
                       "weight_change":np.array(weight2)-np.array(weight1)})    

_,p_value=stats.ttest_rel(a=weight1,b=weight2)
if p_value < 0.05:    # alpha value is 0.05 or 5%
    print("There is significance, we are rejecting null hypothesis")
else:
    print("There is no significance, we are accepting null hypothesis")




#Anova test
#one way
#A test that allows one to make comparisons between the means of three or more groups of data.

#two way
#A test that allows one to make comparisons between the means of three or more groups of data, where two independent variables are considered.     
    
df_anova = data[['PetalWidthCm','Species']]
grps = pd.unique(data['Species'])

d_data = {grp: data['PetalWidthCm'][data['Species']==grp] for grp in grps}

F, p = stats.f_oneway(d_data['Iris-setosa'], d_data['Iris-versicolor'], d_data['Iris-virginica'])

if p < 0.05:
    print("There is significance, reject null hypothesis")
else:
    print("There is no significance, accept null hypothesis")





#z score shows how much a data is far from mean. It standardize the distribution bu making
# sd=1 and mean 0.
#It can also be used to find outliers.
from scipy import stats
z_score = np.abs(stats.zscore(data[data.columns].iloc[:,0:4]))
print(z_score)
cols = [cols for cols in data.columns if data[cols].dtype != 'O']
data_without_outliers = pd.DataFrame(data[(z_score < 3).all(axis=1)], columns = cols)

    
    
    
    



#Non parametric test 
#Mann whitney test 
# This test is used to check whether distributions of two independent samples same or not
 
# Example of the Mann-Whitney U Test
from scipy.stats import mannwhitneyu
from numpy import random
norm1 = random.normal(100,size=(100))
norm2 = random.normal(100,size=(100))
stat, p = mannwhitneyu(norm1, norm2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')

    
    
# Krushkal-Wallis H test 
# This test is used to check whether distributions of two independent samples same or not    
from scipy.stats import kruskal
norm1 = random.normal(100,size=(100))
norm2 = random.normal(100,size=(100))
stat, p = kruskal(norm1, norm2)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Probably the same distribution')
else:
	print('Probably different distributions')


#skew test
# itis used to test skewness in distribution
#skewness = 0 : normally distributed.
#skewness > 0 : more weight in the left tail of the distribution.
#skewness < 0 : more weight in the right tail of the distribution. 
    

from scipy.stats import skew 
import numpy as np  
import pylab as p  
  
x1 = np.linspace( -5, 5, 1000 ) 
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2  ) 
  
p.plot(x1, y1, '*') 
  
print( '\nSkewness for data : ', skew(y1)) 


#describe
print(stats.describe(data[cols]))


