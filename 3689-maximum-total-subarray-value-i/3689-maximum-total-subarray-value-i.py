class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        ans = 0
        value = max(nums) - min(nums)

        for i in range(k):
            ans += value

        return ans