class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            # if window condition is broken, shift l pointer
            # window length - max freq of the character from the map = number of required replacements
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # update the res
            res = max(res, r - l + 1)
        
        return res