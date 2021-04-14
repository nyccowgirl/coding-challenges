/*
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
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Recursive version
//         if (root == NULL) {
//             return 0;
//         } else {
//             // Recurse through each subtree
//             int left = maxDepth(root->left);
//             int right = maxDepth(root->right);
            
//             // Determine deeper one and add 1 for first level
//             // Option 1:
//             // return (left > right ? left + 1 : right + 1);
                
//             // Option 2:
//             return max(left, right) + 1;
//         }

        return maxDepth(root, 0);
    }
    
private:
    // Option 3 - with helper method:
    int maxDepth(TreeNode* root, int depth) {
        if (root == NULL) {
            return depth;
        }
        
        depth++;
        
        // Option 3a - tad bit less memory:
        return max(maxDepth(root->left, depth), maxDepth(root->right, depth));
        
        // Option 3b:
        // int left = maxDepth(root->left, depth);
        // int right = maxDepth(root->right, depth);
        // return (left > right ? left : right);
    }
};