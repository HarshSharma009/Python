# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:03:55 2020

@author: Harsh Sharma
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def isempty(self):
        if self.head is None:
            return True
        else:
            return False
        
    '''This method is find the length of the linked list'''
    def listLength(self):
        curr=self.head
        l=0
        while curr.next is not None:
            l+=1
            curr=curr.next
        return l
    
    '''Inserting element at starting by swapping object of head and new node'''
    def inserthead(self,node):
        temp=self.head
        self.head=node
        self.head.next=temp
        del temp
    
    '''This method is for inseting the element at the last'''
    def insert(self,node):
        if self.head is None:
            self.head=node
        else:
            lastnode=self.head
            while not(lastnode.next is None):
                lastnode=lastnode.next
            lastnode.next=node
            
    '''This method is for insertin the element at certain position'''
    def insertAt(self,nn,pos):
        if pos<0 or pos>self.listLength():
            return 'Invalid Position'
        if pos==0:
            self.insert(nn)
            return
        curr=self.head
        currpos=0
        while True:
            if currpos==pos:
                #previous.next=nn
                nn.next=curr
                break
            #previous = curr
            curr = curr.next
            currpos += 1
    
    def delete(self):
        previous=curr=self.head
        while curr.next is not None:
            previous=curr
            curr=curr.next
        previous.next=None
        return curr.data
        del curr
        
    def deleteHead(self):
        self.head=self.head.next
        
        
    def deleteAt(self,pos):
        if pos<0 or pos>=self.listLength():
            return 'Invalid Position'
        if self.isempty() is False:
            if pos==0:
                self.deleteHead()
                return
            curr=self.head
            l=0
            while True:
                if l==pos:
                    previous.next=curr.next
                    curr.next=None
                    break
                previous=curr
                curr=curr.next
                l+=1
        else:
            print('Trying to delete from an Empty List')
            
    '''This method print the element in the list'''
    def show(self):
        curr=self.head
        while curr is not None:
            print(curr.data)
            curr=curr.next
    
    '''This method return size of the List or By printing the object'''
    def __str__(self):
        return 'Linked List of size: '+str(self.listLength()+1)


l=LinkedList()

firstnode=Node(1)
l.insert(firstnode)

sn=Node(2)
l.insert(sn)

tn=Node(3)
l.insertAt(tn,1)

l.show()
l.deleteAt(0)
l.show()
