# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max=float('-inf')
        def dfs(node):
            if not node:
                return 0 # base condition 
            # calculate left and right contributions
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            # calculate through 
            through=left+node.val+right 
            self.global_max=max(self.global_max,through)
            # calculate up
            up=node.val+max(left,right)
            return up
        dfs(root)
        return self.global_max
        
        