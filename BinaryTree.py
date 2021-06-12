# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:02:07 2020

@author: Harsh Sharma
"""
#Binary Tree

class obj:
    pass

class Node(obj):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(obj):
    def __init__(self,root):
        self.root=Node(root)
        
    def print_tree(self,traversal_type=None):
        if traversal_type=='preorder':
            return self.preorderTraversal(t.root,'')[:-1]
        elif traversal_type=='inorder':
            return self.inorderTraversal(t.root,'')[:-1]
        elif traversal_type=='postorder':
            return self.postorderTraversal(t.root,'')[:-1]
        
    def preorderTraversal(self,start,traversal):
        if start:
            traversal+=(str(start.value)+'-')
            traversal=self.preorderTraversal(start.left,traversal)
            traversal=self.preorderTraversal(start.right,traversal)
        return traversal
        
    def inorderTraversal(self,start,traversal):
        
        if start:
            traversal=self.inorderTraversal(start.left,traversal)
            traversal += (str(start.value)+'-')
            traversal=self.inorderTraversal(start.right,traversal)
        return traversal
    
    def postorderTraversal(self,start,traversal):
        if start:
            traversal=self.inorderTraversal(start.left,traversal)
            traversal=self.inorderTraversal(start.right,traversal)
            traversal += (str(start.value)+'-')
        return traversal
        
        
t=BinaryTree(5)
t.root.left=Node(3)
t.root.right=Node(6)
'''
t=int(input())
for _ in range(t):
    desti=int(input())
    N=int(input())
    d={}
    for i in range(N):
        l=[int(i) for i in input().split()]
        if l[0] in d:
            d[l[0]].append(l[1],l[2])
        else:
            d[l[0]]=[[l[1],l[2]]]
    i=1
    count=0
    while i<desti:
        if i in d:
            for i in 
        
'''
