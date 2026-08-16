import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap=[-s for s in stones] # create a list that converts all s values to -1
        heapq.heapify(self.max_heap) # convert it into a min_heap

        while len(self.max_heap)>1:
            y=-heapq.heappop(self.max_heap)
            x=-heapq.heappop(self.max_heap)

            if y!=x:
                heapq.heappush(self.max_heap,-(y-x))
        return -self.max_heap[0] if self.max_heap else 0
        