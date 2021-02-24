# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:08:26 2021

@author: pranoy
Given an array nums, write a function to move all 0's
 to the end of it while maintaining the relative order 
 of the non-zero elements.
 
 Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(arr):
    count = 0
    length = len(arr)
    for i in range(length):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    zeroes = length-count
    arr[count:] = [0]*zeroes
    print(arr)
    return arr
        
        

try:    
    assert moveZeroes([2,0,4,7,9]) == [2,4,7,9,0]
    assert moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]


except Exception as e:
    print(str(e))
    print('All test cases did not pass')