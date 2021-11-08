
# Tells us if our window contains all the target values 
def isTarget(substring, target):

    # use a count array --> of 26
    # Always use a counting array for this problem 

    # Get a 26 length array of each substring and target
    # Words can be between 0-26 (how to use ORD here)
    # ORD gives us the ASCII equaivlanet of a given character 
    # Compare them and return accordingly  
    
    count_S = [0] * 26
    count_T = [0] * 26

    for ch in substring:
        # aba 
        # a = 0, z = 26
        currLetter = ord(ch) - ord("a")
        count_S[currLetter] +=1 
    
    for ch in target:
        # aba 
        # a = 0, z = 26
        currLetter = ord(ch) - ord("a")

        count_T[currLetter] +=1 

    for a,b in zip(count_S, count_T):
        if b > a:
            return False 
        
    return True 


def minWindowSubstring(string, target):

    if len(target) > len(string):
        return ""

    start = 0 
    end = 0 
    windows = []
    minWindow = float("inf")
    minWindowString = ""

    while start < len(string) and end < len(string):
        currWindow = string[start:end+1]
       
        if isTarget(currWindow, target) == True:
            print(currWindow)
            # We have reached the window 
            # Store window size into a list 
            # move the start pointer ahead 

            if minWindow > len(currWindow):
                minWindow = len(currWindow)
                minWindowString = currWindow

            start +=1 
            # print("Window Reached! ", minWindow, currWindow)
        else:
            end+=1 
    
    print("Min Window is ", minWindow, minWindowString)

    return minWindowString
'''
Time Complexity:    O(M*N) where M is the len of string, N is the len of target 
Space Complexity:   O(1)

'''

s = "ADOBECODEBANC" 
t = "ABC"

s = "a"
t = "a"

s = "a"
t = "aa"

# Failing --> it returns "bba", which is not valid because "bba" != "aba" ---> correct one is "baa" 
s = "bbaa"
t = "aba"

print(minWindowSubstring(s,t))


'''
This problem can be solved with a Sliding window techniuqe 
We have start and end pointers (both zero at the start)
start is fixed and end is moved one by one until the target is reached 

if the target reached -- we move the start to reduce the window size 
if by moving the start -- our target not effected, we continue
otherwise -- we start moving end again till we reach the target 

the steps are repeated until we reach the end 
Since we kept a track of the shortest/longest window -- we can return it 
'''


