
def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=len)

    for i in s:
        k = i.split(',')
        for j in k:
            if j not in answer:
                answer.append(j)

    answer = list(map(int, answer))
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
