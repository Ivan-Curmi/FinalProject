#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("Online-Retail.csv")
df.head()


# In[3]:


df.shape


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[14]:


df_missing_value = df.dropna()


# In[15]:


df_missing_value


# In[30]:


df_filter = df[df['Quantity'] < 0]
df_filter


# In[26]:


df_filter1 = df[df['UnitPrice'] < 0]
df_filter1


# In[23]:


df_filter2 = df[df[['Quantity','UnitPrice',]] < 0]
df_filter2


# In[24]:


df.shape


# In[ ]:




