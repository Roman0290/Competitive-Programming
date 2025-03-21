class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        
        for i in range(left, right + 1):
            isPresent = False
            for j in range(len(ranges)):
                if i >= ranges[j][0] and i <= ranges[j][1]:
                    isPresent = True
                
            if not isPresent:
                return False
        
        return isPresent