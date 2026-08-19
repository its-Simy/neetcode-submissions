class Solution:
    def diameterOfBinaryTree(self, root):
        '''
            this would basically be, greatest right + left subtrees

            I would need to make a helper method here to do the dfs

            I would only store the root in that dfs

            then call it

            in there we would basically we want the max levels of( dfs(left) + dfs(right)), that should be the answer


            we know that to get that answer we must know how to keep track of the levels right so


            base case is that if theres no children return 0

            otherwise call the max between left + right children + 1

            [1,null,2,3,4,5]



            1
            max(dfs(left) + dfs(right) + 1)

            dfsleft(none) -> 0
            dfsright(2) -> max(dfs(left) + dfs(right) + 1) -> left = 2 + 1 + 1 = 4

            left -> 3 + 1 -> max(dfs(left) + dfs(right) + 1) -> left + 1

            right = dfs(right) + 1 = 1


        '''
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            res = max(res, l+r)
            return 1 + max(l,r)       

        dfs(root)
        return res