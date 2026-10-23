
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Method 1: Min Heap
        freq = {}

        # Step 1: Count frequency of each element
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # Step 2: Maintain a heap of size k
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract the top k elements
        result = []
        for x in heap:
            result.append(x[1])

        return result

        # Method 2: Sorting (Alternative)
        # freq = {}
        #
        # for x in nums:
        #     freq[x] = freq.get(x, 0) + 1
        #
        # pairs = sorted(
        #     freq.items(),
        #     key=lambda x: x[1],
        #     reverse=True
        # )
        #
        # result = []
        # for x in pairs[:k]:
        #     result.append(x[0])
        #
        # return result
