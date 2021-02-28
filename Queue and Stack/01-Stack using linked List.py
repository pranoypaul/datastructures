# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:27:00 2021

@author: prano
"""

class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

            
    def push(self, value):
        if self.length == 0:
            self.top=Node(value)
            self.bottom=self.top
            self.length+=1
            return 
        newTop = Node(value)
        newTop.next = self.top
        self.top = newTop
        self.length+=1


    
    def pop(self):
       if not self.top:
           return None
       if self.top==self.bottom:
           self.bottom=None
       poppedNode = self.top    
       self.top = self.top.next
       self.length-=1
       return poppedNode.value
   
    def peek(self):
        if not self.top: return None
        return self.top.value
    

    def printStack(self):
        currentNode = self.top
        while currentNode!=None:
            print('|',currentNode.value,'|')
            currentNode = currentNode.next
        print()
        
        
myStack = Stack()

myStack.push(6)
myStack.push(7)
myStack.push(9)
myStack.push(12)
print(myStack.pop())
print(myStack.peek())
myStack.printStack()
