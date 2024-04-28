# 비내림차순, 길이가 짧은 부분 수열을 이루는 인덱스 두개(투 포인터) -> i, j 최대-> 최소 
def solutionTwoPointer(sequence, k):
    answer = []
    sum_array = [0 for _ in range(len(sequence)+1)]
    for i in range(len(sequence)):
        for j in range(len(sum_array)-1, i, -1):
            sum_array[j] += sequence[i]


    i = 0
    j = i + 1
    while i <= j and j < len(sum_array):
        if sum_array[j] - sum_array[i] == k:
            if len(answer) == 0:
                answer = [i, j-1]
            elif answer[1]-answer[0] > j-i:
                answer = [i, j-1]
            j += 1
        elif sum_array[j] - sum_array[i] > k:
            i += 1
        else: 
            j += 1
    return answer


solutionTwoPointer([1, 1, 1, 2, 3, 4, 5], 5)