"""
Given a signed 32-bit integer x, return x with its digits 
reversed. If reversing x causes the value to go outside the 
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit 
integers (signed or unsigned). 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        min = -2 ** 31
        max = ((2 ** 31) -1)
        
        # Option 1
#         temp = 0
        
#         while (abs(x) > 0):
#             # note: modulus and floor division operators work 
#             # different for negative numbers in python than 
#             # java/c++ 
#             temp = (temp * 10) + int((math.fmod(x, 10)))
#             x = int(x / 10)
            
        # Option 2
        temp = (-int(str(x)[:0:-1]) if x < 0 else int(str(x)[::-1]))
        
        return (0 if (temp < min or temp > max) else temp)
    