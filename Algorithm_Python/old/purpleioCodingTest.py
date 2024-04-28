# 1. 분기 숫자 구하기
def getQuarter(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    else:
        return 4


getQuarter(11)


# 2. 사용하지 않는 가장 작은 숫자 찾기
def getSmallestNumber(nums):
    nums.sort()
    smallest = nums[0]
    for num in nums:
        if smallest < num:
            return smallest
        elif smallest == num:
            smallest += 1
        else:
            continue
    return smallest


getSmallestNumber([0, 1, 2, 3, 4, 5, 6])


# 3. 승점구하기
def getWinningPoint(games):
    total = 0
    for game in games:
        team_a = game[0]
        team_b = game[2]
        score = abs(int(team_a)-int(team_b))
        if score > 0:
            total += 3
        elif score == 0:
            total += 1
    return total


getWinningPoint(["3:1", "2:2", "1:3"])


# 4. 더하고 빼기
def getFruit(n):
    if 10 <= n < 100000:
        return 'apple'


# 1. 모음 찾기
def getVowelsCount(str):
    count = 0
    for s in str.lower():
        if s in 'aeiou':
            count += 1

    return count


getVowelsCount('abracadabra')

# 2. 중간 숫자 찾기


def getMidNumber(numbers):
    numbers.sort()
    return numbers[1]


getMidNumber([5, 1, 2])

# 3. 친구 찾기


def getFriends(users):
    friends = []
    for user in users:
        if len(user) == 4:
            friends.append(user)

    return friends


getFriends(["Ryan", "Kieran", "Mark"])

# 4. 아이큐테스트


def getEvenOrOddNumber(numbers):
    odd = []
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if len(even) == 1:
        return even.pop()
    else:
        return odd.pop()
