from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Optimized two-pointer approach
        # Time complexity: O(n)
        # Space complexity: O(1)
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
