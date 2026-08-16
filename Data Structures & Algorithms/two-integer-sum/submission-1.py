class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # n=len(nums)

     #  for i in range (n-1):
       #    for j in range (i+1,n):
         #      if nums[i]+nums[j]==target:
          #      return [i,j]
               

     #  return None

 #solution=Solution()
#print(solution.twoSum([1,2,4,6],6))

        hashmap={}  #initialize a dict to store index-values
        for i,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
        return []

#t.c=o(n)





    