
# Trapping Rain Water -- Leetcode HARD! 
# https://leetcode.com/problems/trapping-rain-water/ 


'''
    *** Idea 1 ***
    The idea is to keep a track of the leftMax and rightMax 
    !Build Solution at every single step! 

    At every height[i]: 
        treppedWater += min(leftMax, rightMax) - height[i] 
    
    Idea 1:
    Create a leftMax array              O(n) space  
    Create a rightMax array             O(n) space
    Iterate and add the trappedWater    O(n) time 
    
    ''' 

# Solution 1 
# O(N) time, O(N) space 

def trap(height):
    leftMax = [0] * len(height)
    rightMax = [0] * len(height)
    
    # populate leftMax 
    leftMax[0] = 0
    currMax = height[0]
    for i in range(1, len(height) -1):
        leftMax[i] = currMax 

        if height[i] > currMax:
            currMax = height[i]
    
    print(leftMax)

    # populate rightMax (reverse order)
    currMax = 0
    rightMax[-1] = height[-1] 
    for i in range(len(height)-1, -1, -1):
        rightMax[i] = currMax 

        if height[i] > currMax:
            currMax = height[i]
        
    
    print(rightMax)
    
    trappedWater = 0 
    for i in range(len(height) -1):
        currentWaterLevel = min(leftMax[i], rightMax[i]) - height[i]
        if currentWaterLevel > 0:
            trappedWater+= currentWaterLevel
        
    return trappedWater 
        

    '''    
    Idea 2:
    Do the problem on the go by using a 2-pointer technique 
    The idea is that we don't need to store both leftMax and rightMax arrays since we need to take 
    the min of both and we can do this on the go (like DP)

    !Build Solution at every single step! 

    '''


def trapWater(height):
    left, right = 0, len(height) - 1 
    leftMax = height[left]
    rightMax = height[right]
    trappedWater = 0
    
    while left < right:
        if leftMax <= rightMax: 
            left += 1 
            leftMax = max(leftMax, height[left])
            trappedWater += (leftMax - height[left]) 
        else:
            right -= 1 
            rightMax = max(rightMax, height[right])
            trappedWater += (rightMax - height[right])
    
    return trappedWater     


height = [0,1,0,2,1,0,1,3,2,1,2,1]
height =  [4,2,0,3,2,5]
print(trapWater(height))






