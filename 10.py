def solution(s):
    stack = []
    answer = 1
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()

    if len(stack) != 0:
        answer = 0
    return answer