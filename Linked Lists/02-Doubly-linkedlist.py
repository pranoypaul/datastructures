# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:57:51 2021

@author: pranoy

Pros:
1)Can be traversed in both directions
2)Searching is faster
Cons:
1)Requires more memory
2)Requires extra processing when deleting and inserting
"""

class Node:
    
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
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
        newTail.prev = self.tail
        self.tail.next = newTail
        self.tail = newTail
        self.length+=1
        
    def prepend(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head.prev = newHead
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
        newNode.prev = node
        node.next.prev = newNode
        node.next = newNode
        self.length+=1
    
    def remove(self, index):
        if index >= self.length or index < 0:
            print('Index is out of range')
            return
        
        node = self.traverseToIndex(index)
        unwantedNode = node.next
        unwantedNode.next.prev = node
        node.next = unwantedNode.next
        self.length-=1
        
    def printDoublyLinkedList(self):
        currentNode = self.head
        while currentNode!=None:
            print(currentNode.value, '--> ', end="")
            currentNode = currentNode.next
        print()
        currentNoderev = self.tail
        while currentNoderev!=None:
            print(currentNoderev.value, '--> ', end="")
            currentNoderev = currentNoderev.prev
        
        
myDoublyLinkedList = DoublyLinkedList(10)

myDoublyLinkedList.prepend(6)
myDoublyLinkedList.append(12)
myDoublyLinkedList.insert(5, 1)
myDoublyLinkedList.insert(15, 1)

myDoublyLinkedList.printDoublyLinkedList()
