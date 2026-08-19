# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        '''
        left most first, adds from the very beginning, all the way down until the last left leaf node
        iterates back for right leaf nodes,
        '''

        res = []

        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res
        