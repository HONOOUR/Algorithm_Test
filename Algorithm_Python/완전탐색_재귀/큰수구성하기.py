# 숫자 N의 자릿 수와 동일한 수를 뽑아야하는 것으로 문제를 이해함.
# from itertools import product
# def largeNumber():
#     n, m = input().split()
#     nums = list(input().split())

#     length = len(n)
#     target = int(n)
#     temp = 0
    
#     for num_product in product(nums, repeat=length):
#         num = int(''.join(num_product))
#         if num > temp and num <= target:
#             temp = num
#     print(temp)
# largeNumber()

# https://www.acmicpc.net/problem/18511
# 중복 순열에서 몇개 씩 뽑을 지를 변수로 만들어 한개씩 줄인다
from itertools import product
def largeNumber():
    n, m = input().split()
    nums = list(input().split())

    length = len(n)
    target = int(n)
    temp = 0
    
    while length > 0:
      for num_product in product(nums, repeat=length):
          num = int(''.join(num_product))
          if num > temp and num <= target:
              temp = num
      if temp == 0:
          length -= 1
      else:
          break
    print(temp)
largeNumber()