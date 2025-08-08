def main(nums: list[int], k:int):
    list_size = len(nums)
    start_index = 0
    current_index = start_index
    current_value = nums[current_index]
    next_index = (current_index + k) % list_size
    next_value = nums[next_index]
    for i in range(len(nums)):
        nums[next_index] = current_value
        current_value = next_value
        current_index = next_index
        next_index = (next_index + k) % list_size
        next_value = nums[next_index]
        if (current_index == start_index and start_index < list_size-1):
            start_index+=1
            current_index = start_index
            current_value = nums[current_index]
            next_index = (current_index + k) % list_size
            next_value = nums[next_index]
    return nums

print(main([-1,-100,3,99], k = 2))