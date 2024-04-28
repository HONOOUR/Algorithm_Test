import sys
import re
from typing import no_type_check_decorator
# https://www.hackerrank.com/challenges/greedy-florist/problem

city = [[0, 0, 1], [1, 1, 1], [0, 1, 1]]

i = 0
j = 0


def change(city, i, j):
    while i < len(city)-1 and j < len(city)-1:
        if city[i][j] == 0:
            city[i+1][j] = 1
            city[i][j+1] = 1
        else:
            if city[i][j] != 0 and city[i][j] == city[i+1][j]:
                city[i+1][j] = city[i][j] + 1
            if city[i][j] != 0 and city[i][j] == city[i][j+1]:
                city[i][j+1] = city[i][j] + 1

        city = change(city, i+1, j)
        city = change(city, i, j+1)

    return city


def solution(city):
    i = 0
    j = 0
    x = 0
    if city[i][j] == 0:
        city = change(city, i+1, j)
        city = change(city, i, j+1)

    else:
        return


solution(city)


def solution(office, k):
    answer = -1
    num = len(office) - k + 1
    em_count = 0
    for v_n in range(num):
        for h_n in range(num):
            em_count_temp = 0
            for k_i in range(k):
                em_count_temp += office[h_n+k_i][v_n:v_n+k].count(1)
            em_count = max(em_count_temp, em_count)
    return em_count


solution([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 1, 0]], 2)


def solution(n, record):
    answer = []
    record_sorted = []
    for _ in range(n):
        record_sorted.append([])

    for r in record:
        record_sorted[r[0]-1].append(r[1])

    max_biddings = []
    for i in range(n):
        if len(record_sorted[i]) > 0 and record_sorted[i][-1] == -1:
            remove_count = record_sorted[i].count(-1)
            while remove_count > 0:
                if record_sorted[i][-1] == -1:
                    record_sorted[i].pop()
                else:
                    record_sorted[i].pop()
                    remove_count -= 1

        if len(record_sorted[i]) == 0:
            max_biddings.append([0, i+1])
        else:
            max_bidding = record_sorted[i][-1]
            max_biddings.append([max_bidding, i+1])


solution(4, [[4, 120], [3, 200], [4, 220], [4, 150], [4, 250], [2, 150], [4, -1], [4, -1], [2, 200],
         [4, 300], [4, 200], [2, 150], [4, -1], [2, -1], [4, 100], [4, -1], [3, -1], [2, -1], [4, -1], [4, -1]])


def solution(citations):
    answer = 0
    citations = sorted(citations)
    if citations[-1] == 0:
        return answer
    else:
        while answer < len(citations) and answer > -1:
            answer += 1
            if answer >= citations[len(citations)-answer-1]:
                break
    return answer


solution([3, 0, 6, 1, 5])


def getMinFlowerPrice(k, c):
    answer = 0
    # sort price in ascending order
    flowers = sorted(c)

    i = 0
    while True:
        if len(flowers) == 0:
            break
        # the num of people who can buy flower and take the next turn
        for _ in range(k):
            if len(flowers) == 0:
                break
            # buy more expensive one first
            answer += ((i + 1) * flowers.pop())

        i += 1

    # elif len(c) == k:
    #     i = 0
    #     for _ in range(k):
    #         if len(c) == 0:
    #             break
    #         answer += ((i + 1) * c.pop())
    # else:
    return answer


getMinFlowerPrice(3, [390225, 426456, 688267, 800389, 990107, 439248, 240638, 15991, 874479, 568754, 729927, 980985, 132244, 488186, 5037, 721765, 251885, 28458, 23710, 281490, 30935, 897665, 768945, 337228,
                  533277, 959855, 927447, 941485, 24242, 684459, 312855, 716170, 512600, 608266, 779912, 950103, 211756, 665028, 642996, 262173, 789020, 932421, 390745, 433434, 350262, 463568, 668809, 305781, 815771, 550800])


def getMinCandies(n, arr):
    answer = 0
    candies_right = [1]
    candies_left = [1]
    # compare it to its left only
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            temp = candies_left[-1]
            candies_left.append(temp+1)
        else:
            candies_left.append(1)

    # compare it to its right only
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i+1]:
            temp = candies_right[0]
            candies_right.insert(0, temp+1)
        else:
            candies_right.insert(0, 1)

    # take the max between them
    for i in range(n):
        max_candies = max(candies_left[i], candies_right[i])
        answer += max_candies
    return answer


getMinCandies(6, [4, 6, 4, 5, 6, 2])


def getMinCandies_(n, arr):
    answer = 0
    students = arr
    candies = []
    if students[0] > students[1]:
        candies.append(2)
        candies.append(1)
    elif students[0] < students[1]:
        candies.append(1)
        candies.append(2)
    else:
        candies.append(1)
        candies.append(1)

    i = 2
    while i < len(students):
        if students[i-1] < students[i]:
            temp = candies[-1]
            candies.append(temp+1)
        elif students[i-1] > students[i]:
            if candies[-1] == 1:
                temp = candies.pop()
                if temp == 2:
                    candies.append(3)
                    candies.append(2)
                else:
                    candies.append(temp)
                    candies.append(2)
            else:
                candies.append(1)
        else:
            candies.append(1)
        i += 1

    for c in candies:
        answer += c
    return answer


# def solution(amountText):
#     answer = True
#     # pattern = re.compile("?:\d+(?:,?\d{3})*")
#     pattern = re.compile([0-9])
#     pattern.match(amountText)

#     return answer

# solution('10,000')

# def solution(servers, sticky, requests):
#     servers_list = []
#     for _ in range(servers):
#         servers_list.append([])

#     if sticky:
#         i = 0
#         while i < len(servers_list) and servers_list[i] == []:
#             servers_list[i].append(requests.pop(0))
#             i += 1

#         j = 0
#         for r in requests:
#             j = j % len(servers_list)
#             while j < len(servers_list) and servers_list[j].count(r) == 0:
#                 j += 1

#             servers_list[j].append(r)
#             j += 1

#     else:
#         for r in requests:
#             servers_list[0].append(r)
#             temp = servers_list.pop(0)
#             servers_list.append(temp)

#     return servers_list

# solution(2, True, [1, 2, 2, 3, 4, 1])

# def solution(orderAmount, taxFreeAmount, serviceFee):
#     # orderAmount : 주문금액
#     # taxFreeAmount : 비과세금액
#     # serviceFee : 봉사료
#     taxAmount = 0
#     if serviceFee == 0:
#         taxAmount = (orderAmount - taxFreeAmount) * 10 / 11

#     answer = round(taxAmount * 0.1)
#     return answer

# solution(100, 0, 0)


def gridChallenge(grid):
    answer = "YES"
    for g in grid:
        temp = []
        for el in g:
            temp.append(el)
        temp = sorted(temp)

        for i in range(0, len(temp)-1, 1):
            if ord(temp[i+1]) - ord(temp[i]) != 1:
                answer = "NO"
                break

    return answer


grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
gridChallenge(grid)
# https://leetcode.com/problems/non-overlapping-intervals/


def eraseOverlapIntervals(intervals) -> int:
    intervals = sorted(intervals)
    left = 0
    right = 1
    remove_count = 0
    while left != right and right < len(intervals):
        # case 2 -> remove right
        if intervals[left][0] < intervals[right][0] and intervals[left][1] > intervals[right][0]:
            right += 1
            remove_count += 1
        # case 3 -> remove bigger one
        elif intervals[left][0] <= intervals[right][0] and intervals[left][1] >= intervals[right][1]:
            left = right
            right += 1
            remove_count += 1
        elif intervals[left][0] == intervals[right][0] and intervals[left][1] <= intervals[right][1]:
            right += 1
            remove_count += 1
        # case 1 -> non overlapping
        else:
            left = right
            right += 1
    return remove_count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
eraseOverlapIntervals(intervals)


# https://leetcode.com/problems/queue-reconstruction-by-height/


def reconstructQueue(people):
    queue = []
    sorted_people = sorted(people, reverse=True)
    for person in sorted_people:
        if len(queue) == 0:
            queue.append(person)
        else:
            queue.insert(person[1], person)
    return queue


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
reconstructQueue(people)

# https://leetcode.com/problems/remove-k-digits/
# remove k digits


def getSmallestDigits(num, k):
    nums = []
    for n in num:
        nums.append(int(n))

    answer = ""
    removed_count = 0
    i = 0
    while removed_count != k and i < len(nums)-1:
        if nums[i] > nums[i+1]:
            nums.pop(i)
            removed_count += 1
        else:
            i += 1

    while removed_count < k:
        nums.pop()
        removed_count += 1

    while nums[0] == 0 and len(nums) > 0:
        nums.pop(0)

    for num in nums:
        answer += str(num)
    return answer


num = "10"
removed_num = 2
getSmallestDigits(num, removed_num)

# https://leetcode.com/problems/wiggle-subsequence/
# 같은 패턴(down, down )이 나오면 무시할 수 있도록 up, down 으로 나누어 count를 업데이트한다.
# up = down + 1
# down = up + 1


def getWiggleMaxLength(nums):
    up_count = down_count = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            down_count = up_count + 1
        elif nums[i] < nums[i+1]:
            up_count = down_count + 1

    answer = max(up_count, down_count)
    return answer + 1


nums = [1, 7, 4, 9, 2, 5]
getWiggleMaxLength(nums)


# https://leetcode.com/problems/jump-game-ii/


def getJumpToLast(nums):
    jump_count = 0
    left = right = 0  # start point
    while right < len(nums):
        farthest = 0
        for i in range(left, right+1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jump_count += 1

    return jump_count


nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]
getJumpToLast(nums)

# https://leetcode.com/problems/jump-game/


def canJumpNums(nums):
    answer = True
    if len(nums) == 1 and nums[0] == 0:
        return answer

    jump_count = 1
    for i in range(len(nums)-2, -1, -1):
        # 이전에 나오는 수가 다음 수로 점프할수 있는것이 가능한지 (횟수는 중요하지 않음)
        if nums[i] >= jump_count:
            jump_count = 1
            answer = True
            continue
        else:
            jump_count += 1
            answer = False
    return answer


nums = [2, 0]
canJumpNums(nums)
