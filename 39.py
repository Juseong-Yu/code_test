from collections import deque

def solution(graph, start):
  stack = deque([start])
  answer = []
  tmp = []
  while len(stack) != 0:
    now = stack.popleft()
    answer.append(now)
    tmp = []
    for edge in graph:
      if now == edge[0] and edge[1] not in stack and edge[1] not in answer:
        tmp.append(edge[1])
    stack += tmp
  return answer

graph = [(1,2), (1,3), (2,4),(2,5),(3,6),(3,7), (4,8), (5,8), (6,9), (7,9)]
start = 1
print(solution(graph, start))

graph = [(0,1), (1,2), (2,3),(3,4),(4,5),(5,0)]
start = 1
print(solution(graph, start))