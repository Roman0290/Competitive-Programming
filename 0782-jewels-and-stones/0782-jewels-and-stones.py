class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        counter = 0
        for stone in stones:
            if stone in s:
                counter += 1


        return counter
        