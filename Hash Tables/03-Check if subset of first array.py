# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:31:57 2021

@author: pranoy
Given two arrays: arr1[0..m-1] and arr2[0..n-1]. 
Find whether arr2[] is a subset of arr1[] or not.
 Both the arrays are not in sorted order. It may be
 assumed that elements in both array are distinct.
 
 Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
Output: True
"""
def checkSubset(arr1, arr2):
    arr1HashTable = {}
    for i in arr1:
        arr1HashTable[i]=True
    for i in arr2:
        if arr1HashTable.get(i, False):
            continue
        return False
    return True
        

try:    
    assert checkSubset([0,1,2,0,4,7,9], [1,2,4]) == True
    assert checkSubset(['a','c','i'], ['c', 'k']) == False

except Exception as e:
    print('All test cases did not pass')