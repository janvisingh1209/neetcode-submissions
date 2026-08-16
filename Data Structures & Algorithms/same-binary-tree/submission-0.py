# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #and because both conditions must be true
        if p is None and q is None:
            return True
            #if even one of the values are none but the other one isn't then false
        if p is None or q is None:
            return False
        if p.val!=q.val:
            return False

        return (self.isSameTree(p.left,q.left) and
               self.isSameTree (p.right,q.right))
               #bcz both condns must be true
        