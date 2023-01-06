#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[24]:


pwd


# In[25]:


import os
cwd = os.getcwd()
#print the current working directory
print("Current working directory: {0}".format(cwd))
os.chdir("/Users/supriyanallan/Desktop")
print("Current working directory: {0}".format(cwd))


# In[29]:


cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))
os.chdir("/Users/supriyanallan/Desktop/Projects")
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))


# In[30]:


pwd()


# In[37]:


df = pd.read_csv("NetflixViewingHistory.csv")


# In[38]:


df


# In[62]:


list = []
for i in df.Title:
#     print(i.split(':')[0])
    list.append(i.split(':')[0])
df['show_title'] = list
    


# In[60]:


my_titles = list
df.head()


# In[148]:


top_views = pd.Series(my_titles).value_counts().nlargest(10)
print(top_views)


# In[64]:


import matplotlib.pyplot as plt
import numpy as np
N = len(top_views)
x = np.arange(N)
colors = plt.get_cmap('viridis')
plt.figure(figsize=(10,5))
plt.bar(top_views.index, top_views.values, color=colors(x/N))
plt.ylabel("Freq", fontsize=12)
plt.xlabel("Show titles", fontsize=12)
plt.xticks(rotation=30, ha= "right", fontsize=11)
plt.title("My Top 10 Shows on Netflix based on My Viewing Activity", fontsize=16)
plt.savefig("top 10 shows bar.png", dpi=300, bbox_inches='tight')
plt.show()


# In[65]:


from datetime import datetime
df['date'] = pd.to_datetime(df['Date'])
df


# In[152]:


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


# In[153]:


df['Weekday'] = df['Date'].dt.strftime("%A")
df


# In[154]:


cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df.day = pd.Categorical(df['Weekday'], categories=cats, ordered=True)
by_day = df.sort_values('Weekday')['Weekday'].value_counts().sort_index()


# In[155]:


import matplotlib.pyplot as plt


# In[156]:


N = len(by_day)
print(by_day)


# In[157]:


plt.style.use('seaborn-darkgrid')

N = len(by_day)
x = np.arange(N)
colors = plt.get_cmap('winter').reversed()
plt.figure(figsize=(10,5))
plt.bar(by_day.index, by_day.values, color=colors(x/N), snap=False)
plt.title("My Netflix Viewing Activity Pattern by Day", fontsize=20)
plt.xlabel("Day Of The Week", fontsize=15)
plt.ylabel("Frequency", fontsize=15)

plt.savefig("Freq by day.png", dpi=300, bbox_inches='tight')
plt.show()


# In[158]:


by_date = pd.Series(df['date']).value_counts().sort_index()
by_date.index = pd.DatetimeIndex(by_date.index)


# In[159]:


df_date = by_date.rename_axis('date').reset_index(name='counts')
df_date


# In[160]:


idx = pd.date_range(min(by_date.index), max(by_date.index))
s = by_date.reindex(idx, fill_value=0)
print(s)


# In[161]:


plt.figure(figsize=(15,5))
plt.bar(s.index, s.values)
plt.title("My Netflix Viewing Activity Timeline", fontsize=20)
plt.xlabel("date", fontsize=15)
plt.ylabel("freq", fontsize=15)
plt.savefig("timeline.png", dpi=300, bbox_inches='tight')
plt.show()


# In[165]:


idx = pd.date_range(min(df['date']), max(df['date']))
print(top_views)


# In[170]:


plt.style.use('seaborn-darkgrid')
idx = pd.date_range(min(df['date']), max(df['date']))
plt.figure(figsize=(15,12))
palette = plt.get_cmap('tab10')
num = 0
for title in top_views.index:
    num += 1
    plt.subplot(6,2, num)
    plt.ylim(-1.0, 15)
    show = df[df['show_title']==title]
    showly = show['date'].value_counts().sort_index()
    s = showly.reindex(idx, fill_value=0)
    plt.plot(s.index, s.values, marker='', color=palette(num%8), linewidth=2.5, alpha=0.9, label=title)
    plt.title(title, loc='left', fontsize=12, fontweight=0)
plt.suptitle("My top 10 viewing activity on Netflix", fontsize=20, fontweight=0, color='black', y=1.05)
plt.tight_layout()
plt.savefig("viewing activity.png", dpi=300, bbox_inches='tight')
plt.show()
