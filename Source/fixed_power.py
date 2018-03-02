

# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[120]:


import pandas as pd
import numpy as np
import os
import datetime


# In[124]:


files = os.listdir("..\\Data\\Power")


# In[125]:


files_2010 = [x for x in files if '2010' in x]


# In[126]:


path =  os.path.join ('..\\Data\\Power' , files_2010[0])
df = pd.read_csv(path)
for i in range(1, len(files_2010)):
    path =  os.path.join ('..\\Data\\Power' , files_2010[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)


# In[127]:


df.head()


# In[128]:


def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)


# In[129]:


df.head()


# In[131]:


df1 = df.copy()


# In[132]:


df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day


# In[133]:


df1 = df1[df1['Hour'] != '02*']


# In[134]:


df2= df1.copy()

df2 ['Hour'] = df2['Hour'].astype(int)


# In[136]:


len(df2)


# In[137]:


df2.head()


# In[138]:


df2 = df2.sort_values(by=['Date', 'Hour'])


# In[139]:


df2.head()


# In[140]:


df2 = df2.drop(['Date_'], axis=1)


# In[141]:


df2.head()


# In[142]:


df2 ['Year'] =  df2 ['Date'].dt.year
df3 = df2 [(df2['Year'] != 2009) & (df2['Year'] != 2011)]

df3 = df3.reset_index()


df3 = df3.drop(['index'], axis=1)


# In[145]:


df3.head()


# In[146]:


df_2010_power = df3.copy()


# In[153]:


df_2010_power.to_csv("..\\Data\\Power\\fixed\\df_2010.csv")


# In[ ]:


#### 2011


# In[164]:


files_2011 = [x for x in files if '2011' in x]
path =  os.path.join ('..\\Data\\Power' , files_2011[0])
df = pd.read_csv(path)
for i in range(1, len(files_2011)):
    path =  os.path.join ('..\\Data\\Power' , files_2011[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)


# In[165]:


def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)


# In[166]:


df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)


# In[167]:


df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2010) & (df2['Year'] != 2012)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)


# In[168]:


#change
df_2011_power = df3.copy()
df_2011_power.to_csv("..\\Data\\Power\\fixed\\df_2011.csv")






# In[169]:


##2012
files_2012 = [x for x in files if '2012' in x]
path =  os.path.join ('..\\Data\\Power' , files_2012[0])
df = pd.read_csv(path)
for i in range(1, len(files_2012)):
    path =  os.path.join ('..\\Data\\Power' , files_2012[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2011) & (df2['Year'] != 2013)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2012_power = df3.copy()
df_2012_power.to_csv("..\\Data\\Power\\fixed\\df_2012.csv")


# In[174]:


#### 2013


files_2013 = [x for x in files if '2013' in x]
path =  os.path.join ('..\\Data\\Power' , files_2013[0])
df = pd.read_csv(path)
for i in range(1, len(files_2013)):
    path =  os.path.join ('..\\Data\\Power' , files_2013[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2012) & (df2['Year'] != 2014)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2013_power = df3.copy()
df_2013_power.to_csv("..\\Data\\Power\\fixed\\df_2013.csv")


# In[175]:


#### 2014


files_2014 = [x for x in files if '2014' in x]
path =  os.path.join ('..\\Data\\Power' , files_2014[0])
df = pd.read_csv(path)
for i in range(1, len(files_2014)):
    path =  os.path.join ('..\\Data\\Power' , files_2014[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2013) & (df2['Year'] != 2015)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2014_power = df3.copy()
df_2014_power.to_csv("..\\Data\\Power\\fixed\\df_2014.csv")


# In[176]:


#### 2015

files_2015 = [x for x in files if '2015' in x]
path =  os.path.join ('..\\Data\\Power' , files_2015[0])
df = pd.read_csv(path)
for i in range(1, len(files_2015)):
    path =  os.path.join ('..\\Data\\Power' , files_2015[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2014) & (df2['Year'] != 2016)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2015_power = df3.copy()
df_2015_power.to_csv("..\\Data\\Power\\fixed\\df_2015.csv")


# In[177]:


#### 2016

files_2016 = [x for x in files if '2016' in x]
path =  os.path.join ('..\\Data\\Power' , files_2016[0])
df = pd.read_csv(path)
for i in range(1, len(files_2016)):
    path =  os.path.join ('..\\Data\\Power' , files_2016[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2015) & (df2['Year'] != 2017)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2016_power = df3.copy()
df_2016_power.to_csv("..\\Data\\Power\\fixed\\df_2016.csv")


# In[178]:


#### 2017

files_2017 = [x for x in files if '2017' in x]
path =  os.path.join ('..\\Data\\Power' , files_2017[0])
df = pd.read_csv(path)
for i in range(1, len(files_2017)):
    path =  os.path.join ('..\\Data\\Power' , files_2017[i])
    df1 = pd.read_csv(path)
    df = df.append(df1)

def hour_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[1]
df['Hour'] = df.apply(hour_extarct, axis = 1)
def date_extarct(row):
    a = row['Date']
    a=a.split(' ')
    return a[0]
df['Date_'] = df.apply(date_extarct, axis = 1)

df1 = df.copy()
df1 ['Date'] = pd.to_datetime(df1.Date_)
df1 ['Month'] = df1 ['Date'].dt.month
df1 ['Day'] = df1 ['Date'].dt.day
df1 = df1[df1['Hour'] != '02*']
df2= df1.copy()
df2 ['Hour'] = df2['Hour'].astype(int)
df2 = df2.sort_values(by=['Date', 'Hour'])
df2 = df2.drop(['Date_'], axis=1)

df2 ['Year'] =  df2 ['Date'].dt.year
#change
df3 = df2 [(df2['Year'] != 2016) & (df2['Year'] != 2018)]
df3 = df3.reset_index()
df3 = df3.drop(['index'], axis=1)

#change
df_2017_power = df3.copy()
df_2017_power.to_csv("..\\Data\\Power\\fixed\\df_2017.csv")
