def solution(n):
    answer = 0
    dp = [0]*5001
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*3 + sum(dp[:i-3])*2 + 2
    answer = dp[n]
    return answer%1000000007