class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            ans = max(freq, key = freq.get)
        return ans
