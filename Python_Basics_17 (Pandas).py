# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:56:35 2020

@author: Vandan
"""

import pandas as pd
import numpy as np

#to read csv file
dataframe = pd.read_csv('nyc_weather.csv')
dataframe

#shape of data
shape=dataframe.shape

#columns
cols=[i for i in dataframe.columns]
cols

#datatype of columns
dataframe.dtypes

#count of each attribute in column
print(dataframe['Events'].value_counts(normalize=True))

#count of unique values
print(dataframe.nunique())
    
#value values in individual values
for i in dataframe.columns:
    print('COLUMN: ',i)
    print(dataframe[i].unique())
    print(" ")
    
#Null values
dataframe.isnull().sum()

#fill null values with mean, mode
dataframe['Events'].fillna(dataframe['Events'].mode()[0],inplace=True)
dataframe['WindSpeedMPH'].fillna(dataframe['WindSpeedMPH'].mode()[0],inplace=True)

#replace
dataframe.replace({'Temperature':'[A-Za-z]',
                   'WindSpeedMPH':'[A-Za-z]'},'',regex=True, inplace=True)
dataframe['PrecipitationIn'].mode()[0]
dataframe['PrecipitationIn'].replace(to_replace='T',value=0,inplace=True)

#type conversion
dataframe = dataframe.astype({"EST":'datetime64', "Temperature":'float64','WindSpeedMPH':'float64',
                              'PrecipitationIn':'float64','Events':'category'}) 


#reseting index
dataframe.set_index('EST',inplace=True)

#display data using index
dataframe.loc['2016-01-01']

#loc to slice dataframe 
print(dataframe.loc[['2016-01-01','2016-01-02'],["Temperature",]])

#iloc to slice dataframe
dataframe.iloc[5:,:]



#statistical description
stats=dataframe.describe()
print(round(stats,2))
print(dataframe.describe(include=['category']))
print(dataframe.describe(include='all'))



#add column
dataframe['Moisture'] = 'Yes'
#drop column
dataframe.drop(['Moisture'],axis=1,inplace=True)




#filtering data
dataframe[cols[1:]][dataframe['Temperature']==max(dataframe['Temperature'])]

dataframe[cols[1:]][dataframe['Events'].isin(['Rain','Snow'])]

dataframe[cols[1:]].iloc[0:10,:][(dataframe['WindSpeedMPH']>5) & (dataframe['DewPoint']==23)]

filt = (dataframe['Events']=='Rain')
#filters opposite of condtion
dataframe.loc[~filt]

#filter data according to string present in column
filt2 = dataframe['Events'].str.contains('Python',na=False)
dataframe.loc[filt2]



#sorting
dataframe2 = pd.DataFrame({'Name':['vandan','abhishek','vandan',],'Last':['pandya','shevale','patel'],'Data':[10,20,30]})

dataframe2.sort_values(by='Name')

#sort with 2 fields
dataframe2.sort_values(by=['Name','Last'],ascending=False,inplace=False)

dataframe2.sort_values(by=['Name','Last'],ascending=[False,True])


#filter function

#extracts selected columns
col_df = dataframe.filter(['CloudCover','Events']) 


# Using regular expression to extract all 
# columns which has letter 'a' or 'A' in its name. 
a = col_df.filter(regex ='[aA]') 


# select columns by regular expression
col_df.filter(regex='RAI$', axis=1)

# select rows containing 'bbi' index
dataframe.filter(like='RAIN', axis=1)


# filter according to substring
data[data['Species'].str.contains('versi')]








#update data in dataframe
#change column name
dataframe2.columns = ['first name','last name','data']

dataframe2.columns = [i.lower() for i in dataframe2.columns]

dataframe2.columns = dataframe2.columns.str.replace(' ','_')

#change name of specific column
dataframe2.rename(columns={'first_name':'first'},inplace=False)

#update rows
dataframe2.loc[2,['first_name','last_name']] = ['darshana','pandya']

#get a row by a field and change value of other field
filt = (dataframe2['data']==30)
dataframe2.loc[filt, 'first_name']='Niketa'

#append a row
df=pd.DataFrame({'first_name':['Parth'],'last_name':['gandhi'],'data':40})
dataframe2=dataframe2.append(df, ignore_index=True)

#apply() function
def upper_case(last):
    return last.upper()

dataframe2['last_name'] = dataframe2['last_name'].apply(upper_case)

#manipulating values using lambda function
dataframe2['first_name'] = dataframe2['first_name'].apply(lambda x: x.upper())

len(dataframe2['first_name']) 

dataframe2.apply(len)
dataframe2[['first_name','last_name']].applymap(len)

#replace
dataframe2['data'].replace(to_replace=10,value=5,inplace=True)

#map
#map will affect other values 
dataframe2['data'].map({10:20,30:50})


#numeric to category 
#Tenure to categorical column
def tenure_lab(Data) :
  if Data["tenure"] <= 12 :
        return "Tenure_0-12"
  elif (Data["tenure"] > 12) & (Data["tenure"] <= 24 ):
        return "Tenure_12-24"
  elif (Data["tenure"] > 24) & (Data["tenure"] <= 48) :
        return "Tenure_24-48"
  elif (Data["tenure"] > 48) & (Data["tenure"] <= 60) :
        return "Tenure_48-60"
  elif Data["tenure"] > 60 :
        return "Tenure_gt_60"
    
Data["tenure_group"] = Data.apply(lambda Data:tenure_lab(Data), axis = 1)








#grouping
#groups data by particular field
group_events = dataframe.groupby(['Events'])
Rain=group_events.get_group('Rain')

group_events['Temperature'].value_counts()#.loc['Snow']

#aggregation
group_events['Temperature'].agg(['mean','median']).loc['Snow']

#apply on group object
group_events['Temperature'].apply(lambda x: sum(x==25))

#concatenation
conacat_df = pd.concat([dataframe['Temperature'],dataframe['Events']],axis=1)


dataframe3 = pd.read_csv('weather_by_cities.csv')
grp_city = dataframe3.groupby('city')
grp_city

#iterate over
for city, city_df in grp_city:
    print(city)
    print(city_df)

grp_city.plot()



#merge
india_temp = pd.DataFrame({'city':['mumbai','gujarat','delhi','chennai'],'temperature':[30,40,50,60]})
india_hum = pd.DataFrame({'city':['mumbai','gujarat','rajasthan'],'hum':[80,70,56]})

#intersection
pd.merge(india_hum,india_temp,on='city')

#left table
pd.merge(india_hum,india_temp,on='city',how='left')

#union
pd.merge(india_hum,india_temp,on='city',how='outer')

india_1 = pd.DataFrame({'city':['mumbai','gujarat','delhi','chennai'],'temperature':[30,40,50,60],'humidity':[50,40,30,20]})
india_2 = pd.DataFrame({'city':['mumbai','gujarat','rajasthan'],'temperature':[40,50,60],'humidity':[80,70,56]})
df3 = pd.merge(india_1,india_2,on='city',suffixes=('_left','_right'))



#stack
dataframe4 = pd.read_excel('stocks.xlsx',header=[0,1])
dataframe4.stack()
dataframe4.stack(level=0)
dataframe4.unstack()


#crosstab
dataframe5 = pd.read_excel('survey.xls')
pd.crosstab(dataframe5.Sex,dataframe5.Handedness,margins=True)
pd.crosstab(dataframe5.Nationality,[dataframe5.Handedness,dataframe5.Sex],margins=True)







#time series
#converting to datetime before creating dataframe
parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
time_df = pd.read_csv('time_series.csv',parse_dates=['Date'],date_parser=parser)

#convering to date time after loading
time_df['Date']= pd.to_datetime(time_df['Date'], format='%Y-%m-%d %I-%p')

#day name function
time_df['Week']=time_df['Date'].dt.day_name()

#number of days
time_df['Date'].max() - time_df['Date'].min()

#filter
filt = (time_df['Date'] >='2019-01-01') & (time_df['Date']<'2019-02-01')
time_df.loc[filt]

#set datetime as index
time_df.set_index('Date',inplace=True)

#slice data using index
time_df['2020-01-01':'2020-02-01']

#mean during this period
time_df['2020-01-01':'2020-02-01']['High'].mean()

#resampling
#daywise
#gets maximum value of every day
d=time_df['2020-01-01':'2020-02-01']['High'].resample('D').max()

#visualization 
d.plot()

#Monthly
w=time_df['2020-01-01':'2020-02-01']['High'].resample('M').max()

#aggregation function
time_df.resample('D').agg({'Close':'mean','High':"max",'Low':'min','Volume':'sum'})



#change format of date
date1 = time_df.loc[0:3,['Date']]
date1['Date'] = date1['Date'].apply(lambda x: x.strftime('%d/%m/%y'))
#date1['Date']= pd.to_datetime(date1['Date'], format='%Y-%m-%d %I-%p')
type(date1['Date'][0])


#convert to datetime using datetime
from datetime import datetime
date_time_str = '18/09/19 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')




#difference between dates
data2 = pd.read_excel('Date.xlsx')
data2['Date1']= pd.to_datetime(data2['Date1'], format='%Y-%m-%d %I-%p')
data2['Date2']= pd.to_datetime(data2['Date2'], format='%Y-%m-%d %I-%p')

data2['Age'] = data2['Date1'] - data2['Date2']
data2['Age'] = data2['Age']/np.timedelta64(1,'D')

data2['Age_yrs'] = data2['Date1'] - data2['Date2']
data2['years'] = round(data2['Age_yrs']/np.timedelta64(1,'Y'))


#Age from birth date
now = pd.Timestamp('now')   # 1
data2['dob'] = data2['Date2'].where(data2['Date2'] < now, data2['Date2'] -  np.timedelta64(100, 'Y'))   # 2
data2['age'] = (now - data2['dob']).astype('<m8[Y]')    # 3


















#read and write data from different sources

#read from csv
df = pd.read_csv('survey_results_public.csv', index_col='Respondent',sep=None)

#create csv from dataframe
filt = (df['Country']=='India')
df_india=df.loc[filt]
df_india.to_csv('india_dev.csv')

#tab delimeter file
df_india.to_csv('india_dev.csv',sep='\t')


#import data from excel file 
excel_df = pd.read_excel('demo.xlsx',header=1)

#export data to excel file
df_india.to_excel('india_dev.xlsx', sheet_name='india')



#to read data from json
json_df = pd.read_json('india_dev.json')


#to export data in json format 
df_india.to_json('india_dev.json',orient=None,lines=None)


#import data from sql databases
#import sqlalchemy
#Alchemy is an orm which helps to connect with databases
import sqlalchemy

#connection
engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/application')


#read entire table from sql
df = pd.read_sql_table('customers',engine)

#read few columns
df = pd.read_sql_table('customers',engine, columns=[''])


#read data using query
df_q = pd.read_sql_query('select id, name from customers', engine)


#read data by joining two tables
query = '''
 SELECT customers.name, customers.phone_number, orders.name, orders.amount
 FROM customers INNER JOIN orders
 ON customers.id=orders.customer_id
'''
df1 = pd.read_sql_query(query,engine)



#provide column name according to name of coulmns in table
df.rename(columns={
    'Customer Name': 'name',
    'Customer Phone': 'phone_number'
}, inplace=True)
    
    
#write to mysql database 
df.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=False
) 


#read_sql is wrapper around read_sql_query and read_sql_table
pd.read_sql(query,engine)







