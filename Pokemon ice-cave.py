# Libraries
import numpy as np
import matplotlib.pyplot as plt
import ice_cave_library as ice
from random import *

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher
#import pygame as pg


######################################################################
########################### Set-ups ##################################


width = 6
length = 6

startpoint = np.array([[0, 2], [0, 3]]) # same as (1, 3), (1, 4)
endpoint = np.array([[3, 7], [4, 7]]) # same as (4, 8), (5, 8)

initial_rocks = np.array([[4, 5]]) # same as (5, 6)
odds_of_rocks = 0.1 # 10% odds of rocks
num_joints = 5

#######################################################################
#######################################################################


## randomly set startpoint
startpoint_save = startpoint
startpoint = startpoint[randint(1, startpoint.shape[0]) - 1]

## check if the start / end move is vertical / horizontal
if startpoint[0] == 0 or startpoint[0] == width + 1:
    vertical_s = 1
    horizontal_s = 0    
else:
    vertical_s = 0
    horizontal_s = 1
    
if endpoint[0][0] == 0 or endpoint[0][0] == length + 1:
    vertical_e = 1
    horizontal_e = 0    
else:
    vertical_e = 0
    horizontal_e = 1


#######################################################################
#######################################################################
### restart point ###

problemo = 1 
while problemo == 1:

    problemo = 0
    maps = None
    path = None
    num_path = None
    rocks = None
    num_rocks = None

    # Plot setups
    maps = np.zeros((length + 2, width + 2))

    ## set rocks
    maps[:, 0] = 1
    maps[:, width + 1] = 1
    maps[length + 1, :] = 1
    maps[0, :] = 1

    ## set initial setups
    keep = 1

    row = startpoint[0]
    column = startpoint[1]

    horizontal = horizontal_s
    vertical = vertical_s

    now = startpoint

    ### path set
    path = np.zeros([(length + 2) * (width + 2), 2])
    num_path = 0

    ### rock set
    rocks = np.zeros([(length + 2) * (width + 2), 2])
    num_rocks = 0
    for i in range(0, initial_rocks.shape[0]):
        maps[initial_rocks[i]] = 1
        rocks[i] = initial_rocks[i]
        num_rocks = num_rocks + 1

    #######################################################################
    #######################################################################

    joints = 0
    # maps[startpoint[0], startpoint] = 0.001

    while keep == 1:
        
        #find stuckpoint
        if keep == 1:
            maps = ice.imstuck(maps)

        #update now_latest
        if keep == 1:
            now_latest = now
        
        #decide next tile
        if keep == 1:
            now, maps, horizontal, rock_now, problemo = ice.nextile(now, maps, horizontal)
            keep = ice.errorcheck(now, now_latest)
        
        #update maps, path, rocks
        if keep == 1:
            maps, path, rocks, num_path, num_rocks = ice.writemap(maps, now, path, rocks, rock_now, num_path, num_rocks, horizontal, now_latest)
            keep = ice.errorcheck(now, now_latest)

        #swap
        if keep == 1:
            horizontal, vertical = vertical, horizontal
            keep = ice.errorcheck(now, now_latest)
        
        if joints > num_joints:
            #check if the path can end
            keep, maps, path, num_path = ice.endcheck(keep, maps, path, num_path, now, endpoint, horizontal, horizontal_e)
        
        joints = joints + 1

        

        print(joints)

        if joints > width * length:
            keep = 0

        # if joints <= num_joints and keep == 0:
        #     problemo = 1
        #     print('problemo')

#######################################################################
#######################################################################
# redraw maps

maps = ice.imnotstuck(maps)

rocks = rocks[0 : num_rocks, :]
path = path[0 : num_path, :]

path, num_path = ice.redraw(path, num_path)

## set startpoint as 2, endpoint as 3

for i in range(0, initial_rocks.shape[0]):
    maps[initial_rocks[i][0], initial_rocks[i][1]] = 1
    
for i in range(0, startpoint.shape[0]):
    maps[startpoint_save[i][0], startpoint_save[i][1]] = 2
    
for i in range(0, endpoint.shape[0]):
    maps[endpoint[i][0], endpoint[i][1]] = 3
    
#######################################################################
#######################################################################
# plot


# print(num_path)
# print(path)
# print(rocks)
# print(now)

 
# with np.printoptions(precision=3, suppress=True):
#     print(maps)
# # column to x axis, reversed row to y axis
# plt.plot(path[:, 1], (-1) * path[:, 0], 'ro-')
# # plt.plot(startpoint_save, 'r*')
# # plt.plot(endpoint, 'r*')
# plt.axis([0, width + 1, -(length + 1), 0])

# plt.plot(rocks[:, 1], (-1) * rocks[:, 0], 'bo')
# plt.show()