class Solution:
    def trap(self, height: List[int]) -> int:
      left = 0
      right = 0
      ans = 0
      for i in range (len(height)):
        left = 0
        right = 0
        for j in range(i + 1):
          left= max(left, height[j])
        
        for j in range(i, len(height)):
          right = max(right, height[j])
      
        water = min(left, right) - height[i]
        ans += water
      return ans