"""
세계 최고의 갑부가 된 어피치
매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return

gems 배열의 크기는 1 이상 100,000 이하
"""
from collections import defaultdict
def solution(gems):
    """
    :requirements
        1. 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
        2. 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return
        3. 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return
    """
    kinda_gems = len(list(set(gems)))
    s = set()
    r = []
    d = defaultdict(int)
    for i, g in enumerate(gems):
        d[g] = i
        if len(d) == kinda_gems:
            mi = 0xffffff
            ma = -1
            min_k = None
            max_k = None            
            for k in d:
                if d[k] < mi:
                    mi = d[k]
                    min_k = k
                if d[k] > ma:
                    ma = d[k]
                    max_k = d[k]
            r.append((ma-mi, mi, ma))
            del d[min_k]
            # s.add(g)
    r.sort(key=lambda x:(x[0], x[1]))
    print(r)
    return [r[0][1]+1, r[0][2]+1]