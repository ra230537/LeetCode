class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        verifier = 0
        for i in nums:
            verifier = verifier ^ i
        return verifier
print(Solution().singleNumber(nums = [1]))