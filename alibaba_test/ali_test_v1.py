# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:13:03 2017

@author: x
"""

# check the (i,j) is in the matrix index
def isInside(row,col,i,j):
    return (i in range(row)) and (j in range(col))

# get the max step from the current point
def currentMaxStep(data,row,col,i,j):
    max_step=0
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    for (dx,dy) in directs:
        x,y = i+dx,j+dy
        if(isInside(row,col,x,y) and data[x][y] < data[i][j]):
            max_step = max([currentMaxStep(data,row,col,x,y),max_step])
    return max_step + 1

# traverse the whole data and generate the max step map
def getMaxMap(data,row,col):
    Map = [[0 for j in range(col)] for i in range(row)]
    for i in range(row):
        for j in range(col):
            Map[i][j] = currentMaxStep(data,row,col,i,j)
    print('the max step map is:')
    for i in range(row):
        print(Map[i])
    return Map

# find the max from the max step map
def maxStep(data,row,col):
    Map = getMaxMap(data,row,col)
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

