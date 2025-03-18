from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the characters at left and right indices
            s[left], s[right] = s[right], s[left]
            
            # Move towards the center
            left += 1
            right -= 1
