class Solution:
    def canFinish(self, n, prerequisites):
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

        


