import collections
import heapq
from collections import deque


class Solutions:
    # def getNumbers(sel, s) -> int:
    #     numbers = ["zero", "one", "two", "three", "four",
    #                "five", "six", "seven", "eight", "nine"]
    #     answer = ""
    #     str_to_number = ""
    #     for item in s:
    #         if item.isalpha():
    #             str_to_number += item
    #         else:
    #             answer += str(item)

    #         if numbers.count(str_to_number) == 1:
    #             num = numbers.index(str_to_number)
    #             answer += str(num)
    #             str_to_number = ""

    #     return answer

    def getArray(self, n, k, cmd):
        answer = ""
        count = 0
        array = []
        while count < n:
            array.append("O")
            count += 1
        cstack = []
        cur_index = k

        for c in cmd:
            if c[0] == "U":
                cur_index -= int(c[2])
            elif c[0] == "D":
                cur_index += int(c[2])
            elif c[0] == "C":
                # array[cur_index] = "X"
                array.pop(cur_index)
                cstack.append(cur_index)
                # if cur_index > len(array) - 1:
                #     cur_index -= 1
                # if cur_index == n-1:
                #     cur_index -= 1
                # else:
                #     cur_index += 1
            else:  # "z"
                removed_index = cstack.pop()
                # array[removed_index] = "O"
                array.insert(removed_index, "O")

        # for removed in cstack:
        while cstack:
            array.insert(cstack.pop(), "X")

        for item in array:
            answer += item

        return answer

# s = "one4seveneight"
# print(instance.getNumbers(s))


instance = Solutions()

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(instance.getArray(n, k, cmd))
