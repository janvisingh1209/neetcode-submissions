# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return None
        #find mid
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            #slow points toward the middle element now

        #reverse the second half
        prev=None
        current=slow.next
        slow.next=None   #breaking connection
        while current:
            nextnode=current.next
            current.next=prev
            #update
            prev=current
            current=nextnode  
            #now prev is head of reversed list


        #merging
        first=head
        second=prev
        
        while second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2



#o(n)
        