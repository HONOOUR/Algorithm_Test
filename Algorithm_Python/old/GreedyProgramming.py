import sys
from collections import deque
import heapq


class GreedyProgramming():
    def getChangeNumber(self, price):
        change = 1000 - price
        answer = 0
        # x = y = z = p = q = 0  # number of coins
        # change = 500x + 100y + 50z + 10p + 1q
        while change != 0:
            if change >= 500:
                change -= 500
                answer += 1
            elif change < 500 and change >= 100:
                change -= 100
                answer += 1
            elif change < 100 and change >= 50:
                change -= 50
                answer += 1
            elif change < 50 and change >= 10:
                change -= 10
                answer += 1
            elif change < 10 and change >= 5:
                change -= 5
                answer += 1
            elif change < 5 and change >= 1:
                change -= 1
                answer += 1

        # answer = x+y+z+p+q
        return answer

    def getGasPrice(self):
        station_count = int(input())
        dists = list(map(int, input().split()))
        stations = list(map(int, input().split()))
        total_price = 0
        min_price = stations[0]
        for i in range(station_count-1):
            if stations[i] < min_price:
                min_price = stations[i]
            total_price += min_price * dists[i]

        print(total_price)

    # https://www.acmicpc.net/problem/4796
    # 총 휴가 동안 캠핑장을 사용할 수 있는 날짜
    def getCampingDay(self):
        total_day = 0
        test_case = list(map(int, input().split()))
        index = 0
        while True:
            l, p, v = list(map(int, input().split()))
            index += 1
            if l+p+v == 0:
                break
            else:
                val = v // p
                rem = min(v % p, l)
                total_day = l * val
                total_day += rem
                print(f'Case {index}: {total_day}')

    def getSmallest(self):
        num_weights = int(input())
        weights = list(map(int, input().split()))
        weights.sort()
        smallest_weight = 1
        sum_weight = 0

        while True:
            for i in range(num_weights):
                temp = []
                if weights[i] == smallest_weight:
                    break
                if weights[i] > smallest_weight:
                    temp = weights[:i]
                    break

            if len(temp) > 0:
                for j in temp:
                    sum_weight += j
                    if sum_weight == smallest_weight:
                        break
            if sum_weight == smallest_weight:
                smallest_weight += 1
            else:
                print(smallest_weight)

        print(smallest_weight)

    # https://www.acmicpc.net/problem/1202
    # 최소 용량을 가진 가방 부터 최대로 수용할 수 있는 보석 넣기 (보석 고르는 순서는 가격이 높은 것 부터)

    def getJewelsValue(self):
        num_jewels, num_bags = map(int, sys.stdin.readline().split())
        jewels = []
        bags = []

        for _ in range(num_jewels):
            w, v = map(int, sys.stdin.readline().split())
            heapq.heappush(jewels, (v, w))

        for _ in range(num_bags):
            w = int(sys.stdin.readline())
            heapq.heappush(bags, w)

        # sort jewels by decreasing order
        # 가방 수만 큼 선택하고 모두 가방보다
        max_value = 0
        for bag in bags:
            while jewels and bag >= jewels[len(jewels)-1][1]:
                # if bag >= jewels[len(jewels)-1][1]:  # 용량이 작은 가방에
                # 가방보다 가볍지만 최대로 가격이 높은 보석 넣기
                max_value += jewels.pop()[0]
                break

        print(max_value)
    # https://www.acmicpc.net/problem/2847

    def getLowerLevel(self):
        levels = int(sys.stdin.readline())
        scores = []
        for _ in range(levels):
            scores.append(int(sys.stdin.readline()))
        answer = 0
        temp = 0
        for score in scores:
            if temp > score:
                answer += (temp - score + 1)
            temp = score

        print(answer)

    def getUnplugNumber(self):
        tab_num, total_use = map(int, sys.stdin.readline().split())
        items = list(map(int, sys.stdin.readline().split()))
        priority_hash_map = {}
        plugged = []
        for item in items:
            # priority array 만들기
            if item not in priority_hash_map:
                priority_hash_map[item] = 1
            else:
                priority_hash_map[item] += 1

        # create priority array to refer to
        priority_queue = []
        for item in priority_hash_map:
            count = priority_hash_map[item]
            heapq.heappush(priority_queue, (count, item))

        # priority = []
        # for _ in range(len(priority_queue)):
        #     priority.append(heapq.heappop(priority_queue)[1])

        answer = 0
        for item in items:
            if len(plugged) == tab_num:
                if item not in plugged:  # should unplug an item
                    for p in priority_queue:
                        if p[1] in plugged:
                            plugged.remove(p[1])
                            priority_queue.remove(p)
                            heapq.heappush(priority_queue, (p[0]-1, p[1]))
                            answer += 1
                            break
                    plugged.append(item)
            else:  # if the item is plugged don't add its
                for p in priority_queue:
                    if p[1] == item:
                        priority_queue.remove(p)
                        heapq.heappush(priority_queue, (p[0]-1, p[1]))
                        break
                if item not in plugged:
                    plugged.append(item)

        print(answer)

        # when sokets are all taken, unplug one of them,
        # which will not be used again or will be used later than the others.
        index_use = 0
        for item in items:
            if item in plugged:
                continue
            if len(plugged) < tab_num:
                plugged.append(item)
            if len(plugged) == tab_num:
                index = items.index(item)
                for one in plugged:
                    index_temp = items.index(one)
                    if index_temp > index and index_temp > index_use:
                        index_use = index_temp
                plugged.remove(plugged[index_use])  # unplug
                plugged.append(item)
                answer += 1
        print(answer)

    def getPlaneInGate(self):
        input = sys.stdin.readline
        gate_num = int(input())
        plane_num = int(input())
        answer = 0

        # check if a seat left
        gate = []
        for i in range(gate_num):
            gate.append(0)

        plane_range = []
        for i in range(plane_num):
            plane_range.append(int(input())-1)

        # 비행기가 어디에도 도킹할 수 없으면 더이상 진행하지 않는다
        for i in plane_range:
            isGate = False
            while i >= 0:
                if gate[i] == 0:
                    gate[i] = 1
                    answer += 1
                    isGate = True
                    break
                i -= 1
            if isGate == False:
                break

        print(answer)

    # https://www.acmicpc.net/problem/2810
    def getCupHolders(self):
        input = sys.stdin.readline
        seats_num = int(input())
        seats = list(input())
        answer = 0

        couple = []
        for s in seats:
            answer += 1
            if s == "L" and len(couple) == 2:
                couple = [s]
            elif s == "L" and len(couple) == 1:
                answer -= 1
                couple.append(s)
            elif s == "L":
                couple.append(s)

        print(answer)


instance = GreedyProgramming()
instance.getCupHolders()
instance.getPlaneInGate()
instance.getUnplugNumber()
instance.getLowerLevel()
instance.getJewelsValue()
instance.getSmallest()
instance.getCampingDay()
# print(instance.getChangeNumber(380))
print(instance.getGasPrice())
