from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))
        number=0
        prev_end = -50001
        for idx, value in enumerate(intervals):
            start = value[0]
            end = value[1]
                
            if start < prev_end:
                number+=1
                prev_end = min(end, prev_end)
            else:
                prev_end = end

        return number
print(Solution().eraseOverlapIntervals([[1, 10], [2, 5], [6, 8], [9, 10]]))