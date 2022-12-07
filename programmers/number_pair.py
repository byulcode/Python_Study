from collections import Counter

X = input()
Y = input()


def solution(X, Y):
    answer = '-1'
    arr_x = list(X)
    arr_y = list(Y)
    common = set(arr_x) & set(arr_y)

    cnt_x, cnt_y = Counter(arr_x), Counter(arr_y)

    if common:
        answer = ''
        sorted_num = sorted(common, reverse=True)

        for num in sorted_num:
            answer += num * min(cnt_x[num], cnt_y[num])

        if sum(list(map(int, list(answer)))) == 0:
            answer = "0"
    return answer


print(solution(X, Y))
