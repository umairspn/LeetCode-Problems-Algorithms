
def maxSubarray(array):
    maxSum = float("-inf")
    currSum = 0 

    for i in range(len(array)):
        currSum += array[i]

        if currSum < 0:
            currSum = 0

        if currSum > maxSum:
            maxSum = currSum

    return maxSum


def maxContigousSum(array):
    maxSum = 0 
    counterPositive = 0
    for number in array:
        if number >=0:
            counterPositive+=1 
            maxSum+= number
    
    if counterPositive == 0:
        return -1 

    return maxSum


def maxContigousSum_RECURSION(array, counter, sumSofar):
    if counter >= len(array):
        return sumSofar


    sumSofar += maxContigousSum_RECURSION(array, counter+1, sumSofar)
    return sumSofar

array = [-1, 2, 3, -4, 5, 10]
array = [2, -1, 2, 3, 4, -5]
array = [-2, -3, -1, -4, -6]
array = [1, 2, 3, 4]
# print(maxSubarray(array), maxContigousSum(array))

print(maxContigousSum_RECURSION(array, 0, 0)) 



# return the maximum subarray sum + maximum contigous array sum 
# Subarray sum = 16     --> we use the concept where if our sum goes below 0, it becomes zero --> one pass is O(n)
# Contigous sum = 20 ---> we ignore the negatives on the go and simply add the sum -- O(n)









