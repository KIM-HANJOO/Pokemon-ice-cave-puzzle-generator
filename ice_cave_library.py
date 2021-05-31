import numpy as np
from random import *
from numpy.core.numerictypes import maximum_sctype

from numpy.core.records import array
from numpy.lib.stride_tricks import _broadcast_to_dispatcher

#################################################################################################################
#################################################################################################################
#################################################################################################################
######################################### ice-cave puzzle library ###############################################

##### functions #####

##### nextile #####
# randomly decide the next step, considering the previous route and the stones
# code : now, maps, horizontal, rock_now = nextile(now, maps, horizontal)


##### writemap #####
# after making path, update the path and rocks to the maps
# code : maps, path, rocks, num_path, num_rocks = writemap(maps, now, path, rocks, rock_now, num_path, num_rocks, horizontal, now_latest)


##### endcheck #####
# check if the puzzle can end
# code : keep, maps, path = endcheck(keep, maps, path, now, endpoint, horizontal, horizontal_e)


##### imstuck #####
# temporarily blocks the tile that is between rocks (can be a stuck-point)
# code : maps = imstuck(maps)


##### imnotstuck #####
# delete the blocks that are made by 'imstuck'
# code : maps = imnotstuck(maps)


##### redraw #####
# redraw the array 'path', 'num_path' and 'rocks', 'num_rocks'
# code : path, num_path = redraw(path, num_path)

##### dontblockend #####
# making...

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################

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
        ################################################
        print('map_now')
        with np.printoptions(precision=3, suppress=True):
            print(map_now)
        print('i am at')
        print(now_column)
        print('now_column - owns')
        chch = np.zeros(map_now.shape[0])
        for i in range(0, map_now.shape[0]):
            chch[i] = now_column - owns[i]
        print(chch)
        print('map checker before considering path')
        print(map_checker)
        ################################################

        
        for i in range(now_column - 1, -1, - 1):
            if map_checker[i] > 0 and map_checker[i] < 1:
                map_checker[i + 1] = 1

        for i in range(now_column, map_checker.shape[0], 1):
            if map_checker[i] < 0 and map_checker[i] > -1:
                map_checker[i - 1] = 1
        # for i in range(0, map_checker.shape[0]):  
        #     if map_checker[i] < 10:
        #         if map_checker[i] > -10:
        #             #map_checker[i] = 0
        #             if (map_checker[i] > 0 and map_checker[i] < 1):
        #                 if i < map_checker.shape[0]:
        #                     map_checker[i + 1] = 1

        #             elif (map_checker[i] < 0 and map_checker[i] > -1):
        #                 if i > 0:
        #                     map_checker[i - 1] = 1
        ################################################
        print('map_checker after considering path')
        print(map_checker)
        ################################################

        rockend_1 = None
        rockend_2 = None

        rockend_1 = 0
        rockend_2 = 0
        for i in range(0, map_checker.shape[0]):
            if map_checker[i] > 99:
                rockend_1 = i
            if map_checker[i] > -99:
                rockend_2 = i

        rockend = np.array([rockend_1, rockend_2])
        map_checker[now_column] = 1

        nextile_column = now_column
        keep_check = 1

        if rockend_1 + 1 == rockend_2 - 1:
            nextile_column = now[1]
            problemo = 1

        elif rockend_1 + 1 != rockend_2 - 1:
            problemo = 0
            find_problem = 0
            while keep_check == 1 and find_problem < 100:
                if rockend_1 + 1 <= rockend_2 - 1:
                    nextile_column = randint(rockend_1 + 1, rockend_2 - 1)
                    if map_checker[nextile_column] != 1:
                        keep_check = 0
                    elif map_checker[nextile_column] == 1:
                        find_problem = find_problem + 1
                        if find_problem == 99:
                            problemo = 1
                elif rockend_1 + 1 > rockend_2 - 1:
                    keep_check = 0
                    problemo = 1

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
        ################################################
        print('map_now')
        with np.printoptions(precision=3, suppress=True):
            print(map_now)
        print('i am at')
        print(now_row)
        print('now_row - owns')
        chch = np.zeros(map_now.shape[0])
        for i in range(0, map_now.shape[0]):
            chch[i] = now_row - owns[i]
        print(chch)
        print('map checker before considering path')
        print(map_checker)
        ################################################
        for i in range(now_row - 1, -1, - 1):
            if map_checker[i] > 0 and map_checker[i] < 1:
                map_checker[i + 1] = 1

        for i in range(now_row, map_checker.shape[0], 1):
            if map_checker[i] < 0 and map_checker[i] > -1:
                map_checker[i - 1] = 1
        # for i in range(0, map_checker.shape[0]):  

        #     if map_checker[i] < 10:
        #         if map_checker[i] > -10:
        #             #map_checker[i] = 0
        #             if (map_checker[i] > 0 and map_checker[i] < 1):
        #                 if i < map_checker.shape[0]:
        #                     map_checker[i + 1] = 1

        #             elif (map_checker[i] < 0 and map_checker[i] > -1):
        #                 if i > 0:
        #                     map_checker[i - 1] = 1
        ################################################
        ################################################
        print('map_checker after considering path')
        print(map_checker)
        ################################################
        ################################################
        rockend_1 = None
        rockend_2 = None

        rockend_1 = 0
        rockend_2 = 0
        for i in range(0, map_checker.shape[0]):
            if map_checker[i] > 99:
                rockend_1 = i
            elif map_checker[i] < -99:
                rockend_2 = i

        rockend = np.array([rockend_1, rockend_2])
        map_checker[now_row] = 1

        nextile_row = now_row
        keep_check = 1
        if rockend_1 + 1 == rockend_2 - 1:
            nextile_row = now[0]
            problemo = 1
        elif rockend_1 + 1 != rockend_2 - 1:
            problemo = 0

            find_problem = 0
            while keep_check == 1 and find_problem < 100:
                if rockend_1 + 1 <= rockend_2 - 1:
                    nextile_row = randint(rockend_1 + 1, rockend_2 - 1)
                    if map_checker[nextile_row] != 1:
                        keep_check = 0
                    elif map_checker[nextile_row] == 1:
                        find_problem = find_problem + 1
                        if find_problem == 99:
                            problemo = 1
                elif rockend_1 + 1 > rockend_2 - 1:
                    keep_check = 0
                    problemo = 1

        now = [nextile_row, now_column]

        maps[now[0], now[1]] = 0.001

        # add rock
        # is nextile left or right
        ################################################
        print('map_now')
        print(map_now)
        print('rockend')
        print(rockend)
        
        print('nextile_row')
        print(nextile_row)
        print('nextile_row + 1')
        print(nextile_row + 1)
        print('now')
        print(now)
        print('now_column')
        print(now_column)
        print('map_checker')
        print(map_checker)
        ################################################
        # with np.printoptions(precision=3, suppress=True):
        #     print(maps)

        if nextile_row - now_row < 0:
            maps[nextile_row - 1, now_column] = 1
            rock_now = np.array([nextile_row - 1, now_column])
        elif nextile_row - now_row > 0:
            maps[nextile_row + 1, now_column] = 1
            rock_now = np.array([nextile_row + 1, now_column])
        
        
        
    return now, maps, horizontal, rock_now, problemo

#######################################################################
#######################################################################

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

def endcheck(keep, maps, path, num_path, now, endpoint, horizontal, horizontal_e):
      
    
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
                    rightend = i + 1
            

            for i in range(endpoint.shape[0]):
                if (endpoint[i] - np.array([leftend, [now[1]]]))[0] == 0 and (endpoint[i] - np.array([leftend, [now[1]]]))[1] == 0 :
                    keep = 0
    
                elif (endpoint[i] - np.array([rightend, [now[1]]]))[0] == 0 and (endpoint[i] - np.array([rightend, [now[1]]]))[1] == 0 :
                    keep = 0
        
            maps[min(now[0], endpoint[0][0]) : max(now[0], endpoint[0][0]), now[1]] = 0.001
        
        
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
                    rightend = i + 1
            

            for i in range(endpoint.shape[0]):
                if (endpoint[i] - np.array([now[0], leftend]))[0] == 0 and (endpoint[i] - np.array([now[0], leftend]))[1] == 0 :
                    keep = 0
 
                elif (endpoint[i] - np.array([now[0], rightend]))[0] == 0 and (endpoint[i] - np.array([now[0], rightend]))[1] == 0 :
                    keep = 0

            maps[now[0], min(now[1], endpoint[0][1]) : max(now[1], endpoint[0][1])] = 0.001


    if keep == 0:
        if horizontal_e == 1:
            if now[0] == endpoint[0][0]:
                mini = min(now[1], endpoint[0][1]) ##needs to be adjusted
                maxi = max(now[1], endpoint[0][1])

                for i in range(mini, maxi + 1):
                    path[num_path, :] = [now[0], i]
                    num_path = num_path + 1
                    
            elif now[0] == endpoint[1][0]:
                mini = min(now[1], endpoint[1][1])
                maxi = max(now[1], endpoint[1][1])

                for i in range(mini, maxi + 1):
                    path[num_path, :] = [now[0], i]
                    num_path = num_path + 1
                    
        elif horizontal_e == 0:
            if now[1] == endpoint[0][1]:
                mini = min(now[0], endpoint[0][0])
                maxi = max(now[0], endpoint[0][0])

                for i in range(mini, maxi + 1):
                    path[num_path, :] = [i, now[1]]
                    num_path = num_path + 1
                            
            if now[1] == endpoint[1][1]:
                mini = min(now[0], endpoint[1][0])
                maxi = max(now[0], endpoint[1][0])

                for i in range(mini, maxi + 1):
                    path[num_path, :] = [i, now[1]]
                    num_path = num_path + 1                        

    return keep, maps, path, num_path



#######################################################################
#######################################################################


def imstuck(maps):
    for i in range(1, maps.shape[0] - 1):
        for j in range(1, maps.shape[1] - 1):
            if maps[i, j] != 1:
                if maps[i, j + 1] == 1 and maps[i, j - 1] == 1:
                    maps[i, j] = 10
                elif maps[i + 1, j] == 1 and maps[i - 1, j] == 1:
                    maps[i, j] = 10
    return maps


#######################################################################
#######################################################################


def imnotstuck(maps):
    for i in range(maps.shape[0]):
        for j in range(maps.shape[1]):
            if maps[i, j] == 10:
                maps[i, j] = 0

    return maps


#######################################################################
#######################################################################

def redraw(path, num_path):
    for i in range(path.shape[0] - 1, 0, -1):
        if path[i][0] == path[i - 1][0] and path[i][1] == path[i - 1][1]:
            path = np.delete(path, i, axis = 0)
    
    num_path = None
    num_path = path.shape[0]

    return path, num_path


#######################################################################
#######################################################################

# def dontblockend(maps, endpoint, horizontal_e):
#     if horizontal_e == 1:
#         for i in range(maps.shape[0]):
#             for j in range(maps.shape[1]):
#                 if maps[endpoint[0]


