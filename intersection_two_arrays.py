'''
ordena o array 1, 2

 9
enquanto os dois indices forem menores que o tamanho do array
se os dois forem diferentes, ve qual é o menor e aumenta um idx
se os dois forem iguais, aumenta o idx dos dois

'''

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    i = 0
    j = 0
    nums1.sort()
    nums2.sort()
    response = []
    while (i < len(nums1) and j < len(nums2)):
        if (nums1[i] == nums2[j]):
            response.append(nums1[i])
            i += 1
            j += 1
        elif(nums1[i] < nums2[j]):
            i +=1
        else:
            j += 1
    return response

print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))

'''
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
eu precisaria fazer o algoritmo em O(n^2) e ir removendo os numeros de 2, para que não fossem contabilizados duas vezes

'''