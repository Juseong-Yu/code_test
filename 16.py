import math
def solution(progresses, speeds):
    answer = []
    deque = []
    for idx in range(len(progresses)):
        left = 100 - progresses[idx]
        tmp = math.ceil(left / speeds[idx])
        deque.append(tmp)
    max_day = deque[0]
    count = 1
    for day in range(1,len(deque)):
        if max_day < deque[day]:
            max_day = deque[day]
            answer.append(count)
            count = 1
        else:
            count += 1
    answer.append(count)

        
    return answer