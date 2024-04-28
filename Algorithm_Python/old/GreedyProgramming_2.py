import sys

# https://www.acmicpc.net/problem/2457


def getFlowersCount():
    input = sys.stdin.readline
    flowers_num = int(input())
    target_period = [60, 334]
    month_day = {0: 0, 1: 31, 2: 59, 3: 90, 4: 120, 5: 157,
                 6: 181, 7: 212, 8: 248, 9: 273, 10: 304, 11: 334, 12: 365}
    flowers = []
    for _ in range(flowers_num):
        start_m, start_d, end_m, end_d = map(int, input().split())
        start = month_day[start_m-1] + start_d
        end = month_day[end_m-1] + end_d
        flowers.append([start, end])
    candidate = []
    flowers.sort(key=lambda x: (x[0], x[1]))
    # while target starts from 60 and ends to over 334
    target = target_period[0]
    flower_temp = [0, 0]
    while target < target_period[1] and flowers:
        change = False
        for flower in flowers:
            if flower[1] > target_period[1] and flower[0] < target_period[0]:
                candidate.append(flower)
                break
            # target 보다 일찍 핀 꽃을 임시로 저장하고 그중에서 가장 늦게 지는 값으로 선택
            elif flower[0] < target and flower[1] > flower_temp[1]:
                flower_temp = flower
                change = True
        if not change:
            candidate = []
            break
        else:
            candidate.append(flower_temp)
            flowers.remove(flower_temp)
            target = flower_temp[1]

    print(len(candidate))

# https://www.acmicpc.net/problem/2109](https://www.acmicpc.net/problem/2109
# 가장 금액을 많이 지불하는 순으로 정렬
# 가장 금액을 많이 지불하는 순서로 가능한 가장 늦게 간다


def getMostPaidByLectures():
    input = sys.stdin.readline
    num_uni = int(input())
    lectures = []
    for _ in range(num_uni):
        price, due_date = map(int, input().split())
        lectures.append((price, due_date))
    schedule = {}
    lectures.sort(key=lambda x: (-x[0]))
    for lec in lectures:
        for i in range(lec[1], 0, -1):
            if i not in schedule:
                schedule[i] = lec[0]
                break
    answer = 0
    for key in schedule.keys():
        answer += schedule[key]

    print(answer)

# https://www.acmicpc.net/problem/19941


def getHamburgerNum():
    item_num, dist = map(int, input().split())
    item_list = list(input())

    answer = 0
    for i in range(item_num):
        if item_list[i] == "P":
            for d in range(-dist, dist+1, 1):
                if i+d >= 0 and i+d < item_num and item_list[i+d] == "H":
                    item_list[i+d] = "X"
                    answer += 1
                    break
    print(answer)


# http://acmicpc.net/problem/19939](http://acmicpc.net/problem/19939


def getBallNumGap():
    input = sys.stdin.readline
    ball_num, basket_num = map(int, input().split())
    least_ball_num = basket_num*(basket_num+1)//2
    if ball_num < least_ball_num:
        print(-1)
    elif (ball_num - least_ball_num) % basket_num == 0:
        print(basket_num-1)
    else:
        # 가장 많이 공이 들어있는 바구니부터 한개씩 더함
        print(basket_num)

# 오셀로 재배치
# https://www.acmicpc.net/problem/13413

def getOcello(self):
    input = sys.stdin.readline
    test_num = int(input())
    for _ in range(test_num):
        num = int(input())
        src = list(input())
        trg = list(input())
        tmp = []
        answer = 0
        for i in range(num):
            if src[i] != trg[i]:
                # src 와 trg 비교시 다른게 있을때 tmp가 비어있으면 tmp 배열에 넣는다.
                # src 와 trg 비교시 다른게 있을때 tmp 에 아이템이 있으면 마지막아이템과 비교해서 다르면 tmp에서 마지막아이템도 제거하고 비교한 아이템도 제거하고 비교한 아이템도 넣지 않는다 (switch)
                if tmp and tmp[len(tmp)-1] != src[i]:
                    answer += 1
                    tmp.pop(len(tmp)-1)
                else:
                    tmp.append(src[i]) # 1. switch two different 
                                       # 2. flip one
        answer += len(tmp) # (flip)
        print(answer)

# 스네이크 버드
# https://www.acmicpc.net/problem/16435

def getSnakeLength(self):
    input = sys.stdin.readline
    fruit_num, snake_len = map(int, input().split())
    fruits = list(map(int, input().split()))
    fruits.sort()
    for fruit in fruits:
        if fruit <= snake_len:
            snake_len += 1
    print(snake_len)

# APC
# https://www.acmicpc.net/problem/17224
def getTestSum(self):
    input = sys.stdin.readline
    test_num, power, max_test_num = map(int, input().split())
    tests = []
    count = 0
    answer = 0
    for _ in range(test_num):
        easy, hard = map(int, input().split())
        tests.append((easy, hard))
    tests.sort(key=lambda x: (x[1]))

    # for hard question (priority 1)
    for test in tests:
        if count == max_test_num:
            break
        if test[1] <= power: 
            count +=1
            answer += 140
        else:
            break
        
    # for easy question (priority 2)
    tests = tests[count:]
    tests.sort(key=lambda x: (x[0]))
    for test in tests:
        if count == max_test_num: 
            break
        if test[0] <= power:
            count += 1
            answer += 100
        else:
            break
    print(answer)

getFlowersCount()
getMostPaidByLectures()
getHamburgerNum()
getBallNumGap()
getOcello()
getSnakeLength()
getTestSum()
