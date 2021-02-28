# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:27:00 2021

@author: prano
"""

class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Queue:
    
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

            
    def enqueue(self, value):
        if self.length == 0:
            self.first=Node(value)
            self.last=self.first
            self.length+=1
            return 
        newLast = Node(value)
        self.last.next = newLast
        self.last = newLast
        self.length+=1


    
    def dequeue(self):
       if not self.first:
           return None
       if self.first==self.last:
           self.last=None
       poppedNode = self.first    
       self.first = self.first.next
       self.length-=1
       return poppedNode.value
   
    def peek(self):
        if self.length==0:return None
        return self.first.value
   
    def isEmpty(self):
        if not self.first: return None
        return self.first.value
    

    def printQueue(self):
        currentNode = self.first
        while currentNode!=None:
            print(currentNode.value,'-->', end="")
            currentNode = currentNode.next
        print()
        
        
myQueue = Queue()

myQueue.enqueue(6)
myQueue.enqueue(7)
myQueue.enqueue(9)
myQueue.enqueue(12)
print(myQueue.dequeue())
myQueue.printQueue()
