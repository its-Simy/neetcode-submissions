class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       '''
        we should be able to solve this using bfs


        we would save a res list
        curr list

        we append all of the specific layers, we do that using a for loop, so we could actually just go through the deque itself and append it as a list




       '''
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

        