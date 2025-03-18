class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]  # Return the indices (1-based) of the two elements
            elif total < target:
                l += 1
            else:
                r -= 1

        return []  # No solution found