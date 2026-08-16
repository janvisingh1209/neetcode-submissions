# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in-order traversal method
        self.k=k # global k
        self.ans=None
        def check(node):
            if node is None or self.ans is not None:
                return # if we have found the ans or reached leaf node stop recursion whenever either happens
            check(node.left)
            self.k-=1
            if self.k==0:
                self.ans=node.val
                return
            check(node.right)

        check(root)
        return self.ans
        