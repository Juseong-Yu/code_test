def solution(graph, start):
  stack = [start]
  answer = []
  tmp = []
  while len(stack) != 0:
    now = stack.pop()
    answer.append(now)
    tmp = []
    for edge in graph:
      if now == edge[0] and edge[1] not in answer and edge[1] not in answer:
        tmp.append(edge[1])
    tmp.reverse()
    stack += tmp
  return answer

graph = [['A','B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
start = 'A'
print(solution(graph, start))
    
graph = [['A','B'], ['A', 'C'], ['B', 'D'], ['B', 'E'],['C','F'],['E', 'F']]
start = 'A'
print(solution(graph, start))