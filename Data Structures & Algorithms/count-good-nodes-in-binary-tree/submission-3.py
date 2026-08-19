class Solution:
    def goodNodes(self, root):
        def dfs(node,curmax):
            if not node:
                return 0
            res = 1 if node.val >= curmax else 0
            curmax = max(curmax,node.val)
            res += dfs(node.left,curmax)
            res += dfs(node.right,curmax)
            return res
        return dfs(root,root.val)
