def solution(answers):
    answer = []
    A_correct = 0
    B_correct = 0
    C_correct = 0
    for i in range(len(answers)):
        A_answer = i % 5 + 1
        
        if i % 2 == 0 :
            B_answer = 2
        else : 
            B_num =  (i // 2) % 4
            if B_num == 0:
                B_answer = 1
            else :
                B_answer = B_num + 2
                
        C_num = (i // 2) % 5
        C_list = [3, 1, 2, 4, 5]
        C_answer = C_list[C_num]
        
        if A_answer == answers[i]:
            A_correct += 1
        if B_answer == answers[i]:
            B_correct += 1
        if C_answer == answers[i]:
            C_correct += 1
    correct = [A_correct, B_correct, C_correct]
    max = 0
    max_s = []
    for j in range(len(correct)):
        if max < correct[j]:
            max = correct[j]
            max_s = [j+1]
        elif max == correct[j]:
            max_s.append(j+1)
    
    return max_s