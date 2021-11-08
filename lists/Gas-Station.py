# Gas Station
# https://leetcode.com/problems/gas-station/ 



# Time Complexity:  O(N)
# Space Complexity: O(1)
# Approach:         Greedy    

# return the index where if we start, we can visit all gas stations 
# if no such index, return -1 
def gasStation(gas, cost):
    for i in range(len(gas)):
        for j in range(i, len(gas) + i):
            j = j % len(gas)
            print("start: ", gas[i] , " to end: ", gas[j] , "   ---> cost is ",  cost[j])

    return 

# gas = [7,1,0,11,4]
# cost = [5,9,1,2,5]

gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]

# gasStation(gas, cost)
# Output: 3

total_diff = 0 
for i in range(len(gas)):
    total_diff += gas[i] - cost[i]
    # print(total_diff)

if total_diff < 0:
    print("Not possible")
    # return -1 

else:
    tank = 0
    start = 0 
    for i in range(len(gas)):
        tank += (gas[i] - cost[i])

        if tank < 0:
            start = i + 1
            tank = 0 

    print(start)






