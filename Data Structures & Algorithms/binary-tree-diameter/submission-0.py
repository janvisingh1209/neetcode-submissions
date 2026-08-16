# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we initialize diameter as 0
        self.diameter=0
        def height(node):
            if not node:
                return 0  # base case for recursion
            left_height=height(node.left)
            right_height=height(node.right)  #calculate height of subtrees
            self.diameter=max(self.diameter,left_height+right_height)

            return 1+max(left_height,right_height)
        height(root) #recursive call
        return self.diameter





       

        