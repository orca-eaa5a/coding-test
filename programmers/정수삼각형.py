"""
https://school.programmers.co.kr/learn/courses/30/lessons/43105
"""
dp = [0]*125251

def solution(triangle):
    global dp
    answer = 0
    prev_len = 0
    dp_idx = 0
    for floor in reversed(range(len(triangle))):
        for lev in range(len(triangle[floor])):
            if prev_len == 0:
                dp[lev] = triangle[floor][lev]
            else:
                if_left = triangle[floor][lev] + dp[dp_idx-prev_len]
                if_right = triangle[floor][lev] + dp[dp_idx-prev_len+1]
                dp[dp_idx] = max(if_left, if_right)
            dp_idx += 1
        prev_len = len(triangle[floor])
    answer = dp[dp_idx-1]

    return answer