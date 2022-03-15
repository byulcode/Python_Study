def solution(record):
    answer = []
    dict = {}

    # 딕셔너리에 user id, nickname 저장
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dict[sentence_split[1]] = sentence_split[2]

    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % dict[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % dict[sentence_split[1]])

    return answer
