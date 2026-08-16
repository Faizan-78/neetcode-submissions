class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        n = len(height)
        r = n - 1
        ans = 0
        while l < r:
            area = min(height[l],height[r])*(r-l)
            ans = max(ans,area)
            if height[l] < height[r]:
              l += 1
            else:
              r -= 1
        return ans