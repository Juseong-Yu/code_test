import math
def solution(enroll, referral, seller, amount):
    answer = []
    refer_dic = {}
    money_dic = {}
    for idx in range(len(enroll)):
        name1 = enroll[idx]
        name2 = referral[idx]
        refer_dic[name1] = name2
        money_dic[name1] = 0
    for idx in range(len(amount)):
        name = seller[idx]
        money = amount[idx] * 100
        while name != '-' and money > 0:
            money_dic[name] += money - (money // 10)
            parent_name = refer_dic[name]
            name = parent_name
            money //=10
    answer = [money_dic[name] for name in enroll]
    return answer