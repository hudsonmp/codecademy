#!/usr/bin/env python
# coding: utf-8

# In[56]:


paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]


# In[59]:


dates = [1939, 1933, 1946, 1940]


# In[62]:


paintings = list(zip(paintings, dates))
print(paintings)


# In[65]:


new_paintings = [('The Broken Column', 1944), ('The Wounded Deer', 1946), ('Me and My Doll', 1937)]
paintings.extend(new_paintings)
print(paintings)


# In[70]:


len(paintings)


# In[75]:


audio_tour_number = range(1, 8)
print(list(audio_tour_number))


# In[83]:


master_list = list(zip(paintings, audio_tour_number))
print(master_list)


# In[85]:


print(master_list)

