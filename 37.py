def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    edge = set([costs[0][0]])
    while len(edge) != n:
        for cost in costs:
            if cost[0] in edge and cost[1] in edge:
                continue
            if cost[0] in edge or cost[1] in edge:
                edge.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer