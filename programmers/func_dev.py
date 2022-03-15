'''
기능개발(스택 / 큐)
'''
def solution(progresses, speeds):
    answer = [] 
    cnt = 0
    days = 0
    
    while len(progresses) > 0 : # 큐가 비어있지 않을 때
        if (progresses[0] + days * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            days += 1
    answer.append(cnt)
    return answer