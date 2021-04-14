"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node. 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Recursive version
        if not root:
            return 0
        else:
            # Recurse through each subtree
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
            # Determine deeper one and add 1 for first level
            # Option 1 - seems to be quicker runtime:
            return (left + 1 if left > right else right + 1)
        
            # Option 2:
            # return max(left, right) + 1
            
        # Option 3 - with helper method:
#             def maxDepth(root, depth):
#                 if not root:
#                     return depth
#                 depth += 1
#                 # Option 3a - more memory, similar runtime as option 1:
#                 # return max(maxDepth(root.left, depth), maxDepth(root.right, depth)) 
                
#                 # Option 3b - less memory as option 3a; similar runtime as option 2:
#                 left = maxDepth(root.left, depth)
#                 right = maxDepth(root.right, depth)
#                 return left if left > right else right 

#             return maxDepth(root, 0)