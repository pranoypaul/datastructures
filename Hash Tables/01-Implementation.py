# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:07:45 2021

@author: pranoy
"""

  
"""Defining hash table as a nester loop""" 

class HashTable:
    
    def __init__(self, count):
        
        self.data=[[] for _ in range(count)]
        self.count=count
  
    # Hashing Function to return  
    # key for every value. 
    def Hashing(self,keyvalue): 
        return hash(keyvalue) % self.count 
      
      
    """Inserting values into the hash table""" 
    def insert(self,keyvalue, value): 
          
        hash_key = self.Hashing(keyvalue) 
        self.data[hash_key].append([keyvalue,value]) 
    
    def display_hash(self): 
      
        for i in range(self.count): 
            print(i, end = " ") 
            for j in self.data[i]: 
                print("-->", end = " ") 
                print(j, end = " ") 
                  
            print() 
        
    """Getting values from the has table"""
    def get(self,keyvalue):
        hash_key = self.Hashing(keyvalue)
        try:
            hash_arr = self.data[hash_key]
            for i in hash_arr:
                if i[0]==keyvalue:
                    return i[1]
            print('Invalid Key')
                    
        except IndexError:
            print('Invalid Key')
        return
    
    def keys(self):
        keyList = []
        for hashArray in self.data:
            for element in hashArray:
                keyList.append(element[0])
        return keyList
                
    

# Driver Code 
myHashTable = HashTable(10)
myHashTable.insert(10, 'Allahabad') 
myHashTable.insert(25, 'Mumbai') 
myHashTable.insert( 20, 'Mathura') 
myHashTable.insert(9, 'Delhi') 
myHashTable.insert(21, 'Punjab') 
myHashTable.insert(31, 'Noida') 
myHashTable.insert('str1', 'Noida') 

  
myHashTable.display_hash () 

print(myHashTable.get(21))
print(myHashTable.get('str1'))
