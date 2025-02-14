class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n= len(nums)
        cur_sum = 0

        # Bulding the window
        for i in range(k):
            cur_sum += nums[i]

        # Doing the maximam avarage
        max_avg = cur_sum/k

        # Slide the Window

        for i in  range(k,n):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]

            avg = cur_sum/k

            max_avg= max(max_avg,avg)

        return max_avg

        