'''
짝지어 제거하기
1. 짝 제거 후 앞뒤로 문자열 이어 붙임
2. 성공적으로 수행할 시 1, 아닐 경우 0을 리턴

* 스택 사용함!
'''


def solution(s):
    answer = -1

    if len(s) % 2 == 1:
        return 0   # 길이가 홀수면 무조건 남음
    if len(s) == 2:  # 길이가 2이고 두 알파벳이 같으면 제거 성공
        return 1 if s[0] == s[1] else 0

    stack = [s[0]]

    for v in s[1:]:
        if len(stack) > 0 and v == stack[-1]:
            stack.pop()
        else:
            stack.append(v)
    if len(stack) > 0:
        answer = 0
    else:
        answer = 1

    return answer
