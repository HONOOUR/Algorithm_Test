def countSwaps(a):
    count = 0
    for _ in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                count += 1
	print('Array is sorted in ' + count ' swaps.')
	print('First Element: ' +  a[0])
	print('Last Element: ' + a[-1])

# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def maximumToys(prices, k):
    # sort and pick as many as I can
    prices.sort()
    n = len(prices)
    max_toy_count = 0
    for i in range(n):
        money_spent = 0
        toy_count =0
        while i < n and money_spent + prices[i] <= k:
            if money_spent + prices[i] <= k:
                money_spent+=prices[i]
                i += 1
                toy_count += 1
            max_toy_count = max(max_toy_count, toy_count)
    return max_toy_count
    
from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comparator(a, b):
        # order by score desc
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else: # order by name asc
            if a.name <= b.name:
                return -1
            else:
                return 1

