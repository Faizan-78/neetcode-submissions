class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] == 1:
                count += 1
                ans = max(ans,count)
            else:
                count = 0
        return ans