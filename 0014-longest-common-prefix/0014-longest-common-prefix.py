class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first, last = min(strs), max(strs)

        for i, char in enumerate(first):
            if i >= len(last) or char != last[i]:
                return first[:i]

        return first