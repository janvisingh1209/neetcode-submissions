class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.min_heap=[]# initialize a min_heap
        self.k=k
        for num in nums:
            heapq.heappush(self.min_heap,num)
            if len(self.min_heap)>self.k:
                heapq.heappop(self.min_heap)  # pop the smallest element, given by root
        return self.min_heap[0]
        
        