from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        hmap={ ')':'(', '}':'{', ']':'[' }
        stk=[]
        
        for c in s:
            if c not in hmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hmap[c]:
                        return False
        return not stk


    

        