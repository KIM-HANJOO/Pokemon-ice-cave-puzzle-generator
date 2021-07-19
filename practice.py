import numpy as np
import matplotlib.pyplot as plt
import practice_library as ice
from random import *

################################################################
####################### < input > ##############################
width = 6
length = 5

# top = 1, bottom = 2, left = 3, right = 4

startpoint = [2, 3] 
startpoint_place = 1

endpoint = [3]
endpoint_place = 4

################################################################
################################################################

#initial info
startpoint, startpoint_maps, endpoint_maps, horizontal_all = ice.initinfo(startpoint, startpoint_place, endpoint, endpoint_place, width, length)

endpoint = endpoint_maps[0]

#initial horizontal
horizontal_s = horizontal_all[0]
horizontal_e = horizontal_all[1]


#initial maps
maps = np.zeros((length + 2, width + 2))
maps[0, :] = 1
maps[length + 1, :] = 1
maps[:, 0] = 1
maps[:, width + 1] = 1

maps = maps.astype(int)

for i in range(0, startpoint_maps.shape[0]):
    maps[startpoint_maps[i][0], startpoint_maps[i - 1][1]] = 2

for i in range(0, endpoint_maps.shape[0]):
    maps[endpoint_maps[i][0], endpoint_maps[i - 1][1]] = 2

maps[startpoint[0], startpoint[1]] = 3


## start
now = startpoint.copy()
horizontal = horizontal_s

keep = 1
joint = 0
mapplot_save_list = []
mapplot_save_list.append(list(startpoint))
rock_save_list = []
while keep == 1:

    #save now
    now_latest = now.copy()
    maps_latest = maps.copy()

    #next tile
    stuck = 1
    while stuck == 1:
        # not stuck yet
        stuck = 0
        
        #next tile
        now, maps, horizontal = ice.nextile(now, maps, horizontal)

        # see if stuck
        stuck = ice.imstuck(now, maps, horizontal)
        if stuck == 1:
            now = now_latest.copy()
            maps = maps_latest.copy()
    
    #draw maps
    mapplot_save_list = ice.mapplot_save(now, mapplot_save_list)

    # swap horizontal
    if horizontal == 0:
        horizontal = 1
    else: #horizontal = 1
        horizontal = 0

    #joint
    joint = joint + 1

    #endcheck
    if joint > 5:
        end = ice.endcheck(now, maps, endpoint, horizontal)
        if end == 1:
            keep = 0

    
mapplot_save_list.append(list(endpoint))
print("maps", maps)
ice.mapplot(width, length, maps, rock_save_list, mapplot_save_list)
