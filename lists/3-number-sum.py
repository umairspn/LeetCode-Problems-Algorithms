
################################################################

# Given a targetSum, return the triplets from an array that sums up to the given targetSum 

# Approach 1: Brute Force 
# 3 for loops >> i,j,k >> if sum(i,j,k) == targetSum  >> append into array >> O(N^3)

# Approach 2: Sort the array + 2-pointers 
# Sort the array first 
# Apply 2-pointer approach for each i index --> p1 = i+1, p2 = len(arr) - 1

def threeNumberSum(array, targetSum):
    pass 


# test case 1 
array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0
# [-8, 2, 6],
# [-8, 3, 5],
# [-6, 1, 5]

# test case 2 
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
targetSum = 32
# [8, 9, 15]


print(threeNumberSum(array, targetSum))


################################################################


# O(N^2) efficient appproach
# 1. Sort the array 
# 2. Have 3 pointers >> p1= i+1, p2= i+2, p3 = len(arr)-2 
# 3. for every i in the array --> while start < end 
    # currSum =  start + p1 + p2 + p3 
    # while p2 <= p3:
        # if currSum == target  >> append into res 
        # if currSum < target:  p1 +=1, p2+=1  
        # if currSum > target:  p3 -=1 

def fourNumberSum(array, targetSum):
    res = []
    array.sort()
    start = 0
    end = len(array) - 1
    while start <= end:
        p1 = start + 1 
        p2 = start + 2
        p3 = len(array) - 1

        while p2 <= p3:
            currSum = array[start] + array[p1] + array[p2] + array[p3]

            if currSum == targetSum:
                res.append([array[start],array[p1],array[p2],array[p3]])
            
            if currSum < targetSum:
                # p1 +=1 
                p2 +=1 

            else:
                p3 -=1 

        start += 1

    return res 



array = [7, 6, 4, -1, 1, 2]
targetSum = 16 

# [7, 6, 4, -1],
# [7, 6, 1, 2]


array = [-10, -3, -5, 2, 15, -7, 28, -6, 12, 8, 11, 5]
targetSum = 20

# [-5, 2, 15, 8],
# [-3, 2, -7, 28],
# [-10, -3, 28, 5],
# [-10, 28, -6, 8],
# [-7, 28, -6, 5],
# [-5, 2, 12, 11],
# [-5, 12, 8, 5]

print(fourNumberSum(array, targetSum))


################################################################





































