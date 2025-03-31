from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []

        res = []
        count = 0
        max_val = nums[0]

        # Initialize the sliding window
        for i in range(1, k):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                max_val = nums[i]
            else:
                count = 0
                max_val = nums[i]

        if count == k - 1:
            res.append(max_val)
        else:
            res.append(-1)

        # Process the rest of the array
        for i in range(k, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                count += 1
                max_val = nums[i]
            else:
                count = 0
                max_val = nums[i]

            if count >= k - 1:
                res.append(max_val)
            else:
                res.append(-1)

        return res
