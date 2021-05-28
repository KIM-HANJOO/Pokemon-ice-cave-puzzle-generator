#######################################################################
#################### ice-cave puzzle library ##########################
import numpy as np
from random import *

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher
#def nextile(now, horizontal, maps)

#######################################################################
#######################################################################

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

        rockend = np.array([rockend_1, rockend_2])
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

        rockend = np.array([rockend_1, rockend_2])
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

#######################################################################
#######################################################################

# def writemap (maps, rocks, path)

def writemap(maps, now, path, rocks, rock_now, num_path, num_rocks, horizontal, now_latest):
    
    if horizontal == 1:
        # add path to maps
        maps[now[0], min(now[1], now_latest[1]) : max(now[1], now_latest[1])] = 0.001
        if now[1] > now_latest[1] :
            path_add = np.arange(now_latest[1], now[1] + 1, 1)
        elif now[1] < now_latest[1] :
            path_add = np.arange(now_latest[1], now[1] - 1, -1)
            
        # add path to path
        for  i in range(0, max(now[1], now_latest[1]) - min(now[1], now_latest[1]) + 1):
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
        for  i in range(0, max(now[0], now_latest[0]) - min(now[0], now_latest[0]) + 1):
            path[num_path, :] = [path_add[i], now[1]]
            num_path = num_path + 1

    # add rock to rocks
    rocks[num_rocks][0] = rock_now[0]
    rocks[num_rocks][1] = rock_now[1]
    num_rocks = num_rocks + 1

    
    return maps, path, rocks, num_path, num_rocks

#######################################################################
#######################################################################



def endcheck(keep, maps, now, endpoint, horizontal, horizontal_e):
      
    
    if horizontal != horizontal_e:
        keep = 1

    elif horizontal == horizontal_e:
        

        if horizontal == 0:
            map_endcheck = maps[:, now[1]]
            owns_endcheck = np.arange(map_endcheck.shape[0])
            checker = np.zeros(map_endcheck.shape[0])

            for i in range(0, checker.shape[0]):
                checker[i] = 100 * map_endcheck[i] * (now[1] - owns_endcheck[i])

            leftend = 0
            rightend = 0
            for i in range(0, checker.shape[0]):
                if checker[i] > 99:
                    leftend = i
                if checker[i] > -99:
                    rockend = i + 1

            for i in range(endpoint.shape[0]):
                if (endpoint[i] - np.array([leftend, [now[1]]]))[0] == 0 and (endpoint[i] - np.array([leftend, [now[1]]]))[1] == 0 :
                    keep = 0
    
                elif (endpoint[i] - np.array([rightend, [now[1]]]))[0] == 0 and (endpoint[i] - np.array([rightend, [now[1]]]))[1] == 0 :
                    keep = 0

            


        elif horizontal == 1:
            map_endcheck = maps[now[0], :]
            owns_endcheck = np.arange(map_endcheck.shape[0])
            checker = np.zeros(map_endcheck.shape[0])

            for i in range(0, checker.shape[0]):
                checker[i] = 100 * map_endcheck[i] * (now[0] - owns_endcheck[i])

            leftend = 0
            rightend = 0
            for i in range(0, checker.shape[0]):
                if checker[i] > 99:
                    leftend = i
                if checker[i] > -99:
                    rockend = i + 1


            for i in range(endpoint.shape[0]):
                if (endpoint[i] - np.array([now[0], leftend]))[0] == 0 and (endpoint[i] - np.array([now[0], leftend]))[1] == 0 :
                    keep = 0
 
                elif (endpoint[i] - np.array([now[0], rightend]))[0] == 0 and (endpoint[i] - np.array([now[0], rightend]))[1] == 0 :
                    keep = 0

    return keep
