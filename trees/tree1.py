
# ****** DONE ******* #
# A binary tree is given, invert the binary tree without using extra space and linear complexity.
# Diameter of a binary tree in o(n).
# Find if the given binary tree is height balanced.
# Validate BST 
# Maximum Path Sum 
# Flatten a binary tree 

# Print Zigzag traversal of a binary tree.
# Boundary Traversal of binary tree 

# *** Most Common and Important Ones *** 
# Given preorder and inorder traversal of a tree, construct the binary tree ***
# Serialize and deserialize a binary tree ***
# Sub tree of Another Tree ***
# Delete a particular node from binary tree and free up the memory of the deleted node. ***
# Inserting an element into a BST ***

# ************** Code Starts Here *************** # 

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

# output should be 1 
def minValueinTree(root):
    if root is None:
        return float("inf") 
    return min(minValueinTree(root.left), minValueinTree(root.right), root.val)


def treeHeight(root):
    if root is None:
        return 0
    return max(treeHeight(root.left), treeHeight(root.right)) + 1 


# i.e., left,parent,right -- 2,3,1 --> gives us the closest value w.r.t. target  
# return the actual value of the node, based on the differnce between targets 
def KClose_Helper(left, parent, right, target):
    left_diff = abs(target-left)
    parent_diff = abs(target-parent)
    right_diff = abs(target-right)

    closest = min(left_diff, parent_diff, right_diff)

    if closest == left_diff:
        return left 
    
    if closest == parent_diff:
        return parent     
    
    if closest == right_diff:
        return right


def kClose(root, target):
    if root is None:
        return float("inf")

    return KClose_Helper(kClose(root.left, target), root.val, 
    kClose(root.right, target), target)


# Itertive BFS 
def levelOrder_Iterative(root):
    queue = [root]
    while queue:
        popped = queue.pop(0)
        print(popped.val)
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)

# Recursive BFS 
def levelOrderBFSHelper(root, level):
    if level <=1:
        print(root.val)
    
    elif level > 1:
        levelOrderBFSHelper(root.left, level - 1)
        levelOrderBFSHelper(root.right, level - 1)

def levelOrder_Recursive(root):
    height = treeHeight(root)
    for level in range(1, height+1):
        levelOrderBFSHelper(root, level)


def invertTree(root):
    if root is None:
        return 

    # left = root.left 
    # right = root.right
    
    # this also works 
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root 


# Number of nodes on the longest path between two leaves in the tree
def diameterTree(root):
    if root is None:
        return 0 
    
    leftH = treeHeight(root.left)
    rightH = treeHeight(root.right)

    leftD = diameterTree(root.left)
    rightD = diameterTree(root.right)

    print(root.val, "--->", leftH, rightH, leftD, rightD)

    return max(leftH + rightH + 1, max(leftD, rightD))

def validateBSTHelper(root, MIN, MAX):
    if root is None:
        return True 
    if root.val >= MAX or root.val < MIN:
        return False 
    return validateBSTHelper(root.left, MIN, root.val) and validateBSTHelper(root.right, root.val, MAX)

def validateBST(root):
    # root, MIN, MAX 
    return validateBSTHelper(root, float("-inf"), float("inf"))


# Is the height of left subtree, equal to the height of right subtree?  
def isHeightBalanced(root):
    if root is None:
        return True 

    leftH = treeHeight(root.left)
    rightH = treeHeight(root.right)

    if abs(leftH - rightH) > 1:
        return False 

    return isHeightBalanced(root.left) and isHeightBalanced(root.right)


# Flatten a Binary Tree into a LinkedList (PreOrder)
def flattenTree(root):

    # Do something here 
    # pick the entire Left subtree (Lst)
    # save the entire Right subtree into saved (Rst)
    # put Lst in the place of root.right 
    # go all the way to the root's right and place the RST 
    # repeat until done 
    # return the root 

    if root is None:
        return  

    flattenTree(root.left)
    flattenTree(root.right)

    rightSubtree = root.right 
    root.right = root.left 
    root.left = None 

    while root.right:
        root = root.right 
    
    root.right = rightSubtree


############### 
# we are given a list --> find the max element index -- that should be the root 
# recursively call our function -->    and   
# it will take the left root as --> max of start to i-1
# it will take the left root as -->i+1 to end 
 
# Question --> construct special tree from Inorder ^ revise the above idea on Ipad 

# # Very important 
#   def deleteNode(root):
#     pass 


def zigzagTraversal(root):
    pass 

def boundaryTraversal(root):
    pass 



###############
# We hava the root of our tree, and the root of a subtree 
# We need to check if this subtree is part of our tree 

def subTreeHelper(root, sub):
    if root is None or sub is None:
        return True 

    if root.val != sub.val:
        print("Not a Subtree!")
        return False 

    return subTreeHelper(root.left, sub.left) and subTreeHelper(root.right, sub.right)

def isSubtree(root, sub):
    if root is None:
        return False  
    
    if root.val == sub.val:
        return subTreeHelper(root, sub)

    return isSubtree(root.left, sub) or isSubtree(root.right, sub)


# send down --> my value 
# if leaf comes --> send up the currentSum 
def MaxPathSum(root, currSum = 0):
    if root is None:
        return 0

    currSum += root.val 

    if root.left is None and root.right is None:
        print("At leaf: ", currSum)
        return currSum

    return max(MaxPathSum(root.left, currSum), MaxPathSum(root.right, currSum))


# How do we use stacks to do an inorder traversal 
# We keep appending left nodes into the stack till we hit NULL 
# When we hit NULL, we pop the last element from the stack, and go to it's right 
# If we are at leaf node, the right will be null again, so we will pop another from the list **Imp** 
# We repeat the process till our stack gets empty 
def iterativeInorder(root):
    curr = root 
    stack = []

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left 

        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right 


def bstInsert(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = bstInsert(root.left, val)
    elif val > root.val:
        root.right = bstInsert(root.right, val)

    return root 

# Main Function 
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.right.right = Node(8)
root.left.right = Node(1)
root.right.left = Node(6)


# BST 
# root2 = Node(8)
# root2.left = Node(3)
# root2.right = Node(10)
# root2.right.right = Node(14)
# root2.left.left = Node(1)
# root2.left.right = Node(6)

# print(inorder(root))
# print(minValueinTree(root))
# print(treeHeight(root))
# print(kClose(root, 9))
# print(levelOrder_Recursive(root))
# print(levelOrder_Iterative(root))
# print(invertTree(root))
# print(diameterTree(root))
# print(validateBST(root))
# print(validateBST(root2))
# print(isHeightBalanced(root))
# flattenTree(root)
# print(isSubtree(root, sub)) --> create new tree for sub to run 
# print(MaxPathSum(root)) 
# print(iterativeInorder(root))           # need to revise 




