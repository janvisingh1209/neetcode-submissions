# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prevNode=head
        currentNode=head.next
        while currentNode is not None:
            nextNode=currentNode.next
            currentNode.next=prevNode
            #update
            prevNode=currentNode
            currentNode=nextNode
        head.next=None
        head=prevNode
        return head

        #recursive approach
    #    if head is None or head.next is None:
    #       return head 
    #   Newhead=self.reverselist(head.next)
    #    head.next.next=head
    #    head.next=None
    #    return Newhead
            



        