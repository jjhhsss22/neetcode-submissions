class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x : x[0])
        first_interval = sorted_intervals[0]
        ans = [first_interval]

        for i in range(1, len(sorted_intervals)):
            current_interval = sorted_intervals[i]

            if ans[-1][1] >= current_interval[0]:
                min_start = ans[-1][0]
                max_end = max(ans[-1][1], current_interval[1])

                ans[-1] = [min_start, max_end]
                continue

            ans.append([current_interval[0], current_interval[1]])

        return ans