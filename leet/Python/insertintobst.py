"""
You are given the root node of a binary search tree (BST) and a 
value to insert into the tree. Return the root node of the BST 
after the insertion. It is guaranteed that the new value does 
not exist in the original BST.

Notice that there may exist multiple valid ways for the 
insertion, as long as the tree remains a BST after insertion. 
You can return any of them. 

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:
The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        # Iteration
        curr = root
        
        while curr:
            if (val < curr.val):
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    curr = None
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    curr = None

        # Stack
#         s = []
#         s.append(root)
        
#         while len(s) > 0:
#             curr = s.pop()
            
#             if (val < curr.val):
#                 if (curr.left):
#                     s.append(curr.left)
#                 else:
#                     curr.left = TreeNode(val)
#             else:
#                 if (curr.right):
#                     s.append(curr.right)
#                 else:
#                     curr.right = TreeNode(val)

        # Recursion
        # if (val < root.val):
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)
        
        return root