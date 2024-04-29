#https://www.acmicpc.net/problem/5568
# 중복은 허용하지 않고 순서 있는 순열 선택
from itertools import permutations
def countNumbersInSet():
  n = int(input())
  k = int(input())
  nums = []
  for _ in range(n):
    nums.append(input())
  result_set = set()
  for nums_product in permutations(nums, k):
    result_set.add(int(''.join(nums_product)))
  print(len(result_set))

countNumbersInSet()