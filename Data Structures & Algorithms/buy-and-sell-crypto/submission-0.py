class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf')
        profit = 0
        for price in prices:
            minn = min(minn,price)
            profit = max((profit,price - minn))
        return profit