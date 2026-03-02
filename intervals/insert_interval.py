from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        response = []
        inserted = 0
        for idx, value in enumerate(intervals):
            new_start = newInterval[0]
            new_end = newInterval[1]
            cur_start = value[0]
            cur_end = value[1]
            if (cur_end < new_start):
                response.append(value)
            elif(new_end < cur_start):
                if (inserted == 0):
                    response.append(newInterval)
                    inserted = 1
                response.append(value)
            else:
                newInterval = [min(new_start, cur_start),max(new_end, cur_end)]
        if (not inserted):
            response.append(newInterval)
        # print(newInterval)
        return response
print(Solution().insert(intervals = [[1,2],[7,8],[9,11]], newInterval = [1, 4]))
        

'''
[a,b],[c,d],[e,f],[g,h],[i,j]

[x,y]

x > f
y > g

[a,b],[c,d],[e,h],[i,j]
'''