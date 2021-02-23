# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:30:31 2021

@author: prano
"""
def mergeSortedArrays(arr1, arr2):
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    i = 0
    j = 0
    outputList = []
    len1 = len(arr1)
    len2 = len(arr2)
    while(i<len1 and j<len2):
        if arr1[i]< arr2[j]:
            outputList.append(arr1[i])
            i+=1
        else:
            outputList.append(arr2[j])
            j+=1
    outputList = outputList + arr1[i:] + arr2[j:]
        

    return outputList
        
    
    
print(mergeSortedArrays([0,3,4,31], [-1, 4,6,30]))