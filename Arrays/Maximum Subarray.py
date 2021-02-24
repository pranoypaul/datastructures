# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 00:19:28 2021

@author: pranoy

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and 
return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Node: 
     
    def __init__(self, x):
         
        # To store the maximum sum for a sub-array 
        self.max = x
         
        # To store the maximum leftfix sum for a sub-array
        self.left = x
         
        # To store the maximum rightfix sum for a sub-array
        self.right = x
         
        # To store the total sum for a sub-array
        self.sum = x
         
# Function to merge the 2 nodes left and right 
def merge(l, r): 
     
    # Creating node ans 
    ans = Node(0) 
    print(l.left, '(',l.sum,'+',r.left,')','(', l.sum,'+',r.sum, ')')
    ans.left = max(l.left, l.sum+r.left, l.sum+r.sum)
    print('left',ans.left)
    
    print(r.right,'(', r.sum,'+',l.right,')','(' ,l.sum,'+',r.sum,')')
    ans.right = max(r.right, r.sum+l.right, l.sum+r.sum) 
    print('right',ans.right)
    
    print(l.sum, r.sum)
    ans.sum = l.sum + r.sum 
    print('sum',ans.sum)
    
    print(ans.left, ans.right, ans.sum, l.max, r.max, l.right+r.left)
    ans.max = max(ans.left, ans.right, ans.sum,
                    l.max, r.max, l.right+r.left) 
    
    print(ans.max)
    print('-----------------------')

    # Return the ans Node 
    return ans 

def getMaxSumSubArray(l, r, arr, s): 
    
    if l == r: 
        print(l,r, '=>', arr[l])
        print('***********')
        return Node(arr[l]) 
 
    mid = (l + r) // 2
    # Call method to return left Node: 
    left = getMaxSumSubArray(l, mid, arr, 'l') 
     
    # Call method to return right Node: 
    right = getMaxSumSubArray(mid+1, r, arr, 'r') 

     
    # Return the merged Node: 
    
    val = merge(left, right)
    print(s)
    print(l,mid, r)
    print(val.left)
    print(val.right)
    print(val.sum)
    print('------xxxxxx----------')
    return val 

arr = [-2, -5, 6, -2, -3, 1, 5, -6] 
n = len(arr) 
ans = getMaxSumSubArray(0, n-1, arr, 'f') 
print("Answer is", ans.max)