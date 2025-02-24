def solution(graph, start):
  visited = [start]
  distances = {node : [float('inf'), float('inf')] for node in graph}
  distances[start] = [0, start]
  while len(visited) != len(graph):
    print(distances, start)
    check = visited[-1]
    for node, cost in graph[check].items():
      if distances[node][0] > cost:
        distances[node] = [cost, check]
    next_check = float('inf')
    next_node = check
    for cost, node in distances.items():
      if cost < next_check and node not in visited:
        next_check = cost
        next_node = node
    visited.append(node)

graph = {
  'A':{'B':9, 'C': 3},
  'B':{'A':5},
  'C':{'B':1}
}
start = 'A'
solution(graph, start)