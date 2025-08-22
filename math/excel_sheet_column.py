class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count = 0
        size = len(columnTitle)
        for idx_letter in range(size):
            power = size - idx_letter - 1
            letter_value = ord(columnTitle[idx_letter]) - ord('A') + 1
            count += 26**(power) * letter_value
        return count

print(Solution().titleToNumber("ZY"))