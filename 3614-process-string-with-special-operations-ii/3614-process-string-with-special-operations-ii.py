class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0
        lengths = []  
        
        for char in s:
            lengths.append(length)
            if char == '*':
                length = max(0, length - 1)
            elif char == '#':
                length = length * 2
            elif char == '%':
                pass  
            else:
                length += 1
        
        if k < 0 or k >= length:
            return "."
        target = k
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            prev_len = lengths[i] 
            
            if char == '*':
                pass  
            elif char == '#':
                target = target % prev_len
            elif char == '%':
                target = prev_len - 1 - target
            else:
                if target == prev_len:
                    return char
               
        return "."