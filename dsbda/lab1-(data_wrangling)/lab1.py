#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


df=pd.read_csv("data.csv")


# In[5]:


df


# In[7]:


df.shape 
#gives rows and columns


# In[30]:


df.describe()
#use df.min() , df.max() , etc to find individual statistics


# In[9]:


df.dtypes


# In[11]:


df.groupby(by=['Age']).size() 
#gives all ages and how many values of that age


# In[12]:


df.isnull()
#check for null vals here no null values present


# In[16]:


print(type("Age")) 
print(type("BMI"))


# In[18]:


df.Age.astype(float)
#change data type of age to float


# In[19]:


df.sort_values('Age')


# In[20]:


df.sort_values('Age' , ascending = False )


# In[22]:


df.rename(columns = {'Age':'Year old'})
df.rename(columns = {'Year old':'Age'})


# In[24]:


df.sort_index()


# In[25]:


df.reset_index()


# In[26]:


df.drop_duplicates()
#no duplicate vals


# In[27]:


pd.melt(df)
#key val pairs


# In[28]:


df.head()
#gives first 5 entries df.tail() gives last 5


# In[33]:


pd.get_dummies(df)
#used to convert categorical variables into dummy or indicator variables.
pd.get_dummies(df['Age'])


# In[ ]:




