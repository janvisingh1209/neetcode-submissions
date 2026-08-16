class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)           # Create dummy before head
        groupPrev = dummy                   # Pointer to node before group

        while True:
            kth = self.getKthNode(groupPrev, k)  # Find kth node ahead
            if not kth:                          # Less than k nodes left
                break

            groupNext = kth.next                 # Save start of next group

            # Reverse nodes inside this group
            prev, curr = groupNext, groupPrev.next
            for _ in range(k):                   # Reverse exactly k nodes
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect reversed group with previous part
            temp = groupPrev.next                # Old head (now tail)
            groupPrev.next = kth                 # Connect to new head
            groupPrev = temp                     # Move to tail of group

        return dummy.next                        # Return new head

    # Helper: find kth node from current node
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr                              # None if not enough nodes

        