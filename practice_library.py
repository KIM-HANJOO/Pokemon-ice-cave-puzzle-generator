import numpy as np
from random import *
from numpy.core.getlimits import _MACHAR_PARAMS
from numpy.core.numerictypes import maximum_sctype

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher

import matplotlib.pyplot as plt
from PIL import Image
import os
######################################################################################

def initinfo(startpoint, startpoint_place, endpoint, endpoint_place, width, length):
    top = 1
    bottom = 2
    left = 3
    right = 4

    startpoint_maps = np.zeros((len(startpoint), 2))
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

def nextile_2(now, maps, horizontal):
    


    return now, maps, horizontal

######################################################################################

def addpath(now, now_latest, maps, path):
    now_row = now[0]
    now_col = now[1]
    last_row = now_latest[0]
    last_col = now_latest[1]
    
    if now_row == last_row : 
        for i in range(min(now_col, last_col), max(now_col, last_col)) :
            path.append([now_row, i])
    elif now_col == last_col :
        for i in range(min(now_row, last_row), max(now_row, last_row)) :
            path.append([i, now_col])
    
    path = np.array(path)

    for i in range(len(path)) :
        maps[path[i, :]] = 0.1


    return path, maps

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

def endcheck(now, maps, endpoint, horizontal):
    length = maps[0] - 2
    width = maps[1] - 2
    # row_now = now[0].copy()
    # row_endpoint = endpoint[0].copy()
    # end_ch = now - endpoint
    now_row  = now[0]
    now_col = now[1]
    end_row = endpoint[0]
    end_col = endpoint[1]
    if (now_row == end_row) :
        end_pot = 1 # same row
    
    elif (now_col == end_col) :
    # if (min(end_ch[0][0]) == 0) | (min(end_ch[0][1]) == 0):
        # there is the potential that the loop might end
        end_pot = 2 # same col
    else :
        end_pot = 0

    end = 0

    if end_pot == 1 :
        care = maps[now_row, min(now_col, end_col) : max(now_col, end_col)].copy()
        if care.sum() == 0 :
            end = 1
        else : 
            end = 0
    if end_pot == 2 :
        care = maps[min(now_row, end_row) : max(now_row, end_row), now_col].copy()
        if care.sum() == 0 :
            end = 1
        else :
            end = 0

    # if there is potential to be end
    # make a line from now to endpoint (end_line)
    # left_end_line = 0
    # right_end_line = 1

    # if end_pot == 1:
    #     if now[0] - endpoint[0] == 0:
    #         if now[1] < endpoint[1]:
    #             left_end_line = now[1]
    #             right_end_line = endpoint[1]
                
    #         else :
    #             left_end_line = endpoint[1]
    #             right_end_line = now[1]
        
    #     if now[1] - endpoint[1] == 0:
    #         if now[0] < endpoint[0]:
    #             left_end_line = now[0]
    #             rigth_end_line = endpoint[0]

    #         else :
    #             left_end_line = endpoint[0]
    #             right_end_line = now[0]             

    # end_line = maps[now[0], left_end_line : right_end_line].copy()

    # # if end_line's cell have only 0 values,
    # # the loop will end
    
    # end = 0
    # if end_line.shape[0] == 2:
    #     end = 1
    # elif end_line.shape[0] > 2:
    #     temp = 0
    #     for i in range(1, end_line.shape[0]):
    #         if end_line[i] != 0:
    #             temp = 1

    #     if temp == 1:
    #         end = 1
    #     else :
    #         end = 0    
    return end


######################################################################################

def mapplot_save(now, mapplot_save_list) :
    mapplot_save_list.append(list(now))
    # mapplot_save_list = np.array(mapplot_save_list)
    # mapplot_save_list = np.append(mapplot_save_list, now, axis = 0)

    return mapplot_save_list

######################################################################################

def mapplot(width, length, maps, rock_save_list, mapplot_save_list) :
    mapplot_save_list = np.array(mapplot_save_list)

    for i in range(1, maps.shape[0] - 1) :
        for j in range(1, maps.shape[1] - 1) :
            if maps[i][j] == 1 :
                rock_save_list.append([i, j])
    rock_save_list = np.array(rock_save_list)

    plt.plot(mapplot_save_list[:, 1], (-1) * mapplot_save_list[: , 0], 'ro-')
    for i in range(len(rock_save_list)):
        plt.plot(rock_save_list[i, 1], (-1) * rock_save_list[i, 0], 'bo')

    # plt.axis(0, width + 1, -(length + 1), 0)
    plt.xlim(0, width + 1)
    plt.ylim(-(length + 1), 0)
    plt.show()

######################################################################################

def tilemap(maps, tiledir, savedir) :
    os.chdir(tiledir)
    
    ## Images
    #rock = Image.open('rock.png')
    bucket = Image.open('bage.png')
    bucket = bucket.resize((32, 32))
    #ice = Image.open('ice.png')
    base = Image.open('planc.png')
    base = base.resize((32, 32))
    door = Image.open('top_door.png')
    door = door.resize((32, 32))
    left_bottom_corner = Image.open('bottom_corner.png')
    right_bottom_corner = left_bottom_corner

    upper_wall = Image.open('top_wall.png')
    left_wall = Image.open('left_wall.png')
    right_wall = left_wall #left_wall.transpose(Image.FLIP_LEFT_RIGHT)
    telephone = Image.open('telephone.png')
    bottom_wall = Image.open('bottom_wall.png')

    ## resize
    left_bottom_corner = left_bottom_corner.resize((32, 32))
    right_bottom_corner = right_bottom_corner.resize((32, 32))
    upper_wall = upper_wall.resize((32, 32))
    left_wall = left_wall.resize((32, 32))
    right_wall = right_wall.resize((32, 32))
    bottom_wall = bottom_wall.resize((32, 32))
    telephone = telephone.resize((32, 32))

    step = 32 #rock.size[0]
    s = step
    ## Map Image
    mapng = Image.new('RGB', (step * maps.shape[1], step * maps.shape[0]))

    for i in range(maps.shape[1]) :
        for j in range(maps.shape[0]) :

            if i == 0 :
                if maps[j, i] == 1 :
                    maps[j, i] = 2222
            
            elif i == maps.shape[1] - 1 :
                if maps[j, i] == 1 :
                    maps[j, i] = 4444    

            if j == 0 : # upper
                if maps[j, i] == 1 :
                    maps[j, i] = 1111
                elif maps[j, i] == 2 :
                    maps[j, i] = 1111
            
            elif j == maps.shape[0] - 1 :
                if maps[j, i] == 1 :
                    maps[j, i] = 3333
                            
                    

            if maps[j, i] == 1111 :
                mapng.paste(upper_wall, (s * i, s * j))
            
            elif maps[j, i] == 2222 :
                mapng.paste(left_wall, (s * i, s * j))
                
            elif maps[j, i] == 3333 :
                mapng.paste(bottom_wall, (s * i, s * j))
            
            elif maps[j, i] == 4444 :
                mapng.paste(right_wall, (s * i, s * j))
            
            if maps[j, i] == 1 :
                mapng.paste(bucket, (s * (i), s * (j)))
            
            elif maps[j, i] == 0 :
                mapng.paste(base, (s * i, s * j))

            elif maps[j, i] == 2 :
                mapng.paste(base, (s * i, s * j))
            
            elif maps[j, i] == 3 :
                mapng.paste(door, (s * i, s * j))
            

    print('renewed maps', maps)                                 
    mapng.paste(left_bottom_corner, (s * 0, s * 6))
    mapng.paste(right_bottom_corner, (s * 7, s * 6))
    mapng.paste(telephone, (s * 7, s * 5))
    mapng.paste(right_bottom_corner, (s * 7, s * 2))
    os.chdir(savedir)
    mapng.save('map.png', 'PNG')
    # mapng.show()
    return