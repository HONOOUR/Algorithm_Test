from typing import List
import heapq
import collections


class TaskScheduler:
    def getTotalTime(self, tasks: List, period: int) -> int:
        # counter becomes a dic of word occurrence
        counter = collections.Counter(tasks)
        # same with
        # for task in tasks:
        #     if not task in task_sorted:
        #         task_sorted[task] = 0
        #     task_sorted[task] += 1

        result = 0

        while True:
            sub_count = 0

            # n+1 -> run tasks without idle time
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                # dic's value--
                counter.subtract(task)
                counter += collections.Counter()

            if not counter:
                break

            # add idle time
            result += (n+1)-sub_count
        return result


instance = TaskScheduler()
tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(instance.getTotalTime(tasks, n))
