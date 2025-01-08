def solution(arr1, arr2):
    answer = []
    for row in range(len(arr1)):
        list = []
        for col in range(len(arr2[0])):
            num = 0
            for i in range(len(arr1[row])):
                x = arr1[row][i]
                y = arr2[i][col]
                num += x*y
            list.append(num)
        answer.append(list)
    return answer