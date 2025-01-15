N = 5
k = 2
flag = 0
table = [i for i in range(5)]
while len(table) != 1:
  flag += 2
  flag = flag % len(table)
  table.pop(flag)
print(table[0])