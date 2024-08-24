# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# 1 제일 큰 합
# arr[i][j] + arr[i][j+1] + arr[i][j+2] 
# + arr[i+1][j+1] 
# + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
# 2 범위
# i < n-2 and j < n-2

def hourglassSum(arr):
    max_sum = -63
    n = len(arr)
    for i in range(n-2):
        for j in range(n-2):
            max_sum = max(max_sum, arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if max_sum == 63:
                print(max_sum)
    print(max_sum)
    
arr = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]
hourglassSum(arr)


def rotLeft(a, d):
    # a = [1, 2, 3, 4, 5]
    # length = len(a) = 5
    # d = 2
    # a[|0-2+5|%5] = a[3] = 1
    # a[|1-2+5|%5] = a[4] = 2
    # a[|2-2|%5] = a[0] = 3
    # a[|5-2|%5] = a[3] = 5
    
    n = len(a)
    answer = [0 for _ in range(n)]
    for i in range(n):
        if i-d<0:
            answer[abs(i+n-d) % n] = a[i]
        else:
            answer[abs(i-d) % n] = a[i]
    return answer