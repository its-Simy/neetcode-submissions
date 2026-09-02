class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        

        output = []
        visit, cycle = set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for item in prereq[crs]:
                if not dfs(item):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for item in range(numCourses):
            if dfs(item) == False:
                return []
        return output

                
            
