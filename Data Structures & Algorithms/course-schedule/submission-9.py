class Solution:
    def canFinish(self, n, prerequisites):
        '''
        dictionary = [node -> siblings]
        visiting set
        
        dfs current node:
            check if the current node in visiting:
                False
            if the check with dictionary is empty:
                return true

            append this current node to visiting
            traverse through all the sibling nodes of the current node:
                run dfs for those nodes
                if that dfs is false we return false
            we could set that list to []  
            pop current value from visiting
            return true

        we are going to parse through all the number of courses and call the dfs
            if this ever returns false
            will return false

        otherwise always return true
        '''

        dic = {i:[] for i in range(n)}
        for course, pre in prerequisites:
            dic[pre].append(course)

        visiting = set()

        def dfs(cur):
            if cur in visiting:
                return False
            if dic[cur] == []:
                return True
            
            visiting.add(cur)

            for item in dic[cur]:
                if not dfs(item):
                    return False
            dic[cur] = []
            visiting.remove(cur)
            return True

        for item in range(n):
            if not dfs(item):
                return False

        return True

        


