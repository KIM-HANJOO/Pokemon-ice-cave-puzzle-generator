import numpy as np
import matplotlib.pyplot as plt
import practice_library as ice
from random import *

##
top = 1 
bottom = 2
left = 3
right = 4
##

width = 6
length = 5

startpoint = [2, 3] 
startpoint_place = top

endpoint = [3]
endpoint_place = right

##

startpoint_maps = np.zeros((len(startpoint) , 2))
endpoint_maps = np.zeros((len(endpoint), 2))

# set startpoint
if startpoint_place == top:
    startpoint_maps[:, 0] = 0
    startpoint_maps[:, 1] = np.transpose(startpoint)
    
elif startpoint_place == bottom:
    startpoint_maps[:, 0] = length + 1
    startpoint_maps[:, 1] = np.transpose(startpoint)
    
elif startpoint_place == left:
    startpoint_maps[:, 0] = np.transpose(startpoint)
    startpoint_maps[:, 1] = 0
    
elif startpoint_place == right:
    startpoint_maps[:, 0] = np.transpose(startpoint)
    startpoint_maps[:, 1] = width + 1
    
#set endpoint

if endpoint_place == top:
    endpoint_maps[:, 0] = 0
    endpoint_maps[:, 1] = np.transpose(endpoint)
    
elif endpoint_place == bottom:
    endpoint_maps[:, 0] = length + 1
    endpoint_maps[:, 1] = np.transpose(endpoint)
    
elif startpoint_place == left:
    endpoint_maps[:, 0] = np.transpose(endpoint)
    endpoint_maps[:, 1] = 0
    
elif endpoint_place == right:
    endpoint_maps[:, 0] = np.transpose(endpoint)
    endpoint_maps[:, 1] = width + 1
    
    
#
startrand = randint(1, np.shape(startpoint)[0]) - 1
startpoint = startpoint_maps[startrand, :]
startpoint = startpoint.astype(int)
#

maps = np.zeros((length + 2, width + 2))
maps[0, :] = 1
maps[length + 1, :] = 1
maps[:, 0] = 1
maps[:, width + 1] = 1

maps[startpoint[0], startpoint[1]] = 2





