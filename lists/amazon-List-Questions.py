
# Important List Problems! 

# Run Length Encoding 
 # given a string, return the run length encoded in the output string 
 # “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6” 


# *** THE MOST IMPORTANT QUESTION ***
 # Median in a stream of integers (running integers)
 # https://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/ 


# Count All Palindrome Sub-Strings in a String
    # https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/

# 3 Number Sum 

# Longest Palindrome Substring
    # Given a string s, find the longest palindromic substring in s. 

# Search Suggestions System
# https://leetcode.com/problems/search-suggestions-system/


# This is 2 pointer approach 
def searchRotatedArray2P(array, target):
    start = 0 
    end = len(array) - 1 

    while start <= end:
        if array[start] == target:
            return start

        if array[end] == target:
            return end 

        start+=1 
        end-=1 


def searchRotatedArray(array, target):
    start = 0 
    end = 0 

    while start <= end:
        mid = (start+end) // 2 
        if array[mid] == target:
            return mid 

        # left vs right choice 


def findPivot(array):
    start = 0 
    end = len(array) - 1 

    while start <= end:
        mid = (start+end) // 2

        # RHS is completely sorted --> pivot has to be on the LHS 
        if array[mid] > array[mid+1] and mid < end:
            return mid 

        if array[mid] < array[mid-1] and mid > start:
            return mid - 1 
        
        if array[start] >= array[mid]:
            end = mid - 1 
        else:
            start = mid + 1  



target = 9
array = [7,8,9,1,2,3,4,5,6]
print(findPivot(array))




# Solution 1 (could be not acceptable) 
def removeDuplicates(array):
  
  for start in range(len(array)-1):
    if array[start] == array[start+1]:				# we found a duplicate 
      array.append(array[start+1])
      array.pop(start+1)
      array[-1] = None 
      start = start - 1 
  
  return array 


# Main Function 
nums = [1,1,2] 								# Output: 2, nums = [1,2,_]
print(removeDuplicates(nums)) 

nums = [0,0,1,1,1,2,2,3,3,4]  # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates(nums)) 



# Solution 1 (could be not acceptable) 
def removeDuplicates(array):

    start = 0 
    end = len(array) - 1 

    while start < end:
        
        # next is duplicate
        if array[start] == array[start + 1]:         
            array.append(None)
            array.pop(start+1) 
            end -= 1
        else:
            start += 1

    return array

# Main Function 
# nums = [1,1,2] 								# Output: 2, nums = [1,2,_]
# print(removeDuplicates(array)) 
nums = [0,0,1,1,1,2,2,3,3,4]  # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates(nums)) 

# we have current index of the array  
# check if next is duplicate 
# append None to the end 
# pop next element 