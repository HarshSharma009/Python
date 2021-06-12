# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:43:41 2020

@author: Harsh Sharma
"""

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def isempty(self):
        return (self.value==None)

    def append(self,v):
        if self.isempty():
            self.value=v
        elif self.next==None:
            nn=Node(v)
            self.next=nn
        else:
            (self.next).append(v)
    def inserthead(self,v):
        if self.isempty():
            self.value=v
            return
        else:
            nn=Node(v)
            
            nn.value,self.value=self.value,nn.value
            self.next,nn.next=nn,self.next
            return
    
    def bubblesort(self):
        t1=self
        t2=self.next
        while t1!=None:
            tmp=t1
            t2=t1.next
            while t2!=None:
                
                
                if t1.value>t2.value:
                    t1.value,t2.value=t2.value,t1.value
                    t1=t1.next
                t2=t2.next
            t1=tmp.next
    def bubblesort1(self):
        t1=self
        n=self.listLength()
        for i in range(n):
            for j in range(n-i-1):
                if t1.next.value<t1.value:
                    t1.next.value,t1.value=t1.value,t1.next.value
                t1=t1.next
            t1=self
            
    @classmethod    
    def addll(cls,l1,l2):
        n=Node(l1.value+l2.value)
        
        while l1.next!=None and l2.next!=None:
            l1=l1.next;l2=l2.next
            n.append(l1.value+l2.value)
        return n
    
    def listLength(self):
        le=1
        l=self
        while l.next is not None:
            le+=1
            l.next=l.next.next
        
        return le
    def count(self,c=0):
        
        if self.next==None:
            return 1
        else:
            return 1+self.next.count()
    
    def delete(self,v):
        if self.isempty():
            print('Empty List')
            return
        if self.value ==v:
            if self.next == None:
                self.value=None
                return
            else:
                self.value=self.next.value
                self.next=self.next.next
                return
        tmp=self
        while tmp.next!=None:
            if tmp.next.value==v:
                tmp.next=tmp.next.next
                return
            else:
                tmp=tmp.next
                
        else:
            print('not in list')
            return
    @classmethod
    def createList(cls,l):
        n=Node()
        for i in l:
            n.append(i)
        return n
    
    @classmethod
    def concat(cls,l1,l2):
        while l1.next != None:
            l1=l1.next
        l1.next=l2
    @classmethod
    def reverse(cls,l):
        prev=None
        current_node=l
        while current_node is not None:
            n=current_node.next
            current_node.next=prev
            prev=current_node
            current_node=n
        return prev
    
    
        
    def swap(self):
        if self.next==None:
            return
        else:
            (self.value,self.next.value)=(self.next.value,self.value)
            self.next.swap()
    def leftrotate(self,n=1):
        n=n%self.listLength()
        for i in range(n):
            self.swap()
    
    def rswap(self):
        if self.next==None:
            return
        else:
            tmp=self
            while tmp.next!=None:
                tmp=tmp.next
            while self.next.next!=None:
                self.value,tmp.value=tmp.value,self.value
                self=self.next
            self.value,tmp.value=tmp.value,self.value
    def riswap(self):
        t1=self
        
        while t1.next.next!=None:
            t1=t1.next
        t2=t1.next
        t1.next=None
        self.inserthead(t2.value)
        
    def rightrotate(self,n=1):
        n=n%self.listLength()
        for i in range(n):
            self.riswap()
        
        
            
    def show(self):
        if self.isempty():
            return
        elif self.next==None:
            print(self.value)
            return
        else:
            print(str(self.value)+'-->',end='')
            (self.next).show()
            