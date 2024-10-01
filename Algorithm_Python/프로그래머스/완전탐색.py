# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    arr_1 = [1, 2, 3, 4, 5]
    arr_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr_count = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == arr_1[i%5]:
            arr_count[0] += 1
        if answers[i] == arr_2[i%8]:
            arr_count[1] += 1
        if answers[i] == arr_3[i%10]:
            arr_count[2] += 1
    max_count = max(arr_count)
    for i in range(len(arr_count)):
        if max_count == arr_count[i]:
            answer.append(i+1)
    return answer
  
from itertools import permutations

def solution(numbers):
    numbers = list(numbers)
    prime_numbers = set()
    for count in range(1, len(numbers)+1):
        for nums in permutations(numbers, count):
            temp = ''.join(nums)
            num = int(temp)
            is_prime = True
            for i in range(2, int(num**0.5+1)): # root 사용 해서 소수 체크
                if num % i == 0:
                    is_prime = False
            if is_prime and num >= 2:
                prime_numbers.add(num)
    return len(prime_numbers)
  
solution("17")

https://school.programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []
    # brown_y = yellow_y + 2
    # brown_x = yellow_x + 2
    
    for yellow_x in range(1, yellow+1):
        if yellow % yellow_x == 0:
            yellow_y = yellow // yellow_x
            if ((yellow_x+2)+(yellow_y+2))*2== brown+4:
                return [yellow_y+2, yellow_x+2]