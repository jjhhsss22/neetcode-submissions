class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        clear = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in clear:
                return True


            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            clear.add(crs)
            
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True