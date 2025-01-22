def solution(record):
    answer = []
    dic = {}
    list1 = []
    for line in record:
        line = line.split(' ')
        method = line[0]
        uid = line[1]
        if method == 'Enter':
            name = line[2]
            dic[uid] = name
            list1.append([method, uid])
        elif method == 'Leave':
            list1.append([method, uid])
        elif method == 'Change':
            name = line[2]
            dic[uid] = name
    
    for line in list1:
        if line[0] == 'Enter':
            answer.append(dic[line[1]] + '님이 들어왔습니다.')
        if line[0] == 'Leave':
            answer.append(dic[line[1]] + '님이 나갔습니다.')
    return answer