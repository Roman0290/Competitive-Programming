class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        if any(num < k for num in nums):
            return -1
        greater_than_k = {num for num in nums if num > k}
    
        return len(greater_than_k) 