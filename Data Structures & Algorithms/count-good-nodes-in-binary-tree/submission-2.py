class Solution:
    def goodNodes(self, root):
        self.res = 1
        self.root = root
        def dfs(root,curmax):
            if not root:
                return
            if root.val >= curmax and root != self.root:
                self.res += 1
                curmax = root.val
            dfs(root.left, curmax)
            dfs(root.right,curmax)
        
        dfs(root,root.val)
        return self.res
