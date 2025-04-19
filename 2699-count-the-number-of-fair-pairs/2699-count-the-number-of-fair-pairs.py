from bisect import bisect_left, bisect_right

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        n = len(nums)
        
        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1)
            ans += (right - left)
        
        return ans
