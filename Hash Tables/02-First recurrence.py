# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:13:10 2021

@author: pranoy
Find the first recurring character/value in a list
input :[0,1,2,0,4,7,9]
output: 0
"""
def firstRecurringCharacter(arr):
    readValues = {}
    for i in arr:
        if readValues.get(i,False):
            return i
        readValues[i]=True
    print("No recurrences found")
    return
        

try:    
    assert firstRecurringCharacter([0,1,2,0,4,7,9]) == 0
    assert firstRecurringCharacter(['a','c','i','k','n','c','a']) == 'c'

except Exception as e:
    print(e)
    print('All test cases did not pass')