
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import QProcess
from PyQt5.QtGui import QIcon

import sys

import numpy as np
import matplotlib.pyplot as plt
import practice_library as ice
from random import *


class GBA(QMainWindow):

    def __init__(self):
        super().__init__()
        
        ## NAME AND ICON ##
        self.setWindowTitle('Pokemon Ice-cave Puzzle')
        self.setWindowIcon(QIcon('.\images\icon.png'))
		
		## POSITION AND SIZE ##
		# 'self.setGeometry(1000, 300, 800, 1000)' / position and size
        self.move(1000, 300)
        self.resize(500, 400)
        
        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)
    def message(self, s) :
       self.text.appendPlainText(s) 

    def start_process(self):
        self.message("Executing process")
        game = Game()
        
        self.message(" github.com/suhyuuk")

class Game():
    def __init__(self) :
                
        ########### < input > ##########
                
        tiledir = 'C:\\Users\\Stephen Kim\\Documents\\GitHub\\Pokemon-ice-cave-puzzle\\self_tiles'
        savedir = 'C:\\Users\\Stephen Kim\\Documents\\GitHub\\Pokemon-ice-cave-puzzle\\result_map'

        width = 6
        length = 5

        # top = 1, bottom = 2, left = 3, right = 4

        startpoint = [2, 3] 
        startpoint_place = 1

        endpoint = [3]
        endpoint_place = 4

        ##################################
        ##################################
        problemo = 1
        trial = 1
        print('trial = ', trial - 1, end = '\r')
        while problemo == 1 :
            problemo = 0

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

            path = []
            mapplot_save_list = []
            mapplot_save_list.append(list(startpoint))
            rock_save_list = []

            while keep == 1:

                #save now
                now_latest = now.copy()
                maps_latest = maps.copy()

                #next tile
                stuck = 1
                stuck_trial = 0
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
                    stuck_trial += 1
                    if stuck_trial > 100 :
                        stuck = 0
                        problemo = 1
                
                # draw maps
                mapplot_save_list = ice.mapplot_save(now, mapplot_save_list)

                # add path, path to maps
                # path, maps = ice.addpath(now, now_latest, maps, path)

                # swap horizontal
                if horizontal == 0:
                    horizontal = 1
                else: #horizontal = 1
                    horizontal = 0

                #joint
                joint = joint + 1

                #endcheck
                if joint > 5 :
                    end = ice.endcheck(now, maps, endpoint, horizontal)
                    if end == 1:
                        keep = 0
                
                if joint > 100 :
                    problemo = 1
                        
                if problemo == 1 :
                    keep = 0
            trial += 1
            print('trial = ', trial - 1, end = '\r')


        print("maps\n", maps)
        print("route", mapplot_save_list)
        mapplot_save_list.append(list(endpoint))
        ice.mapplot(width, length, maps, rock_save_list, mapplot_save_list)
        ice.tilemap(maps, tiledir, savedir)


app = QApplication(sys.argv)

w = GBA()
w.show()

app.exec_()
