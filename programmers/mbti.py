# 프로그래머스 성격유형 검사하기


def solution(survey, choices):
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    for i in range(len(survey)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            dict[left] += (4 - choices[i])
        else:
            dict[right] += (choices[i] - 4)

    answer += 'R' if dict['R'] >= dict['T'] else 'T'
    answer += 'C' if dict['C'] >= dict['F'] else 'F'
    answer += 'J' if dict['J'] >= dict['M'] else 'M'
    answer += 'A' if dict['A'] >= dict['N'] else 'N'

    return answer
