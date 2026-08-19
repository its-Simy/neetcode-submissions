class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            self.res = max(self.res, l+r)
            return 1 + max(l,r)       
        dfs(root)
        return self.res