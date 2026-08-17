class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        n=len(nums)
        for i in range(n):
            num=target-nums[i]
            if num not in seen:
                seen[nums[i]]=i
            else:
                return [seen[num], i]