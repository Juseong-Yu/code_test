question1 = [[1,2,3,4,8], [2, 3, 5, 9]]
question2 = [6, 10]

def solution1(arr, target): # 그냥 순회해서 찾기
  answer = False
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        answer = True
  return answer

def solution2(arr, target):
  answer = False
  hash_table = [0] * target
  for num in arr:
    if num <= target:
      hash_table[num] = 1
  for num in arr:
    rest = target - num
    if hash_table[rest] == 1 and rest != num and rest >= 0:
      answer = True
  return answer

for arr, target in zip(question1, question2):
  print(solution1(arr, target))
  print(solution2(arr, target))

