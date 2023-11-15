#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


data=pd.read_csv("C:\\BARATHRAJ\\DATASET\\globalterrorismdb_0718dist.csv",encoding='latin1')
data


# In[6]:


data.shape


# In[7]:


data.info()


# In[9]:


col=data.columns
for i in col:
    print(i)


# In[10]:


data_clean=data[['iyear','imonth','iday','country_txt','region_txt','provstate','city','attacktype1_txt','targtype1_txt','targsubtype1_txt','gname','weaptype1_txt']]
data_clean


# In[11]:


data_clean.columns


# In[13]:


data_clean.isnull().sum()


# In[14]:


data_clean['provstate']=data_clean['provstate'].fillna('other')
data_clean['city']=data_clean['city'].fillna('Unknown')
data_clean['targsubtype1_txt']=data_clean['targsubtype1_txt'].fillna('Unknown')
data_clean


# In[15]:


data_clean.isnull().sum()


# In[18]:


data_clean=data_clean.rename(columns={'iyear':'year','imonth':'month','iday':'day','country_txt':'country','region_txt':'region','provstate':'state','attacktype1_txt':'attack','targtype1_txt':
                                      'target','targsubtype1_txt':'targetsub','ganme':'gang_name','weaptype1_txt':'weapon'})
data_clean.columns


# In[19]:


data_clean


# In[20]:


data_clean.info()


# In[21]:


data_clean.describe()


# In[22]:


data_clean.columns


# In[23]:


data_clean['year'].value_counts().head(10)


# In[24]:


data_clean['month'].value_counts().head(10)


# In[25]:


data_clean['day'].value_counts().head(10)


# In[26]:


data_clean['country'].value_counts().head(10)


# In[27]:


data_clean['state'].value_counts().head(10)


# In[28]:


data_clean['city'].value_counts().head(10)


# In[29]:


data_clean['region'].value_counts().head(10)


# In[30]:


data_clean['attack'].value_counts().head(10)


# In[31]:


data_clean['target'].value_counts().head(10)


# In[32]:


data_clean['targetsub'].value_counts().head(10)


# In[38]:


data_clean['gname'].value_counts().head(10)


# In[37]:


data_clean['weapon'].value_co


# # Visualizations

# In[43]:


plt.figure(figsize=(20,5))
plt.xticks(rotation = 90)
plt.title('weapon details')
sns.countplot(x=data_clean['weapon'],color='red')


# In[46]:


plt.figure(figsize=(20,5))
plt.title('target details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['target'],color='red')


# In[47]:


plt.figure(figsize=(20,5))
plt.title('attack details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['attack'],color='red')


# In[51]:


plt.figure(figsize=(20,5))
plt.title('region details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['region'],color='red')


# In[61]:


plt.figure(figsize=(20,5))
plt.title('city details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['city'],color='red')


# In[59]:


plt.figure(figsize=(20,5))
plt.title('state details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['state'],color='red')


# In[58]:


plt.figure(figsize=(50,10))
plt.title('country details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['country'],color='red')


# In[53]:


plt.figure(figsize=(20,5))
plt.title('day details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['day'],color='red')


# In[54]:


plt.figure(figsize=(20,5))
plt.title('month details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['month'],color='red')


# In[55]:


plt.figure(figsize=(20,5))
plt.title('year details')
plt.xticks(rotation=90)
sns.countplot(x=data_clean['year'],color='red')


# # CONCLUSION

# # Results of Analysis
# 1)Most of the attacks were attacked through explosives and then through firearms.
# 
# 2)Attacks were more during 2014 and then in 2015. When compared to attacks from 1970 onwards, the last 6 years scored a maximum
#   But from 2014 onwards count started decreasing.
#     
# 3)Almost Every day has the same contribution but attacks were low during 31st and high during 15th and 1st.
# 
# 4)Iraq dominates all the countries and it has the highest number of attacks and then Pakistan, Afghanistan, and India follow it.
# 
# 5)The Middle East& North Africa leads 1st among all the regions and then South Asia takes 2nd place.
# 
# 6)For most of the attacks, the target is Private Citizens& property and the next Military leads.
# 
# 7)Most of the attacks were through either Bombing or Explosion.

# In[ ]:




