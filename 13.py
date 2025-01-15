def solution(board, moves):
    answer = 0
    stack = []
    answer == 0
    for pick in moves:
        doll = None
        for row in range(len(board)):
            if board[row][pick-1] != 0:
                doll = board[row][pick-1]
                board[row][pick-1] = 0
                break

        if doll != None:
            if len(stack) == 0:
                stack.append(doll)
            else:
                if stack[-1] == doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
    return answer