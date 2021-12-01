#!/usr/bin/env python
# coding: utf-8

# ## Scrape the Houston NPR website
# 
# https://www.houstonpublicmedia.org/
# 
# I want a CSV file called `npr.csv` that includes a row for each story in the top section, with these columns:
# 
# * `section`, the section of the story (e.g. "Transportation", "Harris County")
# * `title`, the title of the story
# * `url`, the full URL to the story
# 
# If you want to start by printing these out, that's fine, but the end result is hopefully a CSV. If you'd like to filter out the rows without a title before saving that would be nice.

# In[22]:


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.houstonpublicmedia.org/")
doc = BeautifulSoup(response.text)


# In[23]:


len(doc.find_all('article'))


# In[24]:


len(doc.find_all(class_='post'))


# In[25]:


for story in doc.find_all('article'):
    print(story.text.strip())


# In[26]:


stories = doc.find_all(class_='post')


# In[27]:


stories = doc.select('.post')


# In[28]:


dataset = []
for story in stories:
    data = {}
    data['section'] = story.find('h3').text
    data['title'] = story.find('h2').text
    data['url'] = story.find('a')['href']
    dataset.append(data)
dataset


# In[29]:


import pandas as pd

df = pd.DataFrame(dataset)
df.head()


# In[30]:


df.to_csv("npr.csv", index=False)


# In[ ]:





# In[ ]:




