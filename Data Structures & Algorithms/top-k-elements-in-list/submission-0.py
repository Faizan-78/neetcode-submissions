import heapq

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        for num,frequency in freq.items():
            heapq.heappush(heap,(-frequency,num))
        ans = []
        for _ in range(k):
            frequency,num = heapq.heappop(heap)
            ans.append(num)
        return ans