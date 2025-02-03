def pre_order(nodes, idx):
  if idx - 1 < len(nodes):
    answer = str(nodes[idx-1])
    answer += pre_order(nodes, idx * 2)
    answer += pre_order(nodes, idx * 2 + 1)
    return str(answer)
  else:
    return ""

def in_order(nodes, idx):
  if idx - 1 < len(nodes):
    answer = ""
    answer += in_order(nodes, idx * 2)
    answer += str(nodes[idx-1])
    answer += in_order(nodes, idx * 2 + 1)
    return str(answer)
  else:
    return ""

def post_order(nodes, idx):
  if idx - 1 < len(nodes):
    answer = ""
    answer += post_order(nodes, idx * 2)
    answer += post_order(nodes, idx * 2 + 1)
    answer += str(nodes[idx-1])
    return str(answer)
  else:
    return ""
nodes = [1, 2, 3, 4, 5, 6, 7]
print(pre_order(nodes, 1))
print(in_order(nodes, 1))
print(post_order(nodes, 1))

