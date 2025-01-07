def solution(arr):
  unique_arr = list(set(arr))
  unique_arr.sort(reverse=True)
  return unique_arr



arrs = [[4, 2, 2, 1, 3, 4], [2, 1, 1, 3, 2, 5, 4]]
for arr in arrs:
  print(solution(arr))