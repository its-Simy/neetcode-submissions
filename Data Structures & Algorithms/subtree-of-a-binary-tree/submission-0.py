# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            we basically parse through until we find the subroot,
            once we find the subroot, we activate is same method, we could do this with a mix of bfs and dfs if we wanted to


            bfs to search, dfs to compare

            have a res attribute to see if its the same or not, we are going to try and find out if first it was found then if it were the same.

            keep track of found vairable -> False
            keep track of same variable -> True

            dfs method (root, subroot):

                if both don't exist:
                    return 
                if one exists but the other doesn't OR values aren't the same:
                    change res
                    return 

                return calling left child and right child for root and subroot
                


            bfs here but for the root

            declare dq

            while dq exists:
                first pop the leftmost node

                if the leftmode node is subroot, 
                change found variable
                call the dfs method with current variable & subroot
                break out of method

            return res if found else: false
        '''
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
            else:
                return False

        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.val == subRoot.val:
                if isSameTree(node,subRoot):
                    return True
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return False
        