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
    public String multiply(String num1, String num2) {
        int x = num1.length(), y = num2.length();
        // To account for carryovers
        int[] result = new int[x + y];
        
        // Start from back of each string
        for (int i = x - 1; i >= 0; i--) {  
            for (int j = y - 1; j >= 0; j--) {
                int prod = (num1.charAt(i) - '0') * 
                (num2.charAt(j) - '0');
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
        StringBuilder str = new StringBuilder("");
      
        for (int value : result) {
            if (!(value == 0 && str.length() == 0)) {
                str.append(value);
            }
        }  
        
        return str.length() == 0 ? "0" : str.toString();
        
        // Using dropWhile
        // return (result.length == 2 && result[1] == 0) ? "0" : Arrays.stream(result).dropWhile(i -> i == 0).collect(StringBuilder::new, StringBuilder::append, (l, r) -> l.append(r)).toString();        
    }
}