class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minV = prices[0]

        for price in prices:
            minV = min(price, minV)
            res = max(res, price - minV)
        
        return res
