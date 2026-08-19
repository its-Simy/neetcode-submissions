class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       res = []
       stack = []
       visited = set()
       curr = root

       while curr or stack:
            if curr and (curr not in visited):
                stack.append(curr)
                stack.append(curr.right)
                visited.add(curr)
                curr = curr.left
            elif curr and curr in visited:
                res.append(curr.val)
                curr = None
            else:
                curr = stack.pop()

       return res
            


