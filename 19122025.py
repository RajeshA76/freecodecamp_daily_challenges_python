def pairwise(arr, target):
    sum_index = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j]) == target:
                sum_index += i + j
    return sum_index