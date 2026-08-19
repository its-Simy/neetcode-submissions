class Solution:
    def cloneGraph(self, node):
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            if not node:
                return
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)
        