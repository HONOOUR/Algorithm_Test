class GasStation:
    def getStationIndexCompletingCircle(self, gas: list, cost: list) -> int:
        start_index = 0
        for i in range(len(gas)):
            if gas[i] > cost[i]:
                start_index = i
                break

        total_gas = 0
        total_cost = 0
        for i in range(start_index, len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            if total_gas < total_cost:
                return -1

        for i in range(start_index):
            total_gas += gas[i]
            total_cost += cost[i]
            if total_gas < total_cost:
                return -1

        return start_index


instance = GasStation()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(instance.getStationIndexCompletingCircle(gas, cost))
