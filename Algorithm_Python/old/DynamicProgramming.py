class DynamicProgramming:
    def fibonacci(self, num: int) -> int:
        array = {}
        array[1] = array[2] = 1
        for i in range(3, num+1):
            array[i] = array[i-1] + array[i-2]

        return array[num]

    def knapsack(self, items: list, limit: int) -> int:
        # value = [number of item][weight limit]
        # row = 0, the number of items is zero
        value = []

        for i in range(len(items)+1):
            value.append([])
            wi = items[i-1][1]  # the weight of i
            for w in range(limit+1):
                if i == 0 or w == 0:
                    # value[i][w] = 0
                    value[i].append(0)
                elif wi > w:
                    # not packing i
                    # value[i][w] = value[i-1][w]
                    value[i].append(value[i-1][w])
                else:
                    vi = items[i-1][0]
                    value[i].append(max(value[i-1][w], value[i-1][w-wi] + vi))
                    # value[i][w] = max(value[i-1][w], value[i-1][w-1] + vi)

        return value[len(items)][limit]


instance = DynamicProgramming()
print(instance.fibonacci(10))
# item = (value, weight)
# the index of items starts from zero
items = [(1, 1), (6, 2), (18, 5), (22, 6), (28, 7)]
print(instance.knapsack(items, 11))
print(instance.knapsack(items, 20))
