import heapq


class KthLargest:
    def getKthLargest(self, nums, k: int) -> int:
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)

        for _ in range(k):
            heapq.heappop(heap)

        return -heap.heappop(heap)

    def findKthLargest(self, nums, k: int) -> int:
        return sorted(nums, reverse=True)[K-1]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
instance = KthLargest()
instance.getKthLargest(nums, 3)
