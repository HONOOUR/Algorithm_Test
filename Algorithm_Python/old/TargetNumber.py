from collections import deque


class TargetNumber:
    def getTargetAnswers(self, numbers: list, target: int):
        answer = 0
        queue = deque([(0, 0)])  # (sum, level)

        while queue:
            s, level = queue.popleft()
            if s == target and level == len(numbers):
                answer += 1
            elif level < len(numbers):
                queue.append((s+numbers[level], level + 1))
                queue.append((s-numbers[level], level + 1))

        return answer


instance = TargetNumber()
print(instance.getTargetAnswers([1, 1, 1, 1, 1], 3))
