def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    answer = 0
    dp = [0]*(len(sticker))
    dp[0] = sticker[0]
    m1, m2 = -1, -1
    for i in range(1, len(sticker)-1): # 첫 번째 부터 떼는 경우
        dp[i] = max(sticker[i] + dp[i-2], dp[i-1])
    m1 = dp[-1]

    dp = [0]*(len(sticker))
    dp[1] = sticker[1]
    
    for i in range(2, len(sticker)): # 두 번째 부터 떼는 경우
        dp[i] = max(sticker[i] + dp[i-2], dp[i-1])
    m2 = dp[-1]

    answer = max(m1, m2)

    return answer

if __name__ == '__main__':
    print(
        solution(
            [14, 6, 5, 11, 3, 9, 2, 10]
            # [1, 3, 2, 5, 4]
            # [2, 4, 5, 4, 1]
            # [1]
        )
    )