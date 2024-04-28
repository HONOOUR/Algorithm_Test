import itertools
import urllib.request
import json


def solution(N, S):
    col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
    seats = [[0 for _ in range(len(col))] for _ in range(N)]
    reserved = list(S.split(" "))
    for seat in reserved:
        r, c = seat[:-1], seat[-1]
        seats[int(r)-1][col.index(c)] = 1

    count = 0
    for i in range(N):
        if seats[i][1] == 0 and seats[i][2] == 0 and seats[i][3] == 0 and seats[i][4] == 0:
            count += 1
            if seats[i][5] == 0 and seats[i][6] == 0 and seats[i][7] == 0 and seats[i][8] == 0:
                count += 1
        elif seats[i][3] == 0 and seats[i][4] == 0 and seats[i][5] == 0 and seats[i][6] == 0:
            count += 1


solution(22, '1A 3C 2B 20G 5A')


def solution(N, A, B):
    graph = [[] for _ in range(N+1)]
    for i in range(len(A)):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])

    for i in range(1, N):
        if i+1 not in graph[i]:
            return False
    return True


solution(6, [2, 4, 5, 3], [3, 5, 6, 4])


def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        if enable_print >= 1:
            print(N % 10, end="")
        N = N // 10


solution(100077)


def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(0, 26):
        if occurrences[i] > best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char


solution("aaaaappppple")


def getways(n, c):
    combinations = [0 for _ in range(n+1)]
    combinations[0] = 1  # temporary

    for coin in c:
        for amount in range(n+1):
            if amount >= coin:
                combinations[amount] += combinations[amount-coin]

    return combinations[n]


getways(10, [2, 5, 3, 6])


def getTopRatedFoodOutlets(city):
    request = 'https://jsonmock.hackerrank.com/api/food_outlets?city='+city+'&page='
    response = urllib.request.urlopen(request+'1')
    obj = json.loads(response)
    total_page_number = obj['total_pages']
    cities = {}
    max_rating = 0
    for i in range(1, int(total_page_number)+1):
        response = urllib.request.get(request+str(i))
        obj = json.loads(response)
        if max_rating < obj['data']['user_rating']['average_rating']:
            max_rating = obj['data']['user_rating']['average_rating']
            city_name = obj['data']['name']
            if max_rating in cities.keys():
                temp = cities.get(max_rating)
                temp.append(city_name)
                cities[max_rating] = temp
            else:
                cities[max_rating] = [city_name]

    key = sorted(cities.keys()).pop()
    return cities[key]


getTopRatedFoodOutlets('Denver')


def decode(encoded):
    encoded = list(str(encoded)).reverse
    decoded = ''
    last_index = len(encoded)-1
    index = 0
    while index < last_index:
        if encoded[index]+encoded[index+1] == '32':
            decoded += ' '
            index += 2
            continue

        if index <= last_index-2:
            if int(encoded[index]+encoded[index+1]+encoded[index+2]) <= 122:
                decoded += chr(int(encoded[index] +
                               encoded[index+1]+encoded[index+2]))
                index += 3
                continue

        decoded += chr(int(encoded[index]+encoded[index+1]))
        index += 2
    return decoded


decode(23511011501782351112179911801562340161171141148)


def solution(cards):
    for i in range(len(cards)):
        kero = 0
        berony = 0
        temp = list.copy(cards)
        temp.pop(i)
        card_index = 0
        while card_index < len(temp):
            if card_index % 2 == 0:
                kero += temp[card_index]
            else:
                berony += temp[card_index]
            card_index += 1
        if kero == berony:
            return i+1
    return -1


solution([2, 5, 2, 7, 8, 4])

min_count = float('inf')


def dfs_w(start, count, visited, weight):
    global min_count
    n = len(weight)
    if count == n:
        min_count = n
        return
    if len(visited) == n:
        min_count = min(min_count, count)
        return

    for i in range(start, n):
        for j in range(i+1, n):
            if i == j:
                continue
            if i in visited:
                break
            if j in visited:
                continue
            if weight[i] + weight[j] <= 3.00:
                visited.add(i)
                visited.add(j)
                dfs_w(i+1, count+1, visited, weight)
                visited.remove(i)
                visited.remove(j)
            else:
                visited.add(i)
                dfs_w(i+1, count+1, visited, weight)
                visited.remove(i)


def solution_w(weight):
    global min_count
    visited = set()
    dfs_w(0, 0, visited, weight)
    return min_count


solution_w([1.01, 1.99, 2.5, 1.5, 1.01])


min_count = float('inf')


def dfs_w(count, visited, weight):
    n = len(weight)
    if len(visited) == n:
        global min_count
        min_count = min(min_count, count)
        return

    for i in range(n):
        for j in range(i+1, n):
            if i == j:
                continue
            if i in visited or j in visited:
                continue
            if weight[i] + weight[j] <= 3.00:
                visited.add(i)
                visited.add(j)
                dfs_w(count+1, visited, weight)
                visited.remove(i)
                visited.remove(j)
            else:
                visited.add(i)
                dfs_w(count+1, visited, weight)
                visited.remove(i)


def solution_w(weight):
    global min_count
    visited = set()
    dfs_w(0, visited, weight)
    print(min_count)
    return min_count


solution_w([1.01, 1.99, 2.5, 1.5, 1.01])


def solution_keypad(s, keypad):
    answer = 0
    board = [[0 for _ in range(3)] for _ in range(3)]
    y = 0
    x = 0
    s = list(str(s))
    keypad = list(str(keypad))
    for r in range(3):
        for c in range(3):
            key = keypad.pop(0)
            board[r][c] = key
            if key == s[0]:
                y = r
                x = c
    key_pressed = s.pop(0)
    while s:  # for key in s:
        visited = set()
        key = s.pop(0)
        if key_pressed == key:
            continue
        else:
            key_pressed = key

        isFirstRound = False
        isSecondRound = True
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if 0 <= y+dy < 3 and 0 <= x+dx < 3 and not isFirstRound:
                    visited.add((y+dy, x+dx))
                    if board[y+dy][x+dx] == key:
                        y += dy
                        x += dx
                        answer += 1
                        isFirstRound = True
                        isSecondRound = False

        if not isSecondRound:
            continue

        for dy in [-2, -1, 0, 1, 2]:
            for dx in [-2, -1, 0, 1, 2]:
                if 0 <= y+dy < 3 and 0 <= x+dx < 3:
                    if (y+dy, x+dx) in visited:
                        continue
                    visited.add((y+dy, x+dx))
                    if board[y+dy][x+dx] == key:
                        y += dy
                        x += dx
                        answer += 2
    return answer


solution_keypad(523817, 371648295)


def test_2(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    if clockwise:
        dy = [[0, 1, 0, -1], [1, 0, -1, 0], [0, -1, 0, 1], [-1, 0, 1, 0]]
        dx = [[1, 0, -1, 0], [0, -1, 0, 1], [-1, 0, 1, 0], [0, 1, 0, -1]]
        y_x = [[0, 0], [0, n-1], [n-1, n-1], [n-1, 0]]
        for i in range(4):
            y = y_x[i][0]
            x = y_x[i][1]
            num = 1
            j = 0
            size = n-2
            while size >= 0:
                for _ in range(0, size):
                    answer[y][x] = num
                    y += dy[i][j]
                    x += dx[i][j]
                    num += 1
                size -= 1
                j = (j+1) % 4
            answer[y][x] = num
    else:
        dy = [[-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1]]
        dx = [[0, -1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1], [-1, 0, 1, 0]]
        y_x = [[n-1, n-1], [n-1, 0], [0, 0], [0, n-1]]
        for i in range(4):
            y = y_x[i][0]
            x = y_x[i][1]
            num = 1
            j = 0
            size = n-2
            while size >= 0:
                for _ in range(0, size):
                    answer[y][x] = num
                    y += dy[i][j]
                    x += dx[i][j]
                    num += 1
                size -= 1
                j = (j+1) % 4
            answer[y][x] = num

    return answer


test_2(5, True)


def test_1(money, costs):
    cost_dic = {}
    cost_to_money = [1, 5, 10, 50, 100, 500]
    for i, cost in enumerate(costs):
        cost_dic[cost/cost_to_money[i]] = [cost_to_money[i], cost]

    cost_sum = 0
    for cost_key in sorted(cost_dic.keys()):
        count = money // cost_dic[cost_key][0]
        money -= (count*cost_dic[cost_key][0])
        cost_sum += (count*cost_dic[cost_key][1])

    return cost_sum


test_1(1999, [2, 11, 20, 100, 200, 600])


def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False
    if (A[0] != 1 and A[n - 1] != K):
        return False
    elif n == 1 and A[0] != K:
        return False
    else:
        return True


solution([1], 1)


def solution(record):
    answer = []
    temp = []
    chairs = [0 for _ in range(100000)]
    table = []
    for r in record:
        table.append(list(r.split(' ')))

    index = 0
    keep = 0
    for t in table:
        if t[1] == 'sit':
            id = int(t[0][3])
            keep = int(t[2][2])
            if index == 0:
                index += keep
            else:
                index += (keep+1)

            # while chairs[index-keep] == 1 or chairs[index-keep] == 2 or chairs[index+keep] == 1 or chairs[index+keep] == 2:
            while chairs[index] != 0:
                index += 1
            chairs[index] = 1
            for i in range(index-keep, index):
                if chairs[i] != 2:
                    chairs[i] = 2
            for i in range(index+1, index+keep+1):
                if chairs[i] != 2:
                    chairs[i] = 2
            temp.append([id, index, keep])
        elif t[1] == 'leave':
            id = int(t[0][3])
            for i in range(len(temp)):
                if temp[i][0] == id:
                    index = temp[i][1]
                    keep = temp[i][2]
                    for j in range(index-keep+1, index+keep):
                        if chairs[j] == 2:
                            chairs[j] = 0
                    temp.pop(i)
                    break

    for t in temp:
        answer.append([t[0], t[1]])
    return answer


solution(["id=1 sit k=1", "id=2 sit k=3", "id=3 sit k=2",
         "id=2 leave", "id=4 sit k=4", "id=5 sit k=2"])

max_units = 0


def select_r(needs, visited, r, count, selected):
    global max_units
    if count == r:
        units = 0
        for need in needs:
            satisfied = False
            for s in selected:
                if need[s] == 1:
                    satisfied = True
                else:
                    satisfied = False
                    break
            if satisfied:
                units += 1

        max_units = max(max_units, units)
        return

    for i in range(len(needs[0])):
        if visited[i] == 1:
            continue
        visited[i] = 1
        selected.append(i)
        select_r(needs, visited, r, count+1, selected)
        visited[i] = 0
        selected = []


def solution(needs, r):
    visited = [0 for _ in range(len(needs[0]))]
    selected = []
    select_r(needs, visited, r, 0, selected)
    return max_units


solution([[1, 0, 0], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1]], 2)


def solutions(scores):
    answer = 0
    for score in scores:
        if score.count('A') >= 2 and score.count('F') < 2:
            answer += 1
        elif score.count('F') >= 2:
            continue
        else:
            sum_s = 0
            max_s = 0
            min_s = 0
            for s in score:
                if s == 'A':
                    max_s = max(5, max_s)
                    min_s = min(5, min_s)
                    sum_s += 5
                elif s == 'B':
                    max_s = max(4, max_s)
                    min_s = min(4, min_s)
                    sum_s += 4
                elif s == 'C':
                    max_s = max(3, max_s)
                    min_s = min(3, min_s)
                    sum_s += 3
                elif s == 'D':
                    max_s = max(2, max_s)
                    min_s = min(2, min_s)
                    sum_s += 2
                elif s == 'E':
                    max_s = max(1, max_s)
                    min_s = min(1, min_s)
                    sum_s += 1
                else:
                    max_s = max(0, max_s)
                    min_s = min(0, min_s)
            average = (sum_s - max_s - min_s)/(len(score)-2)
            if average >= 3:
                answer += 1

    return answer


solutions(["AAFAFA", "FEECAA", "FABBCB", "CBEDEE", "CCCCCC"])


def openChatting(record):
    answer = []
    words = []
    for r in record:
        words.append(list(r.split(" ")))

    for i in range(len(words)):
        if words[i][0] == "Enter" or words[i][0] == "Change":
            id = words[i][1]
            nickname = words[i][2]
            for j in range(i):
                if words[j][1] == id:
                    words[j][2] = nickname
        elif words[i][0] == "Leave":
            id = words[i][1]
            for j in range(i):
                if words[j][1] == id:
                    nickname = words[j][2]
                    words[i].append(nickname)

    for word in words:
        if word[0] == "Enter":
            answer.append(str(word[2]) + "님이 들어왔습니다.")
        elif word[0] == "Leave":
            answer.append(str(word[2]) + "님이 나갔습니다.")

    return answer


openChatting(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
             "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
# def getMaxLeaves(leave, day, holidays):
#     answer = 0
#     days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
#     days_start = {'MON': 0, 'TUE': 0, 'WED': 0,
#                   'THU': 0, 'FRI': 0, 'SAT': 0, 'SUN': 0}

#     day_index = days.index(day)
#     for i in range(7):
#         index = (day_index+i) % 7
#         days_start[days[index]] = i + 1

#     sat = days_start['SAT']
#     sun = days_start['SUN']

#     while sat <= 30:
#         holidays.append(sat)
#         sat += 7

#     while sun <= 30:
#         holidays.append(sun)
#         sun += 7

#     start = days_start[day]
#     while start <= 30:
#         total_leave = 0
#         count = 0
#         temp = start
#         while (count < leave and temp <= 30) or temp in holidays:
#             if temp not in holidays:
#                 count += 1
#             total_leave += 1
#             temp += 1
#         answer = max(answer, total_leave)
#         start += 1

#     return answer

# getMaxLeaves(	3, "SUN", [2, 6, 17, 29])


def solution(registered_list, new_id):
    answer = ''
    if registered_list.count(new_id) > 0:
        sorted_list = []
        temp_id = ''
        digit_index = 0
        word_index = 0
        has_digit = False

        for j in range(len(registered_list)):
            if has_digit:
                break
            for i in range(len(registered_list[j])):
                if registered_list[j][i].isdigit():
                    digit_index = i
                    word_index = j
                    has_digit = True
                    break

        for id in registered_list:
            if id[:digit_index] == new_id:
                sorted_list.append(id)
        min_digits = 100000
        for id in sorted_list:
            digits = int(id[digit_index:])
            min_digits = min(min_digits, digits)

        id = registered_list[word_index]
        min_digits = min(min_digits, int(id[digit_index:])+1)
        temp_id = id[:digit_index] + min_digits

        while registered_list.count(temp_id) > 0:
            min_digits += 1
            temp_id = temp_id[:digit_index] + str(min_digits)

    else:
        answer = new_id

    return answer


solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98")


def getCourses(orders, course):
    answer = []
    combi_dics = {}
    for order in orders:
        num = len(order)
        order = list(map(' '.join, order))
        for i in course:
            # combinations
            combis = list(map(''.join, itertools.combinations(order, i)))
            for comb in combis:
                # in dics ?
                if combi_dics.get(comb):
                    combi_dics[comb] += 1
                else:
                    combi_dics[comb] = 1

    for key, value in combi_dics.items():
        if value >= 2:
            answer.append(key)

    answer.sort()

    print(answer)


getCourses(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]	)
