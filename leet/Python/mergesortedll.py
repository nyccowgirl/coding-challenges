"""
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the 
first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Option 1 - iterative:
        head = tail = ListNode()
        
        # while both linked lists have nodes to traverse, compare the values
        # and add smaller value to tail, moving to the next node in the
        # respective list
        while l1 and l2:
            if l1.val <= l2.val:
                # tail.next = ListNode(l1.val)
                # tacking on entire list seems to run faster than creating
                # new node
                tail.next = l1      
                l1 = l1.next
            else:
                # tail.next = ListNode(l2.val)
                tail.next = l2
                l2 = l2.next
            
            # update tail
            tail = tail.next
            
        # add remaining list to end of tail
        tail.next = l1 or l2
        
        return head.next
        
#         # Option 2 - recursive:
#         # if it is not the end of either linked list
#         if l1 and l2:
#             # return the smaller of the two nodes and continue traversing to
#             # next node in the respective list
#             if l1.val < l2.val:
#                 return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
#             else:
#                 return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))
        
#         # return remaining list which has not reached the end
#         return l1 or l2