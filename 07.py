def solution(dirs):
    answer = 0
    current = [0,0]
    historys = []
    for move in dirs:
        before = current
        if move  == 'U':
            current = [before[0], before[1]+1]
        elif move == 'D':
            current = [before[0], before[1]-1]
        elif move == 'R':
            current = [before[0]+1, before[1]]
        elif move == 'L':
            current = [before[0]-1, before[1]]
        history = [before[0],before[1], current[0],current[1]]
        if max(history) <= 5 and min(history) >= -5:
            history = [before, current]
            history.sort()
            if history not in historys:
                historys.append(history)
        else:
            current = before
    answer = len(historys)
    return answer