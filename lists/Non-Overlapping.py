



# return the min no. of intervals we need to remove so no interval overlaps 
def find_Overlapping_Intervals(intervals):
    counter = 0 

    # Sort intervals by end (Why?)
    intervals = sorted(intervals, key=lambda x:x[1])
    print(intervals)
    
    i = 0
    # curr = 0
    while i < len(intervals) - 1:
        if intervals[i][1] > intervals[i+1][0]:
            del intervals[i+1]          # pop the interval 
            # curr = i 
            counter+=1
        else:
            i+=1 
    
    return counter   



### Test Cases ###  

intervals1 = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
intervals2 = [[1,2],[1,2],[1,2]]
# Output: 2
intervals3 = [[1,2],[2,3]]
# Output: 0

intervals4 = [[0,2],[1,3],[2,4],[3,5],[4,6]]
# Output: 2

# print(find_Overlapping_Intervals(intervals1))
# print(find_Overlapping_Intervals(intervals2))
# print(find_Overlapping_Intervals(intervals3))
print(find_Overlapping_Intervals(intervals4))
