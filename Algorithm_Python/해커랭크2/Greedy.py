from itertools import combinations
# 중복 순서 없는 순열
def maxMin(k, arr):
    answer = max(arr)
    for comb in combinations(arr, k):
        answer = min(answer, max(comb)-min(comb))
    return answer
  
def maxMin2(k, arr):
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


# Kadane's Algorithm
# O(n) <- only through the array
# keep track "max_sum"
# choose starting new subarray or extending the existing subarray
# max(num, sub_sum+num)
def maxSubArray(nums):
    max_sum = sub_sum = nums[0]
    for num in nums[1:]:
        sub_sum = max(num, sub_sum+num) # 현재 숫자가 음수이면 새로 배열을 생성하지 않는다
        max_sum = max(max_sum, sub_sum)
    return max_sum