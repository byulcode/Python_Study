'''
예산
- 최대 몇 개의 부서에 물품을 지원할 수 있는지 return
- d : 부서별로 신청한 금액 budget : 예산
'''
def solution(d, budget):
    answer = 0
    d.sort()
    res = 0
    
    for amount in d:
        if res + amount <= budget:
            res += amount
            answer += 1
        else:
            break
    
    return answer

