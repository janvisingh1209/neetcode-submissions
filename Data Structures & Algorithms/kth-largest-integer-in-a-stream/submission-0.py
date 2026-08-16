import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.min_heap=[]  # initialize a list and this is treated as a heap using heapq
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val)  # ensures a complete bt is created
        if len(self.min_heap)>self.k:
            heapq.heappop(self.min_heap)  # removes smallest element

        return self.min_heap[0]  #returns first element of min heap
        
