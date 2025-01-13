def solution(s):
    stack = []
    answer = True
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                answer = False
                break
            tmp = stack.pop()
            if tmp == ')':
                answer = False
                break
    if len(stack) != 0:
        answer = False
    return answer