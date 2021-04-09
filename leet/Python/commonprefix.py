"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        
        # Option 1:
        # if there is just one item in the list or start with 
        # first word to compare
        prefix = strs[0]
        length = len(prefix)
        
        # start at second word in list, if applicable
        for word in strs[1:]:
            while prefix != word[:length]:
                # continue to reduce prefix until it is the same, if applicable
                prefix = prefix[:length - 1]
                length -= 1
                
                # otherwise there is no common prefix
                if length == 0:
                    break

        return prefix
    
#         # Option 2:
#         # set length of smallest word in list, as max length of prefix
#         length = min([len(word) for word in strs])
        
#         for i in range(length):
#             # if all words have same char at specific index, add to prefix
#             if all(word[i] == strs[0][i] for word in strs):
#                 prefix += strs[0][i]
#             else:
#                 break
                
#         return prefix