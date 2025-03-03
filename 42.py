from collections import deque
def solution(maps):
    start = [0,0]
    q = deque([start])
    moves = [[1,0], [0,1], [-1,0], [0,-1]]
    max_y = len(maps)
    max_x = len(maps[0])
    count = 0
    dist = [[-1] * max_x for _ in range(max_y)]
    dist[start[0]][start[1]] = 1
    while len(q) != 0:
        now = q.popleft()
        count += 1
        for move in moves:
            next = [now[0] + move[0], now[1]+ move[1]]
            if next == [max_x-1, max_y-1] and maps[next[1]][next[0]] == 1:
                return dist[now[1]][now[0]] + 1
            if next[0] >= 0 and next[0] < max_x and next[1] >= 0 and next[1] < max_y:
                if maps[next[1]][next[0]] == 1 and dist[next[1]][next[0]] == -1:
                    q.append(next)
                    dist[next[1]][next[0]] = dist[now[1]][now[0]] + 1
                    
    count = -1
    return count