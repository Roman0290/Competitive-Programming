class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i].isalnum():  
                stack.append(s[i])
            elif s[i] == "*":  
                if stack:
                    stack.pop()
        return ''.join(stack)  
