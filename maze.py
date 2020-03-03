# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:45:52 2020

@author: Harsh Sharma
"""

maze=[[0, '1', '0', '1', '1', '1', '0', 1],
        ['1', '1', '0', '1', '1', '0', '1', '1'],
        ['1', '0', '0', '1', '0', '0', '1', '0'],
        ['1', '0', '0', '1', '1', '0', '1', '0'],
        ['1', '0', '0', '0', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '1', '0', '1', '1'],
        ['0', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '0', '0', '0', '1', '1', '1']]
maze=[[int(maze[j][i]) for i in range(8)] for j in range(8)]
visited=[[0 for i in range(8)] for j in range(8)]
def valid(maze,i,j,visited):
    if i>=0 and i<8 and j>=0 and j<8 and maze[i][j]==1 and visited[i][j]!=1:
        return 1
    else:
        return 0
def diaplay(l):
    for i in l:
        for j in i:
            print(j,end=' ')
        print()
def path(maze,i,j,visited):
    
    if i==0 and j==7:
        visited[i][j]=1
        display(visited)
        return True
    
    elif valid(maze,i,j,visited):
        visited[i][j]=1
        if path(maze,i-1,j,visited)==True:
            return True
        
        if path(maze,i,j+1,visited)==True:
            return True
        if path(maze,i,j-1,visited)==True:
            return True
        visited[i][j]=0
        return False
        
   
        
