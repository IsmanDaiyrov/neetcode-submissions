class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_res = 0

        while r < len(prices):
            max_res = max(max_res, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r

            r += 1

        return max_res