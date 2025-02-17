def solution(n, words):
    answer = []
    wrong = 0
    for idx in range(1, len(words)):
        if words[idx][0] != words[idx-1][-1] or words[idx] in words[:idx]:
            wrong = idx
            break
    if wrong == 0:
        answer = [0, 0]
    else:
        if (wrong + 1) % n == 0:
            answer1 = n
        else:
            answer1 = (wrong + 1) % n
        answer2 = wrong // n + 1
        answer = [answer1, answer2]
    return answer