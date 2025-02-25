def solution(graph, source):
  # 노드의 갯수
  num_vertices = len(graph)
  # 비용 계산 배열
  distances = [float('inf')] * num_vertices
  distances[source] = 0

  # 직전 경로 배열 계산
  predecessor = [None] * num_vertices

  for temp in range(num_vertices - 1): # 벨만 포드 알고리즘은 원래 노드-1번 반복해야함(최단 경로가 한 노드씩 결정됨)
    for u in range(num_vertices): # 시작 노드에서 각 노드를 거쳐 어떤 노드에 도달 할때에 값을 계산해서 기존값보다 작으면 바꿈
      for v, weight in graph[u]: # 해당 노드에서 갈수 있는 간선을 확인해서 기존 경로보다 가중치가 적으면 바꿈
        if distances[u] + weight < distances[v]: # u까지 가서 v로 가는 것과 기존에 v로 가는 것의 가중치를 비교
          distances[v] = distances[u] + weight
          predecessor[v] = u
  
  # 음의 가중치 순회 체크(순환하면서 무한한 음수의 값으로 가중치 값이 진행되는 경우 무한히 반복하는 것이 답이 되니 답이 안됨.)a
  for u in range(num_vertices):
    for v, weight in graph[u]: # 이미 벨만-포드 알고리즘이 끝났는데 수정해야할 가중치 배열 값이 있으면 음의 가중치 aa순회가 되는 것임
      if distances[u] + weight < distances[v]:
        return [-1]
      
  return [distances, predecessor]



graph = [[(1,4), (2,3), (4, -6)], [(3,5)], [(1,2)], [(0,7), (2,4)], [(2, 2)]]
source = 0
print(solution(graph, source))

graph = [[(1,5), (2,-1)], [(2,2)], [(3,-2)], [(0,2), (1,6)]]
source = 0
print(solution(graph, source))