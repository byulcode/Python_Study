import re


def solution(new_id):
    # 1단계
    answer = re.sub('[^0-9a-z_.\-]+', '', new_id.lower())  # 정규식 사용
    # 3단계
    answer = re.sub('\.\.+', '.', answer)
    # 4단계
    answer = answer.strip('.')
    # 5단계
    if answer == '':
        answer = 'a'
    # 6단계
    answer = answer[:15].rstrip('.')
    # 7단계
    answer += answer[-1]*(3-len(answer))

    return answer
