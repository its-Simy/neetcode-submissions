# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        what I'm thinking here is that I make a dfs approach, I compare both the value of both current items, becuase we will parse through both of them in the same way, we will parse through as if we are keeping trakc of levels but not necessary

        we would have both of the trees as the parameters, 
        if one or the other is None:
            make res equal to false
            return 0
        if both are none:
            return 0
        
        otherwise compare values
        then call again the dfs, left and right, and then save the max between them (although not really releveant)


        edgecases:
        one is empty and one isn't
        both empty
        same structure, different values
        different strucure, same values
        '''

        self.res = True
        def dfs(p,q):
            if not q and not p:
                return 0
            elif not q or not p:
                self.res = False
                return 0
            
            if p.val != q.val:
                self.res = False
            
            return max(dfs(p.left,q.left),dfs(p.right,q.right)) + 1
        
        dfs(p,q)
        return self.res
