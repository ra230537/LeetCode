def twoSum(nums: list[int], target: int) -> list[int]:
    sorted_nums = sorted(nums, reverse=True)
    start_idx = 0
    end_idx = len(nums) - 1
    value_a = -1
    value_b = -1
    idx_a = -1
    idx_b = -1
    while (start_idx < end_idx):
        response = sorted_nums[start_idx] + sorted_nums[end_idx]
        if (response < target):
            end_idx -= 1
        elif (response > target):
            start_idx +=1
        else:
            value_a = sorted_nums[start_idx]
            value_b = sorted_nums[end_idx]
            break
    for idx, value in enumerate(nums):
        if (value == value_a and idx_a == -1):
            idx_a = idx
        elif(value == value_b and idx_b == -1):
            idx_b = idx
    return [idx_a, idx_b]


print(twoSum(nums = [3,3], target = 6))