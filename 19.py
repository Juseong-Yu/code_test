string_list = ['apple', 'banana', 'cherry']
query_list = ['banana', 'kiwi', 'melon', 'apple']

def solution(string_list, query_list):
  answer = []
  hash_result = 0
  hash_table = []
  m = 1000000007
  for word in string_list:
    hash_result = 0
    for idx in range(len(word)):
      hash_result += (ord(word[idx]) * (31 ** idx)) % m
    hash_table.append(hash_result)

  for word in query_list:
    hash_result = 0
    for idx in range(len(word)):
      hash_result += (ord(word[idx]) * (31 ** idx)) % m
    if hash_result in hash_table:
      answer.append(True)
    else:
      answer.append(False)

  return answer
print(solution(string_list, query_list))