from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i-coin]+1)
        
    if dp[amount] != float('inf'):
        return dp[amount]

    return -1

print(coinChange([1,2,5], 11))


def lastStoneWeightII(stones: List[int]) -> int:
    total = sum(stones)
    Max_weight = total // 2
    current = [0] * (Max_weight + 1)
    for stone in stones:
        for wgt in range(Max_weight, stone - 1, -1):
            current[wgt] = max(current[wgt], stone + current[wgt - stone])
    return total - 2 * current[Max_weight]

#Greedy Algorithm
def findContentChildren(greeds: List[int], cookies: List[int]) -> int:
    greeds.sort()
    cookies.sort()
    
    count = 0
    i, j = 0,0
    
    while i < len(greeds) and j < len(cookies):
        if cookies[j] >= greeds[i]:
            count += 1
            i += 1
        j+= 1
        
    return count

print(coinChange([1,2,5], 11))