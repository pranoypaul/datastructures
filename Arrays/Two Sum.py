# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:01:31 2021

@author: pranoy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(arr, target):
    readValues = {}
    for i in range(len(arr)):
        if readValues.get(target-arr[i], None) is not None:
            return [i, readValues[target-arr[i]]]
        readValues[arr[i]] = i
        

try:    
    assert twoSum([2,4,7,9],9) == [2,1]

except Exception as e:
    print(e)
    print('All test cases did not pass')