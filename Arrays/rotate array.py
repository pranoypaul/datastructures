# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:36:05 2021

@author: prano
"""
def rotateArray(arr, n):
    dataDict = {}
    rotate = arr[:-n-1:-1]
    rotate.extend(arr[:-n])
    print(rotate)
    return rotate
    
        
        

try:    
    assert rotateArray([2,0,4,7,9], 1) == [9,2,0,4,7]
    assert rotateArray([0,1,0,3,12, 3], 2) == [3,12,0,1,0, 3]


except Exception as e:
    print(str(e))
    print('All test cases did not pass')