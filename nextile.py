#def nextile(now, horizontal, maps)
import numpy as np
from random import *

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