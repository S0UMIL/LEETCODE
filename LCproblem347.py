class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new = defaultdict(int)

        for num in nums:
            new[num] += 1

        heap = []
        for num, count in new.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
