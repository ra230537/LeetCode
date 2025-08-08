class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        next_pos = len(nums1)-1
        while (i >= 0 and j >= 0):
            if (nums1[i] <= nums2[j]):
                nums1[next_pos] = nums2[j]
                next_pos-=1
                j-=1
            else:
                nums1[next_pos] = nums1[i]
                next_pos-=1
                i-=1
        if (i <= 0):
            # feito porque eu preciso pegar até o indice atual e não um anterior a ele
            for k in range(j+1):
                nums1[k] = nums2[k]
        return nums1
print(Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0))