class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""
        from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if not strs:
            return result
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:  
                    return result
            result += strs[0][i]
        
        return result

        
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:  
                    return result
            result += strs[0][i]
        
        return result
