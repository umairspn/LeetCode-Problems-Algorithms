
# *** Important LL questions *** 
    # Merge two Sorted Linked Lists 
    # Copy Linked List with arbitrary pointer 
    # A linked list is given, print the palindrome of link list without using extra space and linear complexity.
    # Find if a cycle exists in a given LinkedList
    # Reverse a Linked List 


class Node: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode 
        else:
            temp = self.head 
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def printLL(self):
        temp = self.head 
        while temp:
            print(temp.val)
            temp = temp.next


    # Time = O(N), Space = O(N)
    def isRepeatExist(self):
        temp = self.head
        counterDict = {} 
        while temp:
            if temp.val not in counterDict:
                counterDict[temp.val] = 1
            else:
                print("Cycle Found at", temp.val)
                return True 
            temp = temp.next
        return False 


    # Note that --> here, we store the entire node in the hash 
    # Then we see if the next node equals any node in the hash 
    # And we move to the next node (temp=temp.next) after the return line
    # So we reach our last value without hitting NULL 
    def isCycle(self):
        temp = self.head
        counterDict = {} 
        while temp:
            if temp not in counterDict:
                counterDict[temp] = 1
            
            if temp.next in counterDict:
                return True 

            temp = temp.next

        return False 


    def reverseLL(self):
        pass 


l1 = LinkedList()
inputList = [1,2,3,4,5]
for val in inputList:
    l1.insert(val)

l1.printLL()
print(l1.isRepeatExist()) 

