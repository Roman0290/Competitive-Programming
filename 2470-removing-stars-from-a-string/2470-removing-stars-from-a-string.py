class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in s:
            if i == "*":
                if res:
                    res.pop()
            else:
                res.append(i)
        return ''.join(res)
