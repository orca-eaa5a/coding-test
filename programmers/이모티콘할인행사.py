"""
1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
2. 이모티콘 판매액을 최대한 늘리는 것.
1번 목표가 우선이며, 2번 목표가 그 다음입니다.

n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매
할인율은 10%, 20%, 30%, 40% 중 하나로 설정

각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입

1 ≤ users의 길이 = n ≤ 100
100 ≤ 가격 ≤ 1,000,000 (가격은 100의 배수입니다.)
1 ≤ emoticons의 길이 = m ≤ 7

완전탐색 밖에 방법이 없어 보이는데...
각 할인 비율을 이모티콘에 반영할 때, 최대 28개의 원소
"""
from itertools import product
from collections import defaultdict
def solution(users, emoticons):
    emo_len = len(emoticons)
    v = product([40, 30, 20, 10], repeat=emo_len)
    v = list(v)
    case = defaultdict(dict)
    for _id, dcs in enumerate(v): # max 16384
        case[_id] = {
            'emo_serv': 0,
            'earned': 0
        }
        total_earned = 0
        for dc_lim, budget_lim in users: # max 100
            l = budget_lim
            current_earned = 0
            for dc, emo_price in zip(dcs, emoticons): # max 7
                if dc >= dc_lim:
                    p = int(emo_price - emo_price*(dc/100))
                    l -= p
                    current_earned += p
                if l <= 0:
                    case[_id]['emo_serv'] += 1
                    current_earned = 0
                    break
            total_earned += current_earned
        case[_id]['earned'] = total_earned
    
    max_service_subs = -1
    earn_max = -1
    for k in case:
        if case[k]['emo_serv'] > max_service_subs:
            max_service_subs = case[k]['emo_serv']
            earn_max = case[k]['earned']
        elif case[k]['emo_serv'] == max_service_subs:
            if case[k]['earned'] > earn_max:
                earn_max = case[k]['earned']

    return [max_service_subs, earn_max]

if __name__ == '__main__':
    print(
        solution(
            [[40, 10000], [25, 10000]], [7000, 9000]
        )
    )