def solution(n):
    answer = ''
    
    if n <= 3:
        return '124'[n-1]
    
    else:
        q, r = divmod(n, 3) #(몫, 나머지)
        answer += solution(q) + '124'[r]
    return answer

