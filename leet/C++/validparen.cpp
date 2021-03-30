/*
Given a string s containing just the characters '(', ')', '{', 
'}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/


class Solution {
    public boolean isValid(String s) {
        // can use Stack but ArrayDeque is faster
        Deque<Character> stack = new ArrayDeque<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                
                char current = stack.pop();
                
                switch (current) {
                    case '(' :
                        if (c != ')') {
                            return false;
                        }
                        break;
                    case '[' :
                        if (c != ']') {
                            return false;
                        }
                        break;
                    case '{' :
                        if (c != '}') {
                            return false;
                        }
                        break;
                }   
            }
        }
        // if stack is not empty, then it is unbalanced  
        return stack.isEmpty();
    }
}