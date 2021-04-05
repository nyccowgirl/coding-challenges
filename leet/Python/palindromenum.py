"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as 
forward. For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to 
left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a 
palindrome.

Example 4:
Input: x = -101
Output: false
 
Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to 
a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Option 1:
        # return str(x) == str(x)[::-1]
    
        # Option 2 - without converting to string:
        temp = x
        reverse = 0
        
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        elif x >= 0 and x < 10:
            return True
        else:
            while (temp > 0):
                # note: modulus and floor division operators work 
                # different for negative numbers in python than 
                # java/c++, but since we have eliminated negatives
                # above, it should work the same.
                reverse = (reverse * 10) + (temp % 10)
                temp //= 10

            return x == reverse