class MedianFinder:

    def __init__(self):
        self.max_heap=[] # tracks all the smaller elements
        self.min_heap=[]  # tracks all the larger elements than the median
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        # check val invariant
        if self.min_heap and (-self.max_heap[0]>self.min_heap[0]):
            val=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)
        # check len invariant
        if len(self.min_heap)>len(self.max_heap):
            val=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)
        # check len invariant
        if len(self.max_heap)>len(self.min_heap)+1:
            val=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,val)
            
              

    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap):
            return (-self.max_heap[0]+self.min_heap[0])/2
        return -self.max_heap[0]

        
        



        
        