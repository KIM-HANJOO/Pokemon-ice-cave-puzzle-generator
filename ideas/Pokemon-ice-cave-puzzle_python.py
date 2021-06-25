{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55352593",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pygame'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-54d58506ced5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mmatplotlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpyplot\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mplt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mpygame\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpg\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'pygame'"
     ]
    }
   ],
   "source": [
    "# Libraries\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "# import pygame as pg"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "472cbbf0",
   "metadata": {},
   "outputs": [],
   "source": [
    "##################################################\n",
    "# Set-ups\n",
    "\n",
    "width = 6\n",
    "length = 6\n",
    "\n",
    "startpoint = np.array([[0, 2], [0, 3]])\n",
    "endpoint = np.array([[3, 7], [4, 7]])\n",
    "\n",
    "initial_rocks = np.array([[0, 0]])\n",
    "odds_of_rocks = 0.1\n",
    "\n",
    "##################################################"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "e4ca55af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1. 1. 2. 2. 1. 1. 1. 1.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 1.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 1.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 3.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 3.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 1.]\n",
      " [1. 0. 0. 0. 0. 0. 0. 1.]\n",
      " [1. 1. 1. 1. 1. 1. 1. 1.]]\n"
     ]
    }
   ],
   "source": [
    "# Plot setups\n",
    "map = np.zeros((length + 2, width + 2))\n",
    "\n",
    "## set rocks\n",
    "map[:, 0] = 1\n",
    "map[:, width + 1] = 1\n",
    "map[length + 1, :] = 1\n",
    "map[0, :] = 1\n",
    "\n",
    "for i in range(0, initial_rocks.shape[0]):\n",
    "    map[initial_rocks[i][0], initial_rocks[i][1]] = 1\n",
    "    \n",
    "for i in range(0, startpoint.shape[0]):\n",
    "    map[startpoint[i][0], startpoint[i][1]] = 2\n",
    "    \n",
    "for i in range(0, endpoint.shape[0]):\n",
    "    map[endpoint[i][0], endpoint[i][1]] = 3\n",
    "\n",
    "print(map)\n",
    "\n",
    "## set "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "4bf55730",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "237de80b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Main code"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
