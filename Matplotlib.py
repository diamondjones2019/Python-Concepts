#!/usr/bin/env python
# coding: utf-8

# In[87]:


pwd


# In[88]:


clothing = pd.read_csv('C:\\Users\\Diamond\\Documents\\Jupyter Files\\Clothing-Review.csv')


# In[89]:


print(clothing)


# In[101]:


import matplotlib.pyplot as plt
import pandas as pd


# In[103]:


clothing.describe()


# In[121]:


clothing.tail()


# In[122]:


clothing.head()


# In[104]:


plt.hist(clothing.Age)
plt.title('What Age Shops More Online?')
plt.xlabel('Age')
plt.ylabel('Number of Shoppers')
plt.show()


# In[105]:


plt.hist(clothing.Rating, color='orange')
plt.show()


# In[114]:


plt.plot(clothing.PositiveFeedbackCount, color='green')
plt.title('How many customers left a positive feedback?')
plt.xlabel('Number of Customers')
plt.ylabel('Feedback')
plt.show()


# In[ ]:




