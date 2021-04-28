"""
Given an integer num, repeatedly add all its digits until the 
result has only one digit, and return it. 

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
 
Constraints:
0 <= num <= 231 - 1
"""


class Solution:
    def addDigits(self, num: int) -> int:
        # Loop
        # while (num > 9):
        #     # num = (num // 10) + (num % 10)
        #     num = sum([int(numStr) for numStr in list(str(num))])
        # return num
    
        # Recursion
#         if (num <= 9):
#             return num
        
#         return self.addDigits(sum([int(numStr) for numStr in list(str(num))]))

        # O(1)
        if (num == 0):
            return num
        
        return (9 if num % 9 == 0 else num % 9)