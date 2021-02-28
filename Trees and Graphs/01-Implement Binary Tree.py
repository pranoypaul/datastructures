# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:08:10 2021

@author: prano
"""

class Node:
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value, end=" "),
        if self.right:
            self.right.printTree()

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        currentNode = self.root
        while(True):

            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = Node(value)
                    return
                currentNode = currentNode.left
            elif value > currentNode.value:
                if currentNode.right is None:
                    currentNode.right = Node(value)
                    return 
                currentNode = currentNode.right
            else:
                print("Node with same value already exists")
                
    def remove(self, value):
        if not self.root:
            print("The tree is empty")
            return
        currentNode = self.root
        parentNode=None
        while(currentNode):
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:#Found the node that needs to be removed
                #Condition1: No right child
                if currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                #Condition2: Right child with no left child
                elif currentNode.right.left is None:
                    if parentNode is None:
                            self.root = currentNode.right
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left
                            
                #Condition3: Right child that has a left child/children
                else:
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    #Find the left most left most node
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right
                    if parentNode is None:
                            self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost
                return
                    

    def lookup(self, value):
        if self.root.value == value:
            return True
        currentNode = self.root
        while currentNode:
            if value<currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False


    def printTree(self):
        self.root.printTree()
    
tree = BinarySearchTree()
tree.insert(10)
tree.insert(20)

tree.insert(0)

tree.insert(12)
tree.remove(10)
tree.printTree()
print(tree.lookup(12))