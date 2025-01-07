def solution(arr):
  arr.sort()
  return arr

arrs = [[1, -5, 2, 4, 3], [2, 1, 1, 3, 2, 5, 4], [6, 1, 7]]
for arr in arrs:
  print(solution(arr))