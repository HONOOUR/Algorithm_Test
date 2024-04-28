from typing import List


class BestTimeToBuyAndSellStock:
    def getMaxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result

    def getMaxProfit_2(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))


instance = BestTimeToBuyAndSellStock()
prices = [7, 1, 5, 3, 6, 4]
print(instance.getMaxProfit(prices))
print(instance.getMaxProfit_2(prices))
