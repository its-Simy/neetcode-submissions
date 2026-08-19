# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        the first thing I notied is that on every level, the last item should be what is appended right since its the right most item, so we just append that to a list that we return

        we could use bfs with this pretty easily acutally

        since we are bascially already oging top to bottom it works out perfectly
        '''

        res = []
        if not root:
            return res
        dq = deque([root])
        while dq:
            node = None
            for i in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(node.val)
            
        return res