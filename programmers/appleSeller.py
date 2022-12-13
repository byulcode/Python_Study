# 프로그래머스 Lv1 과일 장수

kk = 3
mm = 4
scores = [1, 2, 3, 1, 2, 3, 1]


def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    box = [score[i:i + m] for i in range(0, len(score), m)]
    for apple in box:
        if len(apple) == m:
            answer += min(apple) * m

    return answer


print(solution(kk, mm, scores))
