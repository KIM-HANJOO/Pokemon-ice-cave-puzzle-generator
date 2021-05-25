# Libraries
import numpy as np
import matplotlib.pyplot as plt
import random
# import pygame as pg

##################################################
# Set-ups

width = 6
length = 6

startpoint = np.array([[0, 2], [0, 3]]) # same as (1, 3), (1, 4)
endpoint = np.array([[3, 7], [4, 7]]) # same as (4, 8), (5, 8)

initial_rocks = np.array([[4, 5]]) # same as (5, 6)
odds_of_rocks = 0.1 # 10% odds of rocks

##################################################

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

## randomly set startpoint
startpoint = startpoint[randint(1, startpoint.shape[0]) - 1]

## check if the start / end move is vertical / horizontal
if startpoint[0] == 0:
    vertical_s = 1
    horizontal_s = 0
    
elif startpoint[0] == width + 1:
    vertical_s = 1
    horizontal_s = 0
    
else:
    vertical_s = 0
    horizontal_s = 1
    
if endpoint[0][0] == 0:
    vertical_e = 1
    horizontal_e = 0
    
elif endpoint[0][0] == length + 1:
    vertical_e = 1
    horizontal_e = 0
    
else:
    vertical_e = 0
    horizontal_e = 1

print(horizontal_s)
print(horizontal_e)

## set path array, rocks array, etc.

keep = 1

row = startpoint[0][0]
column = startpoint[0][1]

path = np.zeros([2, 2])
path[0] = startpoint
num_path = 2

rocks = np.zeros([2, 2])
num_rocks = 1


# ice-cave puzzle library


# Main code
