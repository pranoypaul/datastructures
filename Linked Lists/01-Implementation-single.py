# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:47:59 2021

@author: pranoy

Pros:
1)Less memory
2) Delete and insert is faster

Cons:
1)Cannot traverse back
2)Slower searching
"""

class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, headValue):
        self.head = Node(headValue)
        self.tail = self.head
        self.length = 1
        
    def traverseToIndex(self, index):
        node = self.head
        for i in range(index-1):
            node = node.next

        return node
            
    def append(self, value):
        newTail = Node(value)
        self.tail.next = newTail
        self.tail = newTail
        self.length+=1
        
    def prepend(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
        self.length+=1
    
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        node = self.traverseToIndex(index)
        newNode = Node(value)
        newNode.next = node.next
        node.next = newNode
        self.length+=1
    
    def remove(self, index):
        if index >= self.length or index < 0:
            print('Index is out of range')
            return
        node = self.traverseToIndex(index)
        if index == 0:
            self.head = node.next
        else:
            unwantedNode = node.next
            node.next = unwantedNode.next
        self.length-=1
    
    def reverse(self):
        self.tail = self.head
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printLinkedList(self):
        currentNode = self.head
        while currentNode!=None:
            print(currentNode.value, '--> ', end="")
            currentNode = currentNode.next
        print()
        
        
myLinkedList = LinkedList(10)

myLinkedList.prepend(6)
myLinkedList.append(12)
myLinkedList.insert(5, 1)
myLinkedList.printLinkedList()

myLinkedList.remove(0)
myLinkedList.printLinkedList()
myLinkedList.reverse()
myLinkedList.printLinkedList()
