class Solution:
    def trap(self, height: List[int]) -> int:
      ans = 0
      n = len(height)    
      l = 0
      r = n -1
      left = height[0]
      right = height[n-1]
        
      while l<r:
        left = max(left, height[l])
        right = max(right, height[r])  
        if left < right:
          ans += left - height[l]
          l += 1
        
        else:
          ans += right - height[r]
          r -= 1
      return ans
        