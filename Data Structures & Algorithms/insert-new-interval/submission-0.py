class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        ans = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                return ans

            if newInterval[0] > interval[1]:
                ans.append(interval)
            else:
                max_end = max(newInterval[1], interval[1])
                min_start = min(newInterval[0], interval[0])
                newInterval = [min_start, max_end]
        
        ans.append(newInterval)
        return ans
