#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\Rishiraj Saha\Downloads\1. Weather Data.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.shape


# In[7]:


data.index


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data['Weather'].unique()


# In[11]:


data.nunique()


# In[12]:


data.count()


# In[13]:


data['Weather'].value_counts()


# In[14]:


data.info()


# In[15]:


data.head(2)


# In[16]:


data.nunique()


# In[17]:


data["Wind Speed_km/h"].nunique()


# In[18]:


data["Wind Speed_km/h"].unique()


# In[19]:


data.Weather.value_counts()


# In[20]:


data.groupby


# In[21]:


data[data["Wind Speed_km/h"] == 4]


# In[22]:


data.isnull().sum()


# In[23]:


data.notnull().sum()


# In[24]:


data.head(2)


# In[25]:


data.rename(columns = {'Weather' : 'Weather Condition'})


# In[26]:


data.Visibility_km.mean()


# In[27]:


data.Press_kPa.std()


# In[28]:


data["Rel Hum_%"].var()


# In[29]:


data.head(2)


# In[30]:


data['Weather'].value_counts()


# In[31]:


data[data['Weather']=='Snow']


# In[32]:


data[data['Weather'].str.contains('Snow')].tail(50)


# In[33]:


data[(data['Visibility_km']==25)&(data['Wind Speed_km/h'] > 24)]


# In[38]:


data[(data['Weather'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[39]:


data[(data['Weather'] == 'Clear')&(data['Rel Hum_%'] > 50)|(data['Visibility_km']>40)]


# In[ ]:





# In[ ]:




