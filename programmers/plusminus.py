'''
음양 더하기

'''
def solution(absolutes, signs):
    answer = 0
    
    for i, sign in enumerate(signs):
        if sign == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

'''
다른사람 풀이: 
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
'''