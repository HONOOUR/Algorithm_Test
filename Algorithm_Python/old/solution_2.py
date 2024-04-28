min_count = 0


def applyPylons(k, arr, index, count):
    for i in range(index-k, index+k):
        if i < 0 or i >= len(arr):
            continue
        arr[i] = 1

    for i in range(len(arr)):
        if arr[i] == 0:
            return

    global min_count
    min_count = min(min_count, count)


def dfs(k, arr, count, visited, num, start_index):
    if count == sum:
        return

    for i in range(start_index, len(arr)):
        if visited[i] == 1:
            continue
        if arr[i] == 1:
            visited[i] = 1
            temp = arr.copy()
            applyPylons(k, temp, i, count+1)
            dfs(k, temp, count+1, visited, num, i+1)
            visited[i] = 0


def pylons(k, arr):
    global min_count
    min_count = len(arr)
    num = arr.count(1)
    visited = [0 for _ in range(len(arr))]
    dfs(k, arr, 0, visited, num, 0)

    print(min_count)
    if min_count == len(arr):
        return -1

    return min_count


pylons(2, [0, 1, 1, 1, 1, 0])
