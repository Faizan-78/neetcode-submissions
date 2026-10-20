import heapq

class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        pairs = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []
        for x in pairs[:k]:
            result.append(x[0])
        return result
