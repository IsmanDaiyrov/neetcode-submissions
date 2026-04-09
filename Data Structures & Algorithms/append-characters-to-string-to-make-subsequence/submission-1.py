class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if t[tp] == s[sp]:
                tp += 1
            
            sp += 1
            
        return len(t) - tp