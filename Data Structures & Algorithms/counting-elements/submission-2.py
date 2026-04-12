class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_map = Counter(arr)
        res = 0

        for n in arr:
            if n + 1 in arr_map:
                res += 1
        
        return res