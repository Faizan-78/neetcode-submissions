class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l= 0
        ans = 0
        n = len(nums)
        profit = 0
        for r in range(l+1,n):
            if nums[l]>nums[r]:
                l = r
            else:
                ans= nums[r]-nums[l]
                profit = max(profit,ans)
        return profit
        

        