# https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
def solution(n, times):
    start = min(times)
    end = max(times) * n
    
    answer = end
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        
        for time in times:
            temp += mid // time
        
        if temp >= n:
            answer = mid
            end = mid - 1 # 가능한 빨리 끝나는시간
        else:
            start = mid + 1
    
    return answer
