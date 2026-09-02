class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)
            for item in preMap[crs]:
                if not dfs(item):
                    return False
            seen.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True