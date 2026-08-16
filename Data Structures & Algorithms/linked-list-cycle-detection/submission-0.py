# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next   #move one step
            fast=fast.next.next  #move two steps
            if slow==fast:  #loop detected
                return True
        return False

        #t.c=o(n)
       # s.c=o(n)
       
        