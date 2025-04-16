class Solution(object):
    def maximumTripletValue(self, nums):
        n = len(nums)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i])
        
        right_max[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        
        maxTriplet = 0
        for j in range(1, n-1):
            current_val = (left_max[j-1] - nums[j]) * right_max[j+1]
            if current_val > maxTriplet:
                maxTriplet = current_val
        
        return max(0, maxTriplet)