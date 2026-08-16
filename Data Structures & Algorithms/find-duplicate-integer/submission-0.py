class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]   #move one step
            fast=nums[nums[fast]]

            if slow==fast:   #meets inside the loop
                break

        slow=nums[0]  # slow begins from start or head
        while slow!=fast:
            slow=nums[slow] #move one step
            fast=nums[fast] #move one step

        return slow

        