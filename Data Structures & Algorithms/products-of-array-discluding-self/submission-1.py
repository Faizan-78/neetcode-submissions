class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = 1
        right = 1
        leftprod = []
        rightprod = []
        for i in range(len(nums)):
            leftprod.append(left)
            left = left * nums[i]
        for i in range(len(nums)-1,-1,-1):
            rightprod.append(right)
            right = right * nums[i]
        rightprod.reverse()
        for i in range(len(nums)):
            ans.append(leftprod[i] * rightprod[i])
        return ans
        