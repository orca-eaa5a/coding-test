"""
하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다.
"""
import heapq

def solution(jobs):
    q = []
    proc_fin_time = 0
    answer = 0
    for s, dur in jobs:
        if not heapq:
            heapq.heappush(q, (dur, s))
            proc_fin_time += dur
        else:
            if proc_fin_time > s:
                heapq.heappush(q, (dur, s))
            elif proc_fin_time == s:
                heapq.heappop(q)
                heapq.heappush(q, (dur, s))
                proc_fin_time += dur
            else: # proc_fin_time < s <-- 여유가 있는 상태
                while True:
                    if proc_fin_time >= s:
                        heapq.heappush((dur, s))
                    if proc_fin_time < s:
                        break
                    proc_fin_time += q[0][0]
                    heapq.heappop(q)
        