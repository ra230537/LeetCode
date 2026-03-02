class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        for idx, value in enumerate(intervals):
            cur_start = value.start
            cur_end = value.end
            if (idx < len(intervals) - 1):
                next_start = intervals[idx+1].start
                next_end = intervals[idx+1].end
                if(cur_end > next_start):
                    return True
        return False

print(Solution().canAttendMeetings( [(0,30),(5,10),(15,20)]))
#  [(0,30),(5,10),(15,20)]
# Ordenar, verificar se há interseção