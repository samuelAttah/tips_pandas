#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


pip install seaborn


# In[3]:


import pandas as pd
import seaborn as sns


# In[5]:


cool = pd.read_csv(r'C:\Users\attah\Documents\Pandasxxx\archive\national-history.csv')


# In[6]:


cool.head()


# In[7]:


tips = sns.load_dataset('tips')


# In[8]:


tips.head()


# In[9]:


tips.day.unique()


# In[10]:


tips.time.unique()


# In[15]:


tips.time.value_counts()


# In[16]:


death = cool.death
positive = cool.positive


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


plt.hist(death,positive, bins=3)


# In[20]:


help(plt.hist)


# In[21]:


plt.hist(death)


# In[23]:


plt.scatter(positive,death)


# In[24]:


tips.time.value_counts().plot(kind='bar')


# In[25]:


tips.time.value_counts(normalize=True)


# In[26]:


cool.states.unique()


# In[27]:


cool.tail()


# In[28]:


cool.states.value_counts(normalize=True)


# In[29]:


cool.states.value_counts().plot(kind='bar')


# In[30]:


tips.groupby(['time'])['tip'].mean()


# In[31]:


tips.groupby(['time'])['tip'].mean().plot(kind='bar')


# In[32]:


tips.smoker.unique()


# In[33]:


tips.smoker.value_counts()


# In[34]:


tips.groupby(['smoker'])['tip'].mean()


# In[35]:


tips.groupby(['smoker'])['tip'].mean().plot(kind='bar')


# In[37]:


tips.groupby(['sex'])['tip'].mean().plot(kind='bar')


# In[38]:


tips.day.value_counts()


# In[39]:


tips.day.unique()


# In[41]:


tips.groupby(['day'])['tip'].mean().plot(kind='bar')


# In[43]:


tips.groupby(['smoker', 'sex'])['tip'].mean()


# In[44]:


tips.groupby(['smoker', 'sex'])['tip'].mean().unstack


# In[45]:


tips.groupby(['smoker', 'sex'])['tip'].mean().unstack()


# In[46]:


tips['tips_pct']= (tips.tip/tips.total_bill)*100


# In[47]:


tips.head()


# In[48]:


tips.tips_pct.unique()


# In[51]:


tips.tips_pct.value_counts()


# In[52]:


tips.groupby(['smoker', 'sex'])['tip'].mean()


# In[54]:


tips.groupby(['smoker', 'sex'])['tips_pct'].mean().plot(kind='bar')


# In[55]:


tips.groupby(['smoker', 'sex'])['tips_pct'].mean().unstack()


# In[56]:


tips.plot.scatter(x='total_bill', y='tip')


# In[59]:


tips.plot.hist(bins = 5)


# In[63]:


import numpy as np
real_total = np.array(tips.total_bill)


# In[64]:


plt.hist(real_total, bins = 5)


# In[65]:


sns.scatterplot(x='total_bill', y='tip', data = tips)


# In[66]:


sns.scatterplot(x='total_bill', y='tip', data= tips, hue='sex')


# In[67]:


sns.scatterplot(x='total_bill', y='tip', data=tips, hue='time')


# In[68]:


sns.relplot(x='total_bill', y='tip', data=tips, col='sex', hue='time')


# In[69]:


help(sns.displot)


# In[71]:


sns.displot(x='total_bill', data=tips, col='time', kde=True)


# #the distribution set above shows the relationship between time and the total bills paid 
# 

# In[72]:


sns.pairplot(data=tips, hue='sex')


# In[ ]:




