# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:30:46 2021

@author: pranoy

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at 
least twice in the array, and it should return false if 
every element is distinct.

Input: [1,2,3,1]
Output: true
"""
def containsDuplicates(arr):
    dataDict = {}
    for i in arr:
        check = dataDict.get(i,False)
        if check is False:
            dataDict[i] = True
        else: return True
    return False
        
        

try:    
    assert containsDuplicates([2,0,4,7,9]) == False
    assert containsDuplicates([0,1,0,3,12]) == True


except Exception as e:
    print(str(e))
    print('All test cases did not pass')