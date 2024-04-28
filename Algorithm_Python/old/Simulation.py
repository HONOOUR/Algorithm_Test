def solution(k):
    numbers = ""
    for i in range(k+1):
        if i % 10 == 0:
            i = 0
        numbers += str(i)

    num_list = list(numbers)
    new_num_list = []
    count = 1
    while num_list:

        if (count >= 11):
            if len(num_list) >= 2:
                temp_str = ""
                pop_count = count // 10
                for _ in range(pop_count):
                    temp_str += str(num_list.pop(0))
                new_num_list.append(temp_str)
            else:
                new_num_list.append(str(num_list.pop(0)))
        else:
            new_num_list.append(str(num_list.pop(0)))
        count += 1

    result = new_num_list[k-1]
    return result


solution(11)


def getTimeStamp(hh, mm):
    if hh < 10:
        answer = "0" + str(hh) + ":"
    else:
        answer = str(hh) + ":"
    if mm < 10:
        answer += "0" + str(mm)
    else:
        answer += str(mm)
    return answer


def getLastTimeForArrival(n, t, m, timetable):
    count = n
    interval = t
    num_crew = m
    timetable.sort()
    answer = ""
    if len(timetable) >= count * num_crew:
        # faster than last crew
        last_crew_time = timetable[count*num_crew-1]
        crew_hh, crew_mm = map(int, last_crew_time.split(":"))

        interval_hh = 0
        interval_mm = 0
        # find interval time faster than last crew
        if interval * (count-1) // 60 >= 1:
            interval_hh = 9 + interval * (count-1) // 60
            interval_mm = interval * (count-1) % 60
        else:
            interval_hh = 9
            interval_mm = interval * (count-1)

        # if everyone is faster than last interval, then find between
        if crew_hh < interval_hh or (crew_hh == interval_hh and crew_mm < interval_mm) or (crew_hh == interval_hh and crew_mm == interval_mm):
            hh = mm = 0
            if crew_mm == 0:
                hh = crew_hh - 1
                mm = 59
            else:
                hh = crew_hh
                mm = crew_mm - 1
            answer = getTimeStamp(hh, mm)

        # if last interval is faster than the last crew, then select last interval
        elif crew_hh > interval_hh or (crew_hh == interval_hh and crew_mm > interval_mm):
            answer = getTimeStamp(interval_hh, interval_mm)

    else:
        interval_hh = 0
        interval_mm = 0
        if interval * (count-1) // 60 >= 1:
            interval_hh = 9 + interval * (count-1) // 60
            interval_mm = interval * (count-1) % 60
        else:
            interval_hh = 9
            interval_mm = interval * (count-1)
        answer = getTimeStamp(interval_hh, interval_mm)

    return answer


getLastTimeForArrival(1,	1,	5,	["08:00", "08:01", "08:02", "08:03"])


def getShuttleTime(n, t, m, timetable):
    answer = ""
    shuttle_num = n
    interval = t
    seats_num = m
    start_time = 540  # 9:00
    shuttle_timetable = []
    # shuttle_timetable = [shuttle_time, crew_time]
    for n in range(shuttle_num):
        for _ in range(seats_num):
            shuttle_timetable.append([start_time + n*interval, -1])


def getTriangle(n):
    triangle = []
    last_num = 0
    # set last number and triangle array
    for i in range(1, n+1):
        last_num += (i)
        triangle.append([0]*i)

    num = 1
    move_y = [-1, 0, 1]
    move_x = [0, 1, 0]
    turn = 0
    while num <= last_num:

        for m in range(len(move_y)):
            for i in range(1, n+1-turn):
                triangle[i+move_y[0]][move_x[0]] = num
                num += 1
            move_x[0] = move_x[0]+1
            turn += 1

            for i in range(1, n+1-turn):
                triangle[move_y[1]][i] = num
                num += 1
            turn += 1

            for i in range(1, n+1-turn):
                last_index = len(triangle[move_y[2]])-1
                triangle[move_y[2]][last_index - move_x[2]]
                move_x[2] += 1


getTriangle(5)
