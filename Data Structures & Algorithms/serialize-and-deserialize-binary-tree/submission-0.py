# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # use preorder traversal to serialize and deserialize, root,left,right
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result=[]# list to store elements/nodes
        def dfs(node):
            if node is None:
                result.append('#')
                return # stop traversing the path once leaf node is hit
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return','.join(result)  # converts the list of individual strings into a one string separated by commas bcz strings are easy to transport over a network

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # convert the string back into a list of nodes
        values=iter(data.split(','))  #convert it back into a list
        def dfs():
            val=next(values)  # stores next value in the list
            if val=='#':
                return None
            node=TreeNode(int(val))  # convert val into a node
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

            







