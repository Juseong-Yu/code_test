def solution(numbers):
    answer = []
    for i in range(1, len(numbers)):
        for j in range(0, i):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)
    answer.sort()
    return answer