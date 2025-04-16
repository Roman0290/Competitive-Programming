class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = { '}':'{',']':'[', ')':'('}
        stack = []

        for char in s:
            if char not in hash_map:
                stack.append(char)

            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hash_map[char]:
                        return False
        return not stack

            