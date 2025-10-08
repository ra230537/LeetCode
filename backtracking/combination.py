from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        array = [i for i in range(1, n + 1)]
        def make_combine(array, k) -> List[List[int]]:
            if k == 1:
                return [[i] for i in array]
            combination = []
            for idx in range(len(array)):
                results = make_combine(array[idx + 1:], k - 1)
                for result in results:
                    combination.append([array[idx]] + result)
            return combination
        return make_combine(array, k)


# assert Solution().combine(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

assert Solution().combine(4, 3) == [[1,2, 3],[1,3, 4],[1,2,4],[2,3, 4]]

assert Solution().combine(1, 1) == [[1]]

