#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries
import numpy as np
import matplotlib.pyplot as plt
# import pygame as pg


# In[84]:


##################################################
# Set-ups

width = 6
length = 6

startpoint = np.array([[0, 2], [0, 3]])
endpoint = np.array([[3, 7], [4, 7]])

initial_rocks = np.array([[0, 0]])
odds_of_rocks = 0.1

##################################################


# In[85]:


# Plot setups
map = np.zeros((length + 2, width + 2))

## set rocks
map[:, 0] = 1
map[:, width + 1] = 1
map[length + 1, :] = 1
map[0, :] = 1

for i in range(0, initial_rocks.shape[0]):
    map[initial_rocks[i][0], initial_rocks[i][1]] = 1
    
for i in range(0, startpoint.shape[0]):
    map[startpoint[i][0], startpoint[i][1]] = 2
    
for i in range(0, endpoint.shape[0]):
    map[endpoint[i][0], endpoint[i][1]] = 3

print(map)

## set startpoint, endpoint


# In[38]:


# Defining functions


# In[39]:


# Main code

