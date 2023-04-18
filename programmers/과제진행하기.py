
def strftime_to_timestamp(strftime):
    hh, mm = map(int, strftime.split(":"))
    return hh*60 + mm

def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x:x[1])
    for p in plans:
        subject, _time, duration = p
        _time = strftime_to_timestamp(_time)
        duration = int(duration)
        # stack의 맨 위는 현재 하고있는 작업
        if stack:
            prev_subject, prev_time, prev_duration = stack.pop()
            time_delta = _time - prev_time
            if time_delta < prev_duration:
                remain_duration = prev_duration - time_delta
                stack.append((prev_subject, _time, remain_duration))
            else:
                answer.append(prev_subject)
                current_time = prev_time + prev_duration
                ava_duration = _time - current_time
                while stack and ava_duration:
                    prev_subject, prev_time, prev_duration = stack.pop()
                    if prev_duration > ava_duration:
                        stack.append((prev_subject, current_time + ava_duration, prev_duration - ava_duration))
                        break
                    answer.append(prev_subject)
                    current_time = current_time + prev_duration
                    ava_duration -= prev_duration
                    
        stack.append((subject, _time, duration))
    
    while stack:
        answer.append(stack.pop()[0])
    return answer

if __name__ == '__main__':
    print(
        solution(
            # [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
            # [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
            [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "40"]]
            # [["korean", "11:40", "30"], ["english", "12:00", "20"]]
        )
    )