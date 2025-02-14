def solution(nums):
    answer = 0
    max_choose = len(nums) / 2
    max_diverse = len(set(nums))
    if max_choose < max_diverse:
        answer = max_choose
    else:
        answer = max_diverse
    return answer