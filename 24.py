def solution(id_list, report, k):
    answer = []
    report_to = {} # 어떤 사람이 리포트 한 사람들을 다 저장하는 것
    report_time = {} # 어떤 사람이 리포트 당한 횟수
    
    for id in id_list:
        report_to[id] = []
        report_time[id] = 0
    
    for i in report:
        send, recieve = i.split(' ')
        if recieve not in report_to[send]:
            report_to[send].append(recieve)
            report_time[recieve] += 1
    
    for id in id_list:
        report_success = 0
        for j in report_to[id]:
            if report_time[j] >= k:
                report_success += 1
        answer.append(report_success)
    return answer