# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:07:45 2021

@author: pranoy
"""
def display_hash(hashTable): 
      
    for i in range(len(hashTable)): 
        print(i, end = " ") 
          
        for j in hashTable[i]: 
            print("-->", end = " ") 
            print(j, end = " ") 
              
        print() 
  
"""Defining hash table as a nester loop""" 
HashTable = [[] for _ in range(10)] 
  
# Hashing Function to return  
# key for every value. 
def Hashing(keyvalue): 
    return hash(keyvalue) % len(HashTable) 
  
  
"""Inserting values into the hash table""" 
def insert(Hashtable, keyvalue, value): 
      
    hash_key = Hashing(keyvalue) 
    Hashtable[hash_key].append([keyvalue,value]) 

"""Getting values from the has table"""
def get(HashTable, keyvalue):
    hash_key = Hashing(keyvalue)
    try:
        hash_arr = HashTable[hash_key]
        for i in hash_arr:
            if i[0]==keyvalue:
                return i[1]
        print('Invalid Key')
                
    except IndexError:
        print('Invalid Key')
    return
  
# Driver Code 
insert(HashTable, 10, 'Allahabad') 
insert(HashTable, 25, 'Mumbai') 
insert(HashTable, 20, 'Mathura') 
insert(HashTable, 9, 'Delhi') 
insert(HashTable, 21, 'Punjab') 
insert(HashTable, 31, 'Noida') 
insert(HashTable, 'str1', 'Noida') 

  
display_hash (HashTable) 

print(get(HashTable, 21))
print(get(HashTable,'str1'))