from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()
        ans = []
        n = len(nums)

        for r in range(n):

            # 1. Window se bahar wale index hatao
            while dq and dq[0] < r - k + 1:
                dq.popleft()

            # 2. Back se chhote elements hatao
            while dq and nums[dq[-1]] <= nums[r]:
                dq.pop()

            # 3. Current index add karo
            dq.append(r)

            # 4. Window complete hone par max add karo
            if r >= k - 1:
                ans.append(nums[dq[0]])

        return ans