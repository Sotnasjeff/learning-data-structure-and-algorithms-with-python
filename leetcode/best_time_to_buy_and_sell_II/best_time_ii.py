from typing import List

def maxProfit(prices: List[int]) -> int:
    max = 0
    start = prices[0]
    len1 = len(prices)
    for i in range(0 , len1):
        if start < prices[i]: 
            max += prices[i] - start
        start = prices[i]
    return max

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))
        