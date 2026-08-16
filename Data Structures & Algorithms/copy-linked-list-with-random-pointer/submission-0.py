"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #intervweave dummy nodes between real nodes
        if not head:
            return None
        current=head
        while current:
            newNode=Node(current.val)
            newNode.next=current.next
            current.next=newNode
            current= newNode.next
        # now add random to these nodes
        current=head
        while current:
            if current.random:
                current.next.random=current.random.next # attach duplicate random 
            current=current.next.next

        current=head
        copyhead=head.next
        
        while current:
            copy=current.next
            current.next=copy.next   # restore original
            if copy.next:
                copy.next=copy.next.next
            current=current.next
        return copyhead









