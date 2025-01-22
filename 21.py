def solution(want, number, discount):
    answer = 0
    dic = {}
    for idx in range(len(want)):
        dic[want[idx]] = number[idx]

    tmp_dic = dic.copy()
    flag = False
    for start in range(0, len(discount) - 9):
        for item_idx in range(start, start + 10):
            item = discount[item_idx]
            if item in tmp_dic and tmp_dic[item] > 0:
                tmp_dic[item] -= 1
            else:
                flag = True
                break
        if flag == False:
            answer += 1
        flag = False
        tmp_dic = dic.copy()


    return answer