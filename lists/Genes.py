# Bear and Steady Gene
# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem 


'''
gene = "ACTG"
We need to find the number of smallest possible substring that needs to be replaced in order to make the string a steady Gene 
A steady gene --> "ACTG" are repeated n/4 times  

Part 1:
How to find the substrings 

Part 2:
Find the missing numebers and try to replace them within the substrings 

** Method 1 ** replace in 1 go O(N), O(1)
input = GAAATAAA

G:1 -- +1  
A:6 -- -4 -- replace with 1G, 1T, 2C  
T:1 -- +1  
C:0 -- +2
i.e., substring should have at least 4 A's 
G A A (G) T (T) (C) (C) + 1 = 5 

G:1 -- +1  
A:6 -- -4 -- replace with 1G, 1T, 2C  
T:1 -- +1  
C:0 -- +2

We wish to find the missing one! 
'''

####################################################################################################

rep = {}
missing_rep = {}
input = "GAAATAAA"
gene = 'ACTG'
repeated = len(input)/4        

for ch in input:
    if ch not in rep:
        rep[ch] = 1 
    else:
        rep[ch] += 1         

for ch in gene:
    if ch not in rep:
        rep[ch] = 0

substrings = []
string = "GAAATAAA"
for i in range(len(string)):
    for j in range(i, len(string) + 1):
        if i!=j:
            substrings.append(string[i:j])

for ch in string:
    missing_rep[ch] = repeated - rep[ch]

to_add = ''
to_replace = ''
len_replace = 0

for key, val in missing_rep.items():
    if val > 0:
        to_add += key * int(val)
    if val < 0:
        # to_replace += str(key * abs(int(val))) 
        to_replace = key
        len_replace = val 

print(to_add, to_replace, len_replace)

for subs in substrings:
    if subs.count(to_replace) == abs(len_replace):
        print(subs)
# This is not complete code 

####################################################################################################

# Can we use a Window Sliding technique? 
'''
We keep sliding the window until we hit a condition

What condition:
every letter in AEGT should have occured n/4 times  

At every step --> need to check:
if count of character in the dict so far exceeds 2 --> counter+=1 (we replace with some other ch and increase it's counter)

i.e., 

start = 0 
end = 0 
we move end till our condition hits 

gene = ACGT 
string = GAAATAAA

Can_Replace = {G:1, C:2, T:1}

start = 0, end = 0          G:1
start = 0, end = 1          G:1, A:1
start = 0, end = 2          G:1, A:2 (A reached it's limit)
start = 0, end = 3          G:1, A:2 --> we need to replace A with any key from Can_Replace --> Let's pick G --> Can_Replace = {G:0, C:2, T:1}            counter = 1 
start = 0, end = 4          G:2, A:2, T:1 
start = 0, end = 5          G:2, A:2, T:1 --> we need to replace A with any key from Can_Replace --> Let's pick C --> Can_Replace = {G:0, C:1, T:1}       counter = 2 
start = 0, end = 6          G:2, A:2, C:1, T:1 --> we need to replace A with any key from Can_Replace --> Let's pick C --> Can_Replace = {G:0, C:0, T:1}  counter = 3
start = 0, end = 7          G:2, A:2, C:2, T:1 --> we need to replace A with any key from Can_Replace --> Let's pick T --> Can_Replace = {G:0, C:0, T:0}  counter = 4 

At this point --> we have successfully formulated a gene from a string and count the number of replacements required 
However, we need to return the length of the entire substring which is replaced 
We can simply calculate the distance between the first occurance of replacement to the last --> i.e., 1st at 3, last at 7 --> distance = (7-3) + 1 = 5 
'''
