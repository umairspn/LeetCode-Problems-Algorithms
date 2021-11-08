# HackerRank Challenge -- Hard Problem 
# 

'''
*** Understanding the Problem *** 

string s 
q days 
l and r --> 
max palindrome within l and r 
we can move the letters --> re-arrange the letters of the string --> that are between l and h 

everyday --> we get a new l and r
we find the max for the entire week (let's assume)

day 1 --> max: 
day 2 --> max: 

s = "week" 
q = [[1,4][2,3]]

1,4 --> max is ewe, eke --> (2) 
2,3 --> ee (1)

output = [2,1]

Sub-Problem 1:
Rearranging the letters within the given range 

0: w
1: e
2: e
3: k

1,4 --> "week"
We need the combinations (len = 3, combinations = 2)

week     -- 2 
ewek     -- 3 
eewk     
keew
kwew
kewe

Sub-Problem 2: 
finding and keeping a track of the max palindrome within each window 


*** Algorithms *** 

isPalindrome(string):
    return string == string[::-1]

res = []
maxCounter = float("-inf") 
resCounter = 0
checkWindow(string):    # week
    combinations = combinations(string)  # week, weke, kewe . . . 

    for comb in combinations: 
        
        currSubstrings = []
        for i in range(len(comb)):
            for j in range(i, len(comb)+1):
                if i != j:
                    currSubstrings.append(comb[i:j]) 

        maxNow = []
        for subs in currSubstrings: # week --> w, we, wee, week, e, ee, eek, e, ek, k  # weke --> w, we, wek, weke, e, ek, eke, k, ke, e
            if isPalindrome(subs):
                palindromeLength = len(subs)
                if maxCounter == palindromeLength:                   2 == 3
                    resCounter += 1

                if maxCounter < palindromeLength:                   --> maxCounter: 2   --> maxCounter:3
                    maxCounter = palindromeLength
                    resCounter = 1

    return resCounter 

s = "week" 
q = [[1,4][2,3]]

res = []
for window in q:
    res.append(checkWindow(s[window[0]-1: window[1])) # week


Time Complexity:    O(N^5)
Space Complexity:   O(N^2)

'''

from itertools import combinations, permutations


def isPalindrome(string):
    return string == string[::-1]

# ewek
def getMaxPalindrome(string):
    pass 

def checkWindow(string):    # week
    maxCounter = float("-inf") 
    resCounter = 0
    combs = permutations(string, len(string))               # week, weke, kewe . . . 
    globalSet = []
    combs = list(set([''.join(i) for i in combs]))

    for comb in combs: 
        print("Comb: ", comb)
        
        currSubstrings = []
        for i in range(len(comb)):
            for j in range(i, len(comb)+1):
                if i != j:
                    currSubstrings.append(comb[i:j]) 

        currSubstrings = list(set(currSubstrings))
        
        for subs in currSubstrings: # week --> w, we, wee, week, e, ee, eek, e, ek, k  # weke --> w, we, wek, weke, e, ek, eke, k, ke, e
            if isPalindrome(subs):
                print("subs: ", subs)
                
                palindromeLength = len(subs)
                if maxCounter == palindromeLength:            #       2 == 3
                    if subs not in globalSet:
                        globalSet.append(subs)
                        resCounter += 1

                if maxCounter < palindromeLength:               # --> maxCounter: 2   --> maxCounter:3
                    maxCounter = palindromeLength
                    resCounter = 1
                    globalSet = [subs]

    return resCounter 

s = "week"
q = [[1,4],[2,3]]

res = []
for window in q:
    res.append(checkWindow(s[window[0]-1: window[1]]))

print(res)


