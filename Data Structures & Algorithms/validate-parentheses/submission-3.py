class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        for p in s:
            if p in pairs:
                stack.append(p)
            else:
                if stack and pairs[stack[-1]] == p:
                    stack.pop()
                else:
                    return False
                    
        return True if not stack else False