class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)  # dictionary to store freq of each letter 
        # initialize a max_heap
        max_heap=[-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time=0
        cooldown=deque()  # queue to store time and freq left
        while max_heap or cooldown:
            time+=1
            if max_heap:
                cnt=heapq.heappop(max_heap)+1
                if cnt!=0:
                    cooldown.append((time+n,cnt))

            if cooldown and cooldown[0][0]==time:
                heapq.heappush(max_heap,cooldown.popleft()[1])
        return time



        