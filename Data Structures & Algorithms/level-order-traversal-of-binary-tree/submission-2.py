class Solution:
    def levelOrder(self, root):
       dq = deque([root])
       res = []
       if not root:
        return res
       while dq:
        curr = []
        for _ in range(len(dq)):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            curr.append(node.val)
        res.append(curr)
       return res