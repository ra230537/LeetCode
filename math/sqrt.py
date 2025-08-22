class Solution:
    def mySqrt(self, x: int) -> int:
        ceil = x
        floor = 0
        value = (ceil + floor) // 2
        while floor <= ceil:
            if (value * value > x):
                ceil = value - 1
            else:
                floor = value + 1
            value = (ceil + floor) // 2
        return value * 2 // 2
print(Solution().mySqrt(0))