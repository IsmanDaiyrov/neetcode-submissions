class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        res = 0

        for n in arr:
            if n + 1 in hash_set:
                res += 1
        
        return res