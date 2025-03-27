class Solution:
    def minimumIndex(self, nums):  
        frequency_map, left_count = {}, {}

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        for index in range(len(nums) - 1):
            left_count[nums[index]] = left_count.get(nums[index], 0) + 1
            frequency_map[nums[index]] -= 1

            if left_count[nums[index]] * 2 > (index + 1) and frequency_map[nums[index]] * 2 > (len(nums) - index - 1):
                return index

        return -1
