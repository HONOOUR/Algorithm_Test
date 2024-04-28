def quicksort(data, start, end):
    if start >= end:
        return
    key = start
    i = start+1
    j = end
    temp = 0

    while i < j:
        while i <= end and data[i] <= data[key]:
            i += 1
        while j > start and data[j] >= data[key]:
            j -= 1
        if i > j:  # i, j cross, key change
            temp = data[j]
            data[j] = data[key]
            data[key] = temp
        else:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

    quicksort(data, start, j-1)
    quicksort(data, j+1, end)


def solution(data):
    size = len(data)-1
    quicksort(data, 0, size)


solution([1, 10, 5, 8, 7, 6, 4, 3, 2, 9])
