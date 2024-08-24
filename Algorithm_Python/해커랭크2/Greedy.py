from itertools import combinations
# 중복 순서 없는 순열
def maxMin(k, arr):
    answer = max(arr)
    for comb in combinations(arr, k):
        answer = min(answer, max(comb)-min(comb))
    return answer
  
def  maxMin2(k, arr):
  answer = max(arr)
  arr.sort()
  for i in range(len(arr)-k-1):
    answer = min(max(arr[i:i+k])-min(arr[i:i+k]))
  return answer

def maxMin3(k, arr):
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - k + 1):
        current_diff = arr[i + k - 1] - arr[i]
        if current_diff < min_diff:
            min_diff = current_diff
    
    return min_diff