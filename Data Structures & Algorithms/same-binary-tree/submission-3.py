class Solution:
    def isSameTree(self, p, q):
        self.res = True
        def dfs(p,q):
            if not q and not p:
                return 
            elif not q or not p:
                self.res = False
                return 
            if p.val != q.val:
                self.res = False
            dfs(p.left,q.left)
            dfs(p.right,q.right)
            return
        dfs(p,q)
        return self.res
