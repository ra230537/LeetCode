def main(nums: list[int], k:int):
    list_size = len(nums)
    current_index = 0
    next_index = (current_index + k) % list_size
    next_value = nums[next_index]
    while list_size > 0:
        nums[next_index] = next_value
        next_index = (current_index + k) % list_size
        next_value = nums[next_index]
        list_size-=1
    return nums

print(main([1,2,3,4,5,6,7], 3))