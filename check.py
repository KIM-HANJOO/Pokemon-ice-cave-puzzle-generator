# Libraries
import numpy as np
import matplotlib.pyplot as plt
from random import *

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher
#import pygame as pg

###################################################################
# Set-ups

width = 6
length = 6

startpoint = np.array([[0, 2], [0, 3]]) # same as (1, 3), (1, 4)
endpoint = np.array([[3, 7], [4, 7]]) # same as (4, 8), (5, 8)

initial_rocks = np.array([[4, 5]]) # same as (5, 6)
odds_of_rocks = 0.1 # 10% odds of rocks

####################################################################

# Plot setups
maps = np.zeros((length + 2, width + 2))

## set rocks
maps[:, 0] = 1
maps[:, width + 1] = 1
maps[length + 1, :] = 1
maps[0, :] = 1

for i in range(0, initial_rocks.shape[0]):
    maps[initial_rocks[i][0], initial_rocks[i][1]] = 1
    
for i in range(0, startpoint.shape[0]):
    maps[startpoint[i][0], startpoint[i][1]] = 2
    
for i in range(0, endpoint.shape[0]):
    maps[endpoint[i][0], endpoint[i][1]] = 3
    

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


## set initial setups
keep = 1

row = startpoint[0]
column = startpoint[1]

horizontal = horizontal_s
vertical = vertical_s

now = startpoint

### path set
path = np.zeros([(length + 2) * (width + 2), 2])
path[0, :] = startpoint
num_path = 1

### rock set
rocks = np.zeros([(length + 2) * (width + 2), 2])
num_rocks = 0
for i in range(0, initial_rocks.shape[0]):
    rocks[i] = initial_rocks[i]
    num_rocks = num_rocks + 1

#######################################################################
#################### ice-cave puzzle library ##########################

#def nextile(now, horizontal, maps)
def nextile(now, maps, horizontal):
        # maps_checker
    now_row = now[0]
    now_column = now[1]
        
    if horizontal == 1:
        map_now = maps[now_row, :]
        owns = np.arange(map_now.shape[0])
        map_checker = np.zeros(map_now.shape[0])

        for i in range(0, map_checker.shape[0]):
            map_checker[i] = 100 * map_now[i] * (now_column - owns[i])
            if map_checker[i] > 99:
                map_checker[i] = 100
            elif map_checker[i] < -99:
                map_checker[i] = -100

        for i in range(0, map_checker.shape[0]):  
            if map_checker[i] < 10:
                if map_checker[i] > -10:
                    #map_checker[i] = 0
                    if (map_checker[i] > 0 and map_checker[i] < 1):
                        if i < map_checker.shape[0]:
                            map_checker[i + 1] = 1

                    elif (map_checker[i] < 0 and map_checker[i] > -1):
                        if i > 0:
                            map_checker[i - 1] = 1

        rockend_1 = 0
        rockend_2 = 0
        for i in range(0, map_checker.shape[0]):
            if map_checker[i] > 99:
                rockend_1 = i
            if map_checker[i] > -99:
                rockend_2 = i + 1

        map_checker[now_column] = 1

        nextile_column = now_column
        keep_check = 1

        while keep_check == 1:
            nextile_column = randint(rockend_1 + 1, rockend_2 - 2)
            if map_checker[nextile_column] != 1:
                keep_check = 0

        now = [now_row, nextile_column]

        maps[now[0], now[1]] = 0.001

        # add rock
        # is nextile left or right
        if nextile_column - now_column < 0:
            maps[now_row, nextile_column - 1] = 1
            rock_now = np.array([now_row, nextile_column - 1])
        elif nextile_column - now_column > 0:
            maps[now_row, nextile_column + 1] = 1
            rock_now =np.array([now_row, nextile_column + 1])

    elif horizontal == 0:
        map_now = maps[:, now_column]
        owns = np.arange(map_now.shape[0])
        map_checker = np.zeros(map_now.shape[0])


        for i in range(0, map_checker.shape[0]):
            map_checker[i] = 100 * map_now[i] * (now_row - owns[i])
                #rock = 100 or -100
            if map_checker[i] > 99:
                map_checker[i] = 100
            elif map_checker[i] < -99:
                map_checker[i] = -100

        for i in range(0, map_checker.shape[0]):  

            if map_checker[i] < 10:
                if map_checker[i] > -10:
                    #map_checker[i] = 0
                    if (map_checker[i] > 0 and map_checker[i] < 1):
                        if i < map_checker.shape[0]:
                            map_checker[i + 1] = 1

                    elif (map_checker[i] < 0 and map_checker[i] > -1):
                        if i > 0:
                            map_checker[i - 1] = 1

        rockend_1 = 0
        rockend_2 = 0
        for i in range(0, map_checker.shape[0]):
            if map_checker[i] > 99:
                rockend_1 = i
            elif map_checker[i] < -99:
                rockend_2 = i + 1

        map_checker[now_row] = 1

        nextile_row = now_row
        keep_check = 1

        while keep_check == 1:
            nextile_row = randint(rockend_1 + 1, rockend_2 - 2)
            if map_checker[nextile_row] != 1:
                keep_check = 0

        now = [nextile_row, now_column]

        maps[now[0], now[1]] = 0.001

        # add rock
        # is nextile left or right
        if nextile_row - now_row < 0:
            maps[nextile_row - 1, now_column] = 1
            rock_now = np.array([nextile_row - 1, now_column])
        elif nextile_row - now_row > 0:
            maps[nextile_row + 1, now_column] = 1
            rock_now = np.array([nextile_row + 1, now_column])
        
        
        
    return now, maps, horizontal, rock_now


# writemap, path, rocks

def writemap(now, maps, now_latest, rock_now, num_path, num_rocks):
    
    if horizontal == 1:
        # add path to maps
        maps[now[0], min(now[1], now_latest[1]) : max(now[1], now_latest[1])] = 0.001
        if now[1] > now_latest[1] :
            path_add = np.arange(now_latest[1], now[1] + 1, 1)
        elif now[1] < now_latest[1] :
            path_add = np.arange(now_latest[1], now[1] - 1, -1)
            
        # add path to path
        for  i in range(0, max(now[1], now_latest[1]) - min(now[1], now_latest[1])):
            path[num_path, :] = [now[0], path_add[i]]
            num_path = num_path + 1

    elif horizontal == 0:
        # add path to maps
        maps[min(now[0], now_latest[0]) : max(now[0], now_latest[0]), now[1]] = 0.001
        if now[0] > now_latest[0] :
            path_add = np.arange(now_latest[0], now[0] + 1, 1)
        elif now[0] < now_latest[0] :
            path_add = np.arange(now_latest[0], now[0] - 1, -1)
            
        # add path to path
        for  i in range(0, max(now[0], now_latest[0]) - min(now[0], now_latest[0])):
            path[num_path, :] = [path_add[i], now[1]]
            num_path = num_path + 1

    # add rock to rocks
    rocks[num_rocks][0] = rock_now[0]
    rocks[num_rocks][1] = rock_now[1]
    num_rocks = num_rocks + 1

    
    return maps, path, rocks, num_path, num_rocks

# def endcheck

#with np.printoptions(precision=3, suppress=True):
#    print(maps)
#print(horizontal)

now_latest = now
now, maps, horizontal, rock_now = nextile(now, maps, horizontal)
maps, path, rocks, num_path, num_rocks = writemap( now, maps, now_latest, rock_now, num_path, num_rocks)
horizontal, vertical = vertical, horizontal

now_latest = now
now, maps, horizontal, rock_now = nextile(now, maps, horizontal)
maps, path, rocks, num_path, num_rocks = writemap( now, maps, now_latest, rock_now, num_path, num_rocks)
horizontal, vertical = vertical, horizontal

now_latest = now
now, maps, horizontal, rock_now = nextile(now, maps, horizontal)
maps, path, rocks, num_path, num_rocks = writemap( now, maps, now_latest, rock_now, num_path, num_rocks)
horizontal, vertical = vertical, horizontal

now_latest = now
now, maps, horizontal, rock_now = nextile(now, maps, horizontal)
maps, path, rocks, num_path, num_rocks = writemap( now, maps, now_latest, rock_now, num_path, num_rocks)
horizontal, vertical = vertical, horizontal



with np.printoptions(precision=3, suppress=True):
    print(maps)
    plt.show()

# for i in range(0, path.shape[0]):
#     if path[i, :] != [0, 0]:
#         Temp = np.zeros(i, 2)
#         Temp = path[0 : i, 0 : 1]
#         path = Temp

# for i in range(0, rocks.shape[0]):
#     if path[i, :] != np.array([0, 0]):
#         Temp = np.zeros(i, 2)
#         Temp = rocks[0 : i, 0 : 1]
#         rocks = Temp

print(path)
print(rocks)
print(now)