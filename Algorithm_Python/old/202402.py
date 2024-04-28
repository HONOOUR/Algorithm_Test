def solution(today, terms, privacies):
    answer = []
    today_arr = today.split(".")
    today_arr = [int(item) for item in today_arr]
    term_dic = {}
    for term in terms:
        t, m = term.split(" ")
        term_dic[t] = int(m)

    for i, privacy in enumerate(privacies, start=1):
        date, t = privacy.split(" ")
        date_arr = date.split(".")
        date_arr = [int(item) for item in date_arr]
        # find m by t
        if term_dic[t] + date_arr[1] > 12:
            date_arr[0] += 1
            date_arr[1] += (term_dic[t]-12)
        else:
            date_arr[1] += term_dic[t]

        # compare date with today
        if date_arr[0] < today_arr[0]:
            answer.append(i)
        elif date_arr[0] == today_arr[0] and date_arr[1] < today_arr[1]:
            answer.append(i)
        elif date_arr[0] == today_arr[0] and date_arr[1] == today_arr[1] and date_arr[2] <= today_arr[2]:
            answer.append(i)

    return answer


solution("2020.01.01", ["Z 3", "D 5"], [
         "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])

# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people)-1
    # i, j 모든 경우 조합 -> i == j -> 혼자 탑승 -> 배열 업데이트
    # 효율적 -> 가장 가벼운 사람 가장 무거운 사람
    while i >= 0 and j >= i:
        if i == j:
            answer += 1
        elif people[i] + people[j] <= limit:
            answer += 1
            i+=1
            j-=1
        else:
            answer += 1
            j-=1

    return answer

print(solution([70, 80, 50], 100))

