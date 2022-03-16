'''
<문자열 압축>
1. n개 단위로 자른다 -> n의 최대값은 문자 길이의 절반
2. 자르다가 남는 문자열은? -> 뒤에 이어 붙임
3. 반복이 10개 이상인 경우, s의 길이가 1인 경우 고려하기!
'''


def solution(s):  # 내가 짠 코드
    answer = 1000

    if len(s) == 1:  # s의 길이가 1인 경우
        return 1

    for n in range(1, len(s) // 2 + 1):
        res = ''  # 압축된 문자열
        tmp = s[:n]
        cnt = 1  # 반복된 횟수(한번일 경우 숫자는 생략)
        for i in range(n, len(s) + n, n):  # n부터 시작, n씩 증가
            if tmp == s[i:i+n]:  # 반복된 경우
                cnt += 1
            else:
                if cnt == 1:
                    res += tmp
                else:
                    res += str(cnt) + tmp
                tmp = s[i:i+n]
                cnt = 1
        answer = min(answer, len(res))
    return answer


print(solution('abcabcabcabcdededededede'))
