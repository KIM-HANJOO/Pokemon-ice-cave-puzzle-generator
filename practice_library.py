import numpy as np
from random import *
from numpy.core.getlimits import _MACHAR_PARAMS
from numpy.core.numerictypes import maximum_sctype

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher

######################################################################################

def initinfo(startpoint, startpoint_place, endpoint, endpoint_place, width, length):
    top = 1
    bottom = 2
    left = 3
    right = 4

    startpoint_maps = np.zeros((len(startpoint) , 2))
    endpoint_maps = np.zeros((len(endpoint), 2))

    # set startpoint
    if startpoint_place == top:
        startpoint_maps[:, 0] = 0
        startpoint_maps[:, 1] = np.transpose(startpoint)
        horizontal_s = 0
        
    elif startpoint_place == bottom:
        startpoint_maps[:, 0] = length + 1
        startpoint_maps[:, 1] = np.transpose(startpoint)
        horizontal_s = 0

    elif startpoint_place == left:
        startpoint_maps[:, 0] = np.transpose(startpoint)
        startpoint_maps[:, 1] = 0
        horizontal_s = 1

    elif startpoint_place == right:
        startpoint_maps[:, 0] = np.transpose(startpoint)
        startpoint_maps[:, 1] = width + 1
        horizontal_s = 1

    #set endpoint

    if endpoint_place == top:
        endpoint_maps[:, 0] = 0
        endpoint_maps[:, 1] = np.transpose(endpoint)
        horizontal_e = 0
        
    elif endpoint_place == bottom:
        endpoint_maps[:, 0] = length + 1
        endpoint_maps[:, 1] = np.transpose(endpoint)
        horizontal_e = 0

    elif startpoint_place == left:
        endpoint_maps[:, 0] = np.transpose(endpoint)
        endpoint_maps[:, 1] = 0
        horizontal_e = 1

    elif endpoint_place == right:
        endpoint_maps[:, 0] = np.transpose(endpoint)
        endpoint_maps[:, 1] = width + 1
        horizontal_e = 1
    
    horizontal_all = np.zeros(2)
    horizontal_all[0] = horizontal_s
    horizontal_all[1] = horizontal_e
    
    startrand = randint(1, np.shape(startpoint)[0]) - 1
    startpoint = startpoint_maps[startrand, :]
    startpoint = startpoint.astype(int)
    startpoint_maps = startpoint_maps.astype(int)
    endpoint_maps = endpoint_maps.astype(int)
    

    return startpoint, startpoint_maps, endpoint_maps, horizontal_all

######################################################################################

def nextile(now, maps, horizontal):
    
    #load line
    if horizontal == 1:
        line = maps[now[0], :].copy()
        line_save = line.copy()
        now_line = now[1]
        
    elif horizontal == 0:
        line = np.transpose(maps[:, now[1]].copy())
        line_save = line.copy()
        now_line = now[0]
    

    #adjust line array
    for i in range(0, line.shape[0]):
        if i < now_line:
            line[i] = line[i] * -1
        elif i == now_line:
            line[i] = 0
        # if i > now_line:
        # line [i] = line[i] * 1
    

    # forcely add rocks to the left / right end
    line[0] = -1
    line[line.shape[0] -1] = 1

    #last nega/posi num
    for i in range(0, line.shape[0]):
        if line[i] < 0:
            leftend = i

    for i in range(line.shape[0] - 1, -1, -1):
        if line[i] > 0:
            rightend = i


    # #randomly decide next tile
    re_next = 1
    while re_next == 1:
        next_tile = randint(leftend + 1, rightend - 1)
        if next_tile == now_line:
            re_next = 1

        # if there is no problem, keep on
        elif next_tile != now_line:
            re_next = 0
    

    # #place the rock
    if next_tile < now_line:
        num_next_rock = next_tile - 1
    elif next_tile > now_line:
        num_next_rock = next_tile + 1


    # renew now
    next_rock = np.zeros(2)
    next_rock = next_rock.astype(int)

    if horizontal == 1:
        now[1] = next_tile
        next_rock[0] = now[0]
        next_rock[1] = num_next_rock

    elif horizontal == 0:
        now[0] = next_tile
        next_rock[0] = num_next_rock
        next_rock[1] = now[1]

    #add rocks to maps
    next_rock = next_rock.astype(int)
    maps[next_rock[0], next_rock[1]] = 1


    return now, maps, horizontal

######################################################################################

def imstuck(now, maps, horizontal):
    stuck = 0
    
    if horizontal == 1:
        if maps[now[0] + 1, now[1]] != 0:
            if maps[now[0] - 1, now[1]] != 0:
                stuck = 1
    elif horizontal == 0:
        if maps[now[0], now[1] + 1] != 0:
            if maps[now[0], now[1] - 1] != 0:
                stuck = 1
    
    return stuck

######################################################################################

def endcheck(now, maps, endpoint_place, horizontal, horizontal_e, width, length):
    end = 1
    if horizontal == 1:
        # top = 1, bottom = 2, left = 3, right = 4
        if endpoint_place == 1 or 2:
            end_line = np.array([1])
        elif endpoint_place == 3:
            end_line = maps[now[0], 1 : now[1]].copy()
        elif endpoint_place == 4:
            end_line = maps[now[0], now[1] : width + 1].copy()
    
    if horizontal == 0:
        # top = 1, bottom = 2, left = 3, right = 4
        if endpoint_place == 3 or 4:
            end_line = np.array([1])
        elif endpoint_place == 1:
            end_line = maps[1 : now[0], now[1]].copy()
        elif endpoint_place == 2:
            end_line = maps[now[0] : length + 1, now[1]].copy()
    print("end_line", end_line)
    for i in range(0, end_line.shape[0]):
        if end_line[i] != 0:
            end = 0


    return end



    
    
    