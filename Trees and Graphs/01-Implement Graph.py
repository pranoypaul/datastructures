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

class Tree:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}