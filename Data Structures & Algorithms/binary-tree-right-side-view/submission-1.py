# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we have to apply bfs, we will initialize a queue and we will append the last value at every level
        result=[]
        queue=deque([root])
        if root is None:
            return []

        while queue:
            level_len=len(queue)
           # level=[]  #skippable
            for i in range(level_len):
                node=queue.popleft()
                if i==level_len-1:
                    result.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result



        