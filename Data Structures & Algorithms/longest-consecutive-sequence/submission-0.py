class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums_arr=set(nums)  #takes o(1) time which is independent of size using it as a list would have been of o(n) complexity
         
        longest=0 #length of seq
        for num in nums_arr:
            if num-1 not in nums_arr:
                current=num
                streak=1  #length of seq

                while current+1 in nums_arr:
                    current+=1
                    streak+=1
                longest=max(longest,streak)
        return longest
