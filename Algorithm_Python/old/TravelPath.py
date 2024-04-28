from collections import deque


def getTravelPath(tickets):
    answer = []
    queue = deque()

    tickets.sort()
    for ticket in tickets:
        if ticket[0] == "ICN":
            queue = deque([([ticket[0]], ticket)])
            tickets.remove(ticket)
            break

    while queue:
        if len(tickets) == 0:
            break
        path, [depart, arrive] = queue.popleft()
        for ticket in tickets:
            if ticket[0] == arrive:
                path.append(ticket[0])
                queue.append((path, ticket))
                tickets.remove(ticket)
                break

    answer, ticket = queue.popleft()
    answer.append(ticket[1])
    return answer


getTravelPath([["ICN", "SFO"]])
