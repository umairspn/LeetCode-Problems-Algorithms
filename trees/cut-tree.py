
# Cut the Tree -- HackerRank 
# https://www.hackerrank.com/challenges/cut-the-tree/problem


'''
Given a tree, a tree cut means cutting an edge and creating two trees. 
For a given tree, find the MIN difference edge. 
Difference of an edge cut is the absolute difference between the sums of all nodes 
 of the two trees created after the edge cut. 

'''

class TreeNode:
  def __init__(self, val):
    self.val = val 
    self.left = None 
    self.right = None 
  
# Returns the sum of the left and right subtrees from a given node including itself 
def treeSum(root):
  if root is None:
    return 0
		
  totalSum = 0
  totalSum += treeSum(root.left) + treeSum(root.right) + root.val 
  return totalSum 


def cutEdgesDifferenceHelper(root, overallSum):
    if root is None:
        return float("inf") 

    # if root.left:
    #     leftSum = cutEdgesDifferenceHelper(treeSum(root.left))

    # if root.right:
    #     rightSum = cutEdgesDifferenceHelper(treeSum(root.right)) 
        
    # return min(abs(overallSum - leftSum), abs(overallSum - rightSum)) 
    leftAbsDiff = float('inf')
    rightAbsDiff = float('inf')

    # Step 3: Calculate the sum of left subtree if it exists
    if root.left:
        leftSum = treeSum(root.left)
        leftAbsDiff = abs(overallSum - 2 * leftSum)
    
    # Step 4: Calculate sum of right subtree
    if root.right:
        rightSum = treeSum(root.right)
        rightAbsDiff = abs((overallSum - 2 * rightSum))

    # Step 5, 6: Calculate abs diff

    # Step 7, 8
    min_edge_cut_on_left_side = cutEdgesDifferenceHelper(root.left, overallSum)
    min_edge_cut_on_right_side = cutEdgesDifferenceHelper(root.right, overallSum)

    # Step 9
    return min(leftAbsDiff, rightAbsDiff, min_edge_cut_on_left_side, min_edge_cut_on_right_side)


# Returns the Absolute Min difference of all possible edge cuts from a given tree 
def cutEdgesDifference(root):
  
  # step 1 
  overallSum = treeSum(root) 	
  
  # step 2 
  return cutEdgesDifferenceHelper(root, overallSum)

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right = TreeNode(12)
    root.right.right = TreeNode(2)
    root.right.left = TreeNode(4)

    print(cutEdgesDifference(root))


# # We are given a root node 
# cutEdgesDifference(root) 


# PsuedoCode Idea 1:
# Step 1: Calculate the sum of entire tree (SUM) 
# Step 2: Go over the tree with the SUM
# 	3: At every single node:
#				find the leftSum (sum of left subtree) 									leftSum
# 			find the rightSum (sum of right subtree) 								rightSum 
# 
# 			find the absDiff of left --> abs(SUM - leftSum) 				absLeft
# 			find the absDiff of right --> abs(SUM - rightSum)				absRight 

#				return min(absLeft, absRight)			








