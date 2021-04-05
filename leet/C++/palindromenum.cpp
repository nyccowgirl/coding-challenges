/*
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
*/


class Solution {
public:
    bool isPalindrome(int x) {
        // Option 1:
//         int temp = x;
//         long reverse = 0;
        
//         if (x < 0 || (x % 10 == 0 && x != 0)) {
//             return false;
//         } else if (x >= 0 && x < 10) {
//             return true;
//         } else {
//             while (temp > 0) {
//                 reverse = (reverse * 10) + (temp % 10);
//                 temp /= 10;
//             }
            
//             return (temp < INT_MIN || x > INT_MAX) ? 
//                 false : x == (int)reverse;
//         }
        
        // Option 2 - similar to option 1 but traverse to 
        // middle and compare
        int reverse = 0;
        
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        } else if (x >= 0 && x < 10) {
            return true;
        } else {
            while (x > reverse) {
                reverse = (reverse * 10) + (x % 10);
                x /= 10;
            }
            
            return x == reverse || x == reverse / 10;
        }   
    }
};