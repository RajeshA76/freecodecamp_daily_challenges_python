from collections import Counter
def purge_most_frequent(arr):
    result = []
    counter = Counter(arr)
    max = float('-inf')
    for key in counter:
        if counter[key] > max:
            max = counter[key]
    for num in arr:
        if counter[num] != max:
            result.append(num)
    return result


        