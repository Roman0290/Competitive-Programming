class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        def is_common_prefix(length):
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        left, right = 0, len(min(strs, key=len))
        while left < right:
            mid = (left + right + 1) // 2
            if is_common_prefix(mid):
                left = mid
            else:
                right = mid - 1

        return strs[0][:left]