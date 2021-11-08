
# Container with most Water problem 
# https://leetcode.com/problems/container-with-most-water/


def contains_most_water(array):
    start = 0 
    end = len(array) - 1

    distance = 0 
    MaxArea = 0 
    MaxAreaSoFar = 0 

    while start < end:
        MaxArea = (end - start) * min(array[start], array[end])
        
        if MaxArea > MaxAreaSoFar:
            MaxAreaSoFar = MaxArea
            
        if array[start] < array[end]:
            start+=1 
        else:
            end -= 1

    return MaxAreaSoFar



##### Main Function ##### 
 
height = [1,8,6,2,5,4,8,3,7]
# Output: 49

print(contains_most_water(height))