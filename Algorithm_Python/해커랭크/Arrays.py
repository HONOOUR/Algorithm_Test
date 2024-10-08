# https://www.hackerrank.com/
# challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
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
    n = len(a)
    answer = [0 for _ in range(n)]
    for i in range(n):
        answer[abs(i+n-d) % n] = a[i]
        
    return answer

# Palindrome
def solution(S):
    # Implement your solution here
    for i in range(len(S)):
        left_string = S[:i]
        right_string = S[i+1:]
        if left_string == right_string[::-1]:
            return i
    return -1