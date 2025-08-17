# array sorted in non-decreasing order: nums
# ordenar os elementos na ordem atual de forma que os primeiro k sejam unicos, o resto não é importante (reordenação)
# retornar k

# temos dois ponteiros, um i e um k e o k representa onde será a próxima posição do numero que é diferente
def main(nums: list[int]):
    k = 1
    for i in range(len(nums)-1):
        current_value = nums[i]
        next_value = nums[i+1]
        if (current_value != next_value):
            nums[k] = next_value
            k+=1

    return k


if __name__ == '__main__':
    main([1,1, 2])