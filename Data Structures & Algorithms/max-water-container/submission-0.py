class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        for i in range(n):
         for j in range(i+1, n):
          area = min(heights[i], heights[j]) * (j-i)
          ans = max(ans, area)
        return ans