def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = []
    for idx in range(len(prices)):
        if len(stack) == 0:
            stack.append(idx)
        
        else:
            flag = False
            while flag == False:
                if prices[stack[-1]] > prices[idx]:
                    idx2 = stack.pop()
                    answer[idx2] = idx - idx2
                else:
                    flag = True
                if len(stack) == 0:
                    flag = True
            stack.append(idx)

    return answer