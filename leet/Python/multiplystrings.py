"""
Given two non-negative integers num1 and num2 represented as 
strings, return the product of num1 and num2, also represented 
as a string.

Note: You must not use any built-in BigInteger library or 
convert the inputs to integer directly. 

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 
Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the 
number 0 itself.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Option 1 - faster version:
        i, j, base1, base2, len1, len2 = 0, 0, 0, 0, len(num1), len(num2)
        
        while (i < len1):
            base1 = base1 * 10 + (ord(num1[i]) - ord('0'))
            i += 1
            
        while (j < len2):
            base2 = base2 * 10 + (ord(num2[j]) - ord('0'))
            j += 1
            
        return str(base1 * base2)
    
#         # Option 2 (equivalent to Java and C++ implementations) - slower version:
#         x, y = len(num1), len(num2);
#         result = [0] * (x + y);            # To account for carryovers
        
#         # Start from back of each string
#         for i, value1 in reversed(list(enumerate(num1))): 
#             for j, value2 in reversed(list(enumerate(num2))):
#                 prod = (ord(value1) - ord('0')) * (ord(value2) - ord('0'));
#                 # Determine array position for carryover and remainder
#                 p1 = i + j;                 # Carryover
#                 p2 = p1 + 1;                # Remainder
#                 # Add product with prior carryover, if any
#                 sum = prod + result[p2];
#                 # Update values in result array for carryover and remainder with
#                 # carryover being added to previous value
#                 result[p1] += sum // 10
#                 result[p2] = sum % 10
                
#         string = ""
#         for value in result:
#             if not (value == 0 and len(string) == 0):
#                 string += str(value)

                
#         return "0" if len(string) == 0 else string