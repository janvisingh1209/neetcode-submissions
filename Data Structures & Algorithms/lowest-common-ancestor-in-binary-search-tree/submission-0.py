# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursive approach
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

        # using recusrion we dont have to manually update curr at each step

        # approach 2
       # curr=root
       # while curr:
       # if p.val<curr.val and q.val<curr.val:
       #     curr=curr.left
       # elif p.val>curr.val and q.val>curr.val:
       #    curr=curr.right
       # else:
       #     return curr
       # here we dont have to consider complexity of call stack which will be equal to o(h)

        