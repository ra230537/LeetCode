class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for idx in range(len(digits)-1,-1,-1):
            val = digits[idx]
            if (val+1 == 10):
                digits[idx] = 0
                if(idx == 0):
                    digits.insert(0, 1)
            else:
                digits[idx]+=1
                break
        return digits
print(Solution().plusOne(digits = [1,9,9]))