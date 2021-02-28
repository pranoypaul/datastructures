# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:53:48 2021

@author: prano
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:27:00 2021

@author: prano
"""

        
class Stack:
    
    def __init__(self):
        self.array = []
        self.length=0
        
    def push(self, value):
        self.array.append(value)
        self.length+=1
    
    def pop(self):
        top = self.array.pop() 
        self.length-=1
        return top
   
    def peek(self):
        return self.array[-1]
    

    def printStack(self):
        for i in range(1, self.length+1):
            print('|',self.array[-i],'|')
        
        
myStack = Stack()

myStack.push(6)
myStack.push(7)
myStack.push(9)
myStack.push(12)
print(myStack.peek())
print(myStack.pop())
print(myStack.peek())
myStack.printStack()
