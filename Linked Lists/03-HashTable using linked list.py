# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:18:00 2021

@author: prano
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
        
    
    def traverseToKey(self, key):
        node = self.head
        while node is not None:
            if node.value[0] == key:
                return node
            node = node.next

        return None
    def traverseToPrevKey(self, key):
        node = self.head
        prev = None
        while node is not None:
            if node.value[0] == key:
                return prev
            prev = node
            node = node.next

        return None
            
    def insert(self, value, inplace):
        existingNode = None
        if inplace:
            existingNode = self.traverseToKey(value[0])
        if existingNode:
            existingNode.value = value
        else:
            newTail = Node(value)
            self.tail.next = newTail
            self.tail = newTail
            self.length+=1
            
    def remove(self, key):
        
        previousNode = self.traverseToPrevKey(key)
        if previousNode:
            unwantedNode = previousNode.next
            previousNode.next = unwantedNode.next
        else:
            unwantedNode = self.traverseToKey(key)
            self.head = unwantedNode.next
        self.length-=1

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, '--> ', end="")
            currentNode = currentNode.next
    
    def getKeys(self):
        currentNode = self.head
        keys = []
        while currentNode is not None:
            keys.append(currentNode.value[0])
            currentNode = currentNode.next
        return keys
        
class HashTable:
    
    def __init__(self, count):
        
        self.data=[None for _ in range(count)]
        self.count=count
  
    
    def Hashing(self,keyvalue): 
        return hash(keyvalue) % self.count 
      
      
    """Inserting values into the hash table""" 
    def set(self,keyvalue, value, inplace=False): 
          
        hash_key = self.Hashing(keyvalue) 
        if self.data[hash_key] is None:
            self.data[hash_key] = LinkedList([keyvalue,value])
        else:
            self.data[hash_key].insert([keyvalue,value], inplace) 
            
    def replace(self,keyvalue, value):
        self.set(keyvalue, value, True)
    
    def display_hash(self): 
      
        for i in range(self.count):
            if(self.data[i]):
                print(i, end=" : ")
                self.data[i].printLinkedList()
                print()
        
    """Getting values from the hash table"""
    def get(self,keyValue):
        hash_key = self.Hashing(keyValue)
        try:
            linkedList = self.data[hash_key]
            value = linkedList.traverseToKey(keyValue).value[1]
            if value:
                return value
            else:
                print('Key is invalid')

        except Exception as e:
            print('Invalid Key')
        return
    
    def delete(self, keyValue):
        hash_key = self.Hashing(keyValue)
        try:
            linkedList = self.data[hash_key]
            linkedList.remove(keyValue)
            
                    
        except Exception as e:
            print('Invalid Key')
        return
    
    def keys(self):
        keyList = []
        for linkedList in self.data:
            if linkedList:
                keyList.extend(linkedList.getKeys())
        return keyList
    
myHashTable = HashTable(10)
myHashTable.set(10, 'Allahabad') 
myHashTable.set(25, 'Mumbai') 
myHashTable.set( 20, 'Mathura') 
myHashTable.set(9, 'Delhi') 
myHashTable.set(21, 'Punjab') 
myHashTable.set(31, 'Noida') 
myHashTable.set('str1', 'Chennai') 
myHashTable.replace('str1', 'Kerala') 

myHashTable.delete(31)

  
myHashTable.display_hash () 

print(myHashTable.get(21))
print(myHashTable.get('str1'))
print(myHashTable.keys())