#!/usr/bin/python3 

def makeChange(coins, total):
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
    return dp[total] if dp[total] != float('inf') else -1
