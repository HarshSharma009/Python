# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:53:54 2020

@author: Harsh Sharma
"""

global N
N=int(input())
def printsol(board):
    for i in board:
        for j in i:
            print(j,end=' ')
        print()
    
def issafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    
    for i,j in zip(range(row,N,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True


def solveNq(board,col):
    if col>=N:
        return True
    
    for i in range(N):
        if issafe(board,i,col):
            board[i][col]=1
            if solveNq(board,col+1)==True:
                return True
            board[i][col]=0
        
    return False

board=[[0 for _ in range(N)] for _ in range(N)]
solveNq(board,0)
printsol(board)