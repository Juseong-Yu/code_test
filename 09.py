decimal = [10, 27, 12345]

def solution(num):
  stack = []
  answer = ''
  while 1:
    stack.append(num % 2)
    num = num // 2
    if num == 0:
      break
  for i in range(len(stack)):
    top = stack.pop()
    answer += str(top)
  return answer


for dec in decimal:
  print(solution(dec))
  