

class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        # o(n) tc
        seen=set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

       # o(nlogn)=tc
      #  n=len(nums) 
       # nums.sort()  
        
     
       # for i in range(n-1):
         #   if nums[i]==nums[i+1]:
         #       return True
            
        #return False




