/*
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
*/


class Solution {
public:
    string multiply(string num1, string num2) {
        int x = num1.length(), y = num2.length();
        vector<int> result(x + y);  // To account for carryovers
        
        // Start from back of each string
        for (int i = x - 1; i >= 0; i--) {  
            for (int j = y - 1; j >= 0; j--) {
                int prod = (num1.at(i) - '0') * 
                (num2.at(j) - '0');
                // Determine array position for carryover and 
                // remainder
                int p1 = i + j;             // Carryover
                int p2 = p1 + 1;            // Remainder
                // Add product with prior carryover, if any
                int sum = prod + result[p2];
                // Update values in result array for carryover 
                // and remainder with carryover being added to 
                // previous value
                result[p1] += sum / 10;
                result[p2] = sum % 10;     
            }
        }
        
        // To convert to string removing any leading zeros
        string str;
      
        for (int value : result) {
            if (!(value == 0 && str.length() == 0)) {
                str += to_string(value);
            }
        }  
        
        return str.length() == 0 ? "0" : str;
    }
};