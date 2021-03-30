"""
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
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                # pop out last item in stack
                current = stack.pop()
                
                if current == "(":
                    if c != ")":
                        return False
                
                if current == "[":
                    if c != "]":
                        return False
                    
                if current == "{":
                    if c != "}":
                        return False
                   
        # if stack is not empty, then it is unbalanced
        if stack:
            return False
        
        return True