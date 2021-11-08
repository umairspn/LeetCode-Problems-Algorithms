
# Min Jumps Question Leetcode 

# Problem:               
 # We have an array where each index represents the jump that we can take in order to move to the end of the array
 # [1,1,5,1,1,0,2]           
 # [1,2,3,1,1,0,0,1,1]       

# The question has 3 parts:
    # 1. Can we simply check if we can reach the end from the Starting Index? --> return either a True or False 
    # 2. What are the MIN number of jumps we need to reach the end? --> 
    # 3. Min Jump III (we can jump left and right from a given point) --> do we end up with zero and cannot reach the end? !  

# There are multiple ways to solve this problem
 # Iteration >> simple Loop in one go --> O(n) time  
 # Recursion >> 
 # Dynamic Programming --> O(n) 



# Algorithm -- Problem 1 # 
'''
at each index >> we have the jump 
from start, if jump hits 0 --> go back, start again from start + 1  
if jump reaches end or greater >> return True 
if number of jumps exceeds length of array >> return False 

'''

# Part 1 -- Can we reach the end? 
def canReachEnd(array):
    start = 0 
    end = len(array) - 1 
    distanceCovered = 0 
    jumpsSoFar = 0 
    prev = 0
    while start < end: 
        prev = start 
        start = start + array[start]
        jumpsSoFar += 1 

        if start >= end:
            return True 

        if array[start] == 0:
            start = prev + 1

        if jumpsSoFar > end:
            return False 

    return False 




nums1 = [2,3,1,1,4]      # true 
nums2 = [3,2,1,0,4]      # false 
nums3 = [2,5,0,0]        # true  
nums4 = [1]

print(canReachEnd(nums4))
# print(canReachEnd(nums2))
# print(canReachEnd(nums3))










