class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use a self.max_heap by converting distance to -ve
        self.max_heap=[]
        for x,y in points:
            dist=x*x+y*y
            heapq.heappush(self.max_heap,(-dist,x,y))
            if len(self.max_heap)>k:
                heapq.heappop(self.max_heap)
        return[[x,y] for (_,x,y) in self.max_heap]
        