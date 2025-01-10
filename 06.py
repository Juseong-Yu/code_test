def solution(N, stages):
    answer = []
    stages.sort(reverse = True)
    passer = 0
    count = 0
    back = 0
    errors = [0] * N 
    tmp = []
    for stage in stages:
        passer += 1
        if stage != N + 1:
            if stage != back:
                count = 1
                error =  count / passer
                errors[stage-1] = error
            else :
                count += 1
                error = count / passer
                errors[stage-1] = error
            back = stage
        else :
            count = 0
            back = stage
    for index, error in enumerate(errors):
        tmp.append([error, N - index])
    tmp.sort(reverse = True)
    for lst in tmp:
        answer.append(N - lst[1] + 1)
    return answer