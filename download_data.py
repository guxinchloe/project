#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import csv


# In[10]:


url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
response = pd.read_html(url)[0]

response.to_csv(r'rawdata.csv', mode='a',encoding='UTF-8',header=1,index=0)


# In[11]:


df = pd.read_csv(r'rawdata.csv')


# In[12]:


df.head()


# In[19]:


df = df[df['Borough'] != "Not assigned"]
df.reset_index(drop=True, inplace=True)


# In[20]:


df.head()


# In[ ]:




