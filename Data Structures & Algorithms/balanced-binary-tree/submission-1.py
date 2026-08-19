# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res = True
        
        #This calculates but from the root, now fix for every level

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            print("LEfT: ",l)
            print("right:",r)
            if abs(l - r) > 1:
                self.res = False

            return max(l,r) + 1
            
        dfs(root)
        return self.res