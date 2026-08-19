class Solution:
    def isSameTree(self, p, q):
        self.res = True
        def dfs(p,q):
            if not q and not p:
                return 0
            elif not q or not p:
                self.res = False
                return 0
            if p.val != q.val:
                self.res = False

            return dfs(p.left,q.left)+dfs(p.right,q.right)
        
        dfs(p,q)
        return self.res
