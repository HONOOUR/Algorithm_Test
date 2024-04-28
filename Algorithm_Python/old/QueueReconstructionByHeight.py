from typing import List
import heapq


class QueueReconstructionByHeight:
    def getQueuByHeight(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        heap = []
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])  # create max heap

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result


instance = QueueReconstructionByHeight()
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(instance.getQueuByHeight(people))
