# 프로그래머스 Lv1 과일 장수

kk = 3
mm = 4
scores = [1, 2, 3, 1, 2, 3, 1]


def solution(k, m, score):
    answer = 0
    min_score = []
    score.sort(reverse=True)

    # m씩 나누기. 마지막 박스의 사과가 m보다 적을 경우 삭제
    box = [score[i:i + m] for i in range(0, len(score), m)]
    if (len(box[-1])) < m:
        box.pop()

    min_val = k
    for apple in box:
        min_val = min(min(apple), min_val)
        min_score.append(min_val)

    for val in min_score:
        answer += val * m
    return answer


print(solution(kk, mm, scores))
