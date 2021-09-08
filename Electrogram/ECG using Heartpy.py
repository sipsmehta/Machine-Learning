#!/usr/bin/env python
# coding: utf-8

# In[21]:


import heartpy as hp
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


#first let's load the clean PPG signal
data, timer = hp.load_exampledata(0)

#and visualise
plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()


# In[23]:


#run the analysis
wd, m = hp.process(data, sample_rate = 100.0)
#wd stands for working data and m stands for measure


# In[24]:


#set large figure
plt.figure(figsize=(12,4))

#call plotter
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))


# In[11]:


data, timer = hp.load_exampledata(1)

plt.figure(figsize=(12,4))
plt.plot(data)
plt.show()


# In[12]:


sample_rate = hp.get_samplerate_mstimer(timer)

wd, m = hp.process(data, sample_rate)

#plot
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))


# In[13]:


data, timer = hp.load_exampledata(2)

print(timer[0])


# In[14]:


sample_rate = hp.get_samplerate_datetime(timer, timeformat='%Y-%m-%d %H:%M:%S.%f')

print('sample rate is: %f Hz' %sample_rate)


# In[15]:



wd, m = hp.process(data, sample_rate, report_time = True)

#plot
plt.figure(figsize=(12,4))
hp.plotter(wd, m)

#let's zoom in on a bit
plt.figure(figsize=(12,4))
plt.xlim(20000, 30000)
hp.plotter(wd, m)

#display measures computed
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))


# In[ ]:




