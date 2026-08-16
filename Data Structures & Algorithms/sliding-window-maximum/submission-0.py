class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums or k==0:
            return []

        result =[]
        dq=deque()

        # now remove index that is out of bounds
        for i in range(len(nums)):
            # remove out of bound index
            while dq and dq[0]<i-k+1:
                dq.popleft()
                # compare element in last of dequewith the current element
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)

            if i>=k-1:
                result.append(nums[dq[0]])
        return result 

              


