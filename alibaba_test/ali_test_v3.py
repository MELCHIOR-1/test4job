# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:43:00 2017

@author: x
"""

# check the (i,j) is in the matrix index
def isInside(row,col,i,j):
    return (i in range(row)) and (j in range(col))

# check data[i][j] is the local minima
def isLocalMinima(data,row,col,i,j):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    invalid_directs = [isInside(row,col,i+dx,j+dy) and data[i][j]>data[i+dx][j+dy] for (dx,dy) in directs]
    return not any(invalid_directs)

# find the local minima
def findLocalMinimaElements(data,row,col):
    minima = []
    for i in range(row):
        for j in range(col):
            if isLocalMinima(data,row,col,i,j):
                minima.append((i,j))
    return minima

# update the local-max-step map
def updateMap(data,Map,row,col,i,j):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    for (dx,dy) in directs:
        x,y = i+dx,j+dy
        if(isInside(row,col,x,y) and data[x][y] > data[i][j] and Map[x][y] < Map[i][j]+1):
            Map[x][y] = Map[i][j]+1
            updateMap(data, Map,row,col,x,y)   

# main function
def maxStep(data,row,col):
    minima = findLocalMinimaElements(data,row,col)
    Map = [[1 for j in range(col)] for i in range(row)]
    for (min_x,min_y) in minima:
        updateMap(data,Map,row,col,min_x,min_y)
    print('the max step map is:')
    [print(Map[i]) for i in range(row)]
    return max([max(i) for i in Map])

if __name__=='__main__':
    row,col = 6,6
    data = [[32,  34,   7,  33,  21,   2],
            [13,  12,   3,  11,  26,  36],
            [16,  30,  22,  1,   24,  14],
            [20,  23,  25,  5,   19,  29],
            [27,  15,   9,  17,  31,   4],
            [ 6,  18,   8,  10,  35,  28]]
    
    print(maxStep(data,row,col))