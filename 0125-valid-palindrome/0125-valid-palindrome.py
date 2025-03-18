class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isItAlphanum(s[l]):
                l += 1
            while r > l and not self.isItAlphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isItAlphanum(self, c):
        return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')